from django.urls import path
from .views import *
urlpatterns = [
    path("", home, name='home'),
    path("<int:pk>", chatroom, name='conversation_room'),
]
