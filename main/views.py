import re
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
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

@login_required
def create_chat(request):
    form = ChannelForm
    if request.method == 'POST':
        form = ChannelForm(request.POST)
        if form.is_valid():
            # form.data["owner"] = request.user
            # print(form.data)
            con = Conversation.objects.create(
                title = form.cleaned_data['title'],
                owner = request.user,
            )
            con.users.add(request.user)
            con.save()
            return redirect('/%s'%con.id)
            
    return render(request, 'chatform.html', {'form':form})




# 'implementing Http section'
# git push -f -u origin main 

# wsl
# sudo service redis-server start