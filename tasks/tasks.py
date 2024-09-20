from celery import shared_task
from .models import Task
import time
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import logging
logger = logging.getLogger(__name__)
@shared_task(bind=True)
def process_task(self, task_id):
    try:
        time.sleep(6) 
        task = Task.objects.get(id=task_id)
        task.status = 'In Progress'
        task.save()
        # Inform front end that the task is in progress
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "tasks",
            {
                "type": "task_message",
                "task_id" : task_id,
                "message": ["Task started", "Processing", "Task completed"],
                "status": "in_progress",
                "details": task_id,
            }
        )

        # Simulate a long-running task
        print(f"Processing task {task_id}...")  # Log when task starts
        logger.debug(f"Completed processing task {task_id}")
        time.sleep(5)  # Simulating processing time
        print(f"Waiting to send completion message for task {task_id}...")  # Log before delay
        time.sleep(10)  # Wait before sending the message
    
        print(f"Sending task completion message for task {task_id}") 
        taskall = Task.objects.all()

        # After the process is complete, send a message to WebSocket
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "tasks",
            {
                "type": "task_message",
                "task_id" : task_id,
                "message": ["Task started", "Processing", "Task completed"],
                "status": "completed",
                "details": task_id,
            }
        )
        print("Sent task completion message for Task ")
        logger.debug(f"Sent WebSocket message for task {task_id}")
        task.status = 'Completed'
        task.save()
        return {"status": "completed", "task_id": task_id}
    except Task.DoesNotExist:
        return {"status": "failed", "task_id": task_id, "reason": "Task not found"}