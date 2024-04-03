from django.db import models
from register.models import User
from django.urls import reverse


class Conversation(models.Model):
    title = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("conversation_room", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title

class Message(models.Model):
    conv = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

