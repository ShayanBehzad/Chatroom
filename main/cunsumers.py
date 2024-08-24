import json
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from django.shortcuts import get_object_or_404
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async
from datetime import datetime
import time
from main.models import *
from register.models import *



class PvChatCunsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["pk"]
        self.room_group_name = f"chat_{self.room_name}"
        self.user = self.scope['user']
        self.status = 'online'
        print('connected')
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name, 
            self.channel_name
        )
    
        await self.accept()
        await self.update_online_status(self.user, "online")    

    async def disconnect(self, close_code):
        user = self.scope['user']
        self.status = 'offline'
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )
        await self.update_online_status(user, "offline")       


    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        self.message = text_data_json["message"]
        chat = await sync_to_async(get_object_or_404)(PvChat, id=self.room_name)
        PM = PVMessage(conv=chat, sender=self.user, content=self.message)
        await sync_to_async(PM.save)()
        # date = str(datetime.datetime.now())
        # print(date)
        # ttime = date.split()[1]
        # ptime = ttime.split(':')[:2]
        # kir = ':'.join(ptime)
        now = datetime.now()
        kir2 = now.strftime('%H:%M')
        print(type(self.message))
        print('received')
        await self.channel_layer.group_send(
            self.room_group_name, 
            {"type": "chat.message", "type_of_message":"new_message", "message": self.message,"time":kir2, "sender":str(self.user), 'sender_id':str(self.user.id)}
        )

    async def chat_message(self, event):
        print('sent')
        await self.send(text_data=json.dumps(event))

    
    async def send_onlineStatus(self, event):
        username = self.user.username
        online_status = self.status
        await self.send(text_data=json.dumps({
            'type':'online-status',
            'username':username,
            'online_status':online_status
        }))


    @database_sync_to_async
    def update_online_status(self, user, status):
        ConnectionHistory.objects.filter(user=user,).update(status=status)
    





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
