from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.

def home(request):
    conversations = Conversation.objects.all()
    return render(request, 'home.html', {'conv':conversations})

@login_required
def chatroom(request, pk=None):
    conversation = get_object_or_404(Conversation, id=pk)
    messages = Message.objects.filter(conv=pk)
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
            con = Conversation.objects.create(
                title = form.cleaned_data['title'],
                owner = request.user,
            )
            con.users.add(request.user)
            con.save()
            return redirect('/%s'%con.id)
            
    return render(request, 'chatform.html', {'form':form})


@login_required
def pv_chat(request, pk):
    conversation = get_object_or_404(PvChat, id=pk)
    messages = PVMessage.objects.filter(conv=pk)
    count = messages.count()
    if conversation.first_user == request.user:
        second_user = conversation.second_user
    else:
        second_user = conversation.first_user
    contacts = request.user.connections.all()
    
    return render(request, 'chatroom/pv.html', {'contacts':contacts, 'conv':conversation,'first_user':request.user, 'second_user':second_user, 'messages':messages, 'count':count})




# 'implementing Http section'
# git push -f -u origin main 

# wsl
# sudo service redis-server start