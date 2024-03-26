import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print('yessss')
        self.accept()

    def disconnect(self, close_code):
        print('noooooo') 
        

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        self.user = self.scope['user']
        print(self.user)
# shall give rhe self.user to it
        self.send(text_data=json.dumps({ "message": message}))