from rest_framework import viewsets
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from .tasks import process_task

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        # Start the Celery task
        task = process_task.delay(serializer.instance.id)
        
        return Response({
            "task_id": serializer.instance.id,
            "celery_task_id": task.id,
            "status": "queued"
        }, status=201, headers=headers)