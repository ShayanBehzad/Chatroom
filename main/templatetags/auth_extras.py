from django import template
from main.models import *


register = template.Library()

@register.filter(name='has_group')
def has_group(user, g_pk): 
    group = Conversation.objects.get(id=g_pk) 
    group_users = group.users.all()
    
    print(group_users)
    if user in group_users:
        return True
    else:
        return False