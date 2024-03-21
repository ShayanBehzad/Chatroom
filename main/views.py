from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    conversations = Conversation.objects.all()
    print(request.user)
    return render(request, 'home.html', {'conv':conversations})

@login_required
def chatroom(request, pk=None):
    conversation = get_object_or_404(Conversation, id=pk)
    messages = Message.objects.filter(conv=pk)
    print(request)
    return render(request, 'chatroom.html', {'conv':conversation, 'messages':messages})

@login_required
def join_chat(request, g_pk):
    user_id = request.user.id
    conv = get_object_or_404(Conversation, id=g_pk)
    conv.users.add(user_id)
    return redirect('/%s' %g_pk)

def leave_chat(request, g_pk):
    user_id = request.user.id
    conv = get_object_or_404(Conversation, id=g_pk)
    conv.users.remove(user_id)
    return redirect('/')

# 'implementing Http section'