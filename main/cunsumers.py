import json
from channels.generic.websocket import WebsocketConsumer
from django.shortcuts import get_object_or_404

from main.models import Conversation, Message


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print('yessss')
        self.accept()

    def disconnect(self, close_code):
        print('noooooo') 
        

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        user = self.scope['user']
        message = text_data_json["message"]
        M = Message(conv=get_object_or_404(Conversation,id=int(self.scope['url_route']['kwargs']['pk'])) , sender=user, content=message)
        M.save()
        self.send(text_data=json.dumps({"message": message, "sender":str(user)}))