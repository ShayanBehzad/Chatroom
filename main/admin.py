from django.contrib import admin
from .models import *


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
     filter_horizontal = ('users',)


# Register your models here.
admin.site.unregister(Conversation)
admin.site.register(Conversation, ConversationAdmin)
admin.site.register(Message)