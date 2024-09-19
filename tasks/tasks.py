from celery import shared_task
from .models import Task
import time

@shared_task(bind=True)
def process_task(self, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.status = 'in_progress'
        task.save()

        # Simulate a long-running task
        time.sleep(60)

        task.status = 'completed'
        task.save()
        return {"status": "completed", "task_id": task_id}
    except Task.DoesNotExist:
        return {"status": "failed", "task_id": task_id, "reason": "Task not found"}