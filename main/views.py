
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .models import *
from .forms import *

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
        else:
            messages.error(request, "%s" %form.errors)
            
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
    
    return render(request, 'chatroom/pv.html', {'contacts':contacts,'self': request.user, 'conv':conversation,'first_user':request.user, 'second_user':second_user, 'messages':messages, 'count':count})


# get the list of contatcs
@login_required
def contacts(request, username):
    contacts = get_object_or_404(User, id=request.user.id).connections.all()
    return render(request, 'contacts/contacts.html', {'contacts': contacts})

@login_required
def add_contatcs(request):
    members = User.objects.exclude(username=request.user.username)
    context={'members': members, 'self': request.user}
    print(members)
    return render(request, 'contacts/members.html', context)


# 'implementing Http section'
# git push -f -u origin main 

# wsl
# sudo service redis-server start