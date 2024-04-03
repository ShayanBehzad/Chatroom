from django.urls import path
from .views import *
urlpatterns = [
    path("", home, name='home'),
    path("j/<int:g_pk>", join_chat, name='join'),
    path("l/<int:g_pk>", leave_chat, name='leave'),
    path("chatform/", create_chat, name='chatform'),
    path("<int:pk>", chatroom, name='conversation_room'),
]
