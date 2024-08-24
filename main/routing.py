from django.urls import re_path
from .cunsumers import *

websocket_urlpatterns = [
     re_path(r"ws/(?P<pk>\d+)/$", ChatConsumer.as_asgi()), 
     re_path(r"ws/pv_room/(?P<pk>\d+)/$", PvChatCunsumer.as_asgi()), 
     
]


     # re_path(r"ws/(?P<pk>\w+)/$", ChatConsumer.as_asgi()),
     # re_path(r"ws/([1-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9])", ChatConsumer.as_asgi()),
