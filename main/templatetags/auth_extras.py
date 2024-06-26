from django import template
from main.models import *
from django.db.models import Q


register = template.Library()

@register.filter(name='has_group')
def has_group(user, g_pk): 
    group = Conversation.objects.get(id=g_pk) 
    group_users = group.users.all()
    
    if user in group_users:
        return True
    else:
        return False

@register.filter(name='is_contact')
def is_contact(user, self):
    connections = User.objects.get(username=self).connections
    # print(connections.all())
    if user in connections.all():
        return True
    else:
        return False


@register.filter(name='pv_chat')
def pv_chat(user, self):
    try:
       chat = PvChat.objects.get((Q(first_user=self )| Q(second_user=self)) & (Q(first_user=user) | Q(second_user=user)))
    except:
            chat = PvChat.objects.create(
                first_user = user,
                second_user = self   
            )
            chat.save()

    return chat.id


@register.filter(name='first_sent')
def first_sent(mes, first_user):
    if mes.sender == first_user:
        return True
    else:
        return False
    
@register.filter(name='is_user')
def is_user(user, self):
    if user == self:
        return True
    else:
        return False