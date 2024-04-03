from django import forms
from .models import *

class ChannelForm(forms.ModelForm):
    class Meta:
        model = Conversation
        fields = ['title']