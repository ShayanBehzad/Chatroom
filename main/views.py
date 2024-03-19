from django.shortcuts import get_object_or_404, render
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    conversations = Conversation.objects.all()
    return render(request, 'home.html', {'conv':conversations})

@login_required
def chatroom(request, pk=None):
    conversation = get_object_or_404(Conversation, id=pk)
    messages = Message.objects.filter(conv=pk)
    print(request)
    return render(request, 'chatroom.html', {'conv':conversation, 'messages':messages})



# 'implementing Http section'