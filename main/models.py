from django.db import models
from register.models import User
from django.urls import reverse
from datetime import datetime



class Conversation(models.Model):
    title = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("conversation_room", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title
    

class PvChat(models.Model):
    first_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pv_first')
    second_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pv_second')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["first_user", "second_user"]
    
    def users_list(self):
        lis = []
        lis.append(self.first_user)
        lis.append(self.second_user)
        return lis

    def __str__(self):
        return f'{self.first_user} and {self.second_user}'

class Message(models.Model):
    conv = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class PVMessage(models.Model):
    conv = models.ForeignKey(PvChat, on_delete=models.CASCADE, related_name='pv')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pv_sender')
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def formatted_time(self):
        # Format the time as HH:MM in 24-hour format
        return self.created_at.strftime("%H:%M")

