from django import template
from main.models import *


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