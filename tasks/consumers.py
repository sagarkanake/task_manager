import json
from channels.generic.websocket import AsyncWebsocketConsumer
import logging
logger = logging.getLogger(__name__)
class TaskConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("tasks", self.channel_name)
        await self.accept()
        await self.send(text_data=json.dumps({
            "type" : 'connection established',
            "message" : 'hi'
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("tasks", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        logger.debug(f"Received message from group: {data}")

        # Process data received from the client
        # For example, send a message to the group
        await self.channel_layer.group_send(
            "tasks",
            {
                "type": "task_message",
                "message": data,
            }
        )

    async def task_message(self, event):
       status = event["status"]
       details = event["details"]  # Receiving the array
        
        # Send the message to WebSocket client
       await self.send(text_data=json.dumps({
            "status": status,
            "details": details,  # Sending the array back as part of the WebSocket message
        }))
