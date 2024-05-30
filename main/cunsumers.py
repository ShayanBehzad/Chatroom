import json
from channels.generic.websocket import WebsocketConsumer
from django.shortcuts import get_object_or_404
from asgiref.sync import async_to_sync
from main.models import *
from register.models import *



class PvChatCunsumer(WebsocketConsumer):
    def connect(self):
        print(self.scope)
        self.room_name = self.scope["url_route"]["kwargs"]["pk"]
        self.room_group_name = f"chat_{self.room_name}"
        user = self.scope['user']

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()
        self.update_online_status(user, "online")    

    def disconnect(self, close_code):
        user = self.scope['user']
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )
        self.update_online_status(user, "offline")       


    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        self.message = text_data_json["message"]
        self.user = self.scope['user']
        PM = PVMessage(conv=get_object_or_404(PvChat, id=self.room_name), sender=self.user, content=self.message)
        PM.save()
        print(self.message)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, 
            {"type": "chat.message", "type_of_message":"new_message", "message": self.message, "sender":str(self.user), 'sender_id':str(self.user.id)}
        )
    

    def chat_message(self, event):
        self.send(text_data=json.dumps(event))

    
    def update_online_status(self, user, status):
        return ConnectionHistory.objects.filter(user=user,).update(status=status)






class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["pk"]
        self.room_group_name = f"chat_{self.room_name}"
        
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user = self.scope['user']
        M = Message(conv=get_object_or_404(Conversation,id=int(self.scope['url_route']['kwargs']['pk'])) , sender=user, content=message)
        M.save()
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat.message", "message": message, "sender":str(user)}
        )

    # Receive message from room group
    def chat_message(self, the_data_that_will_come_from_the_layer):
        message = the_data_that_will_come_from_the_layer["message"]
        user = the_data_that_will_come_from_the_layer['sender']
        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message, "sender":str(user)}))