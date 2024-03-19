from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    conversations = Conversation.objects.all()
    return render(request, 'home.html', {'conv':conversations})


def chatroom(request, pk=None):
    messages = Message.objects.filter(conv=pk)
    if request.method == 'POST':
        Message.objects.create()

# 'implementing Http section'