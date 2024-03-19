from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.urls import reverse


class Conversation(models.Model):
    name = models.CharField(max_length=50)
    user = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse("conversation_room", kwargs={"pk": self.pk})
    

class Message(models.Model):
    conv = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

