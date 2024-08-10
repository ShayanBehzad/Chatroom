from Chatroom import settings
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.core.validators import MinValueValidator, RegexValidator
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class UserRoleMixin(models.Model):
    phone_regex = RegexValidator(
        regex=r'^(0|0098|\+98)9(0[1-5]|[1 3]\d|2[0-2]|98)\d{7}$',
        message="Phone number must be entered in the format: '+989031234567'."
    )
    connections = models.ManyToManyField('self', blank=True)
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, default='')
    image = models.ImageField(upload_to='profiles/', blank=True)
    bio = models.CharField(max_length=150, blank=True)
    
    def get_absolute_url(self):
        return reverse("profileview", kwargs={"username": self.username})
    
    class Meta:
        abstract = True

class User(UserRoleMixin, AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to.'),
        related_name='custom_user_set', 
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='custom_user_set', 
        related_query_name='custom_user',
    )



class ConnectionHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    STATUS = (
        ("online", "On-line"),
        ("offline", "Off-line")
    )
    status = models.CharField(max_length=10, choices=STATUS, default="online")
    first_login = models.DateTimeField(auto_now_add=True)
    last_echo = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Connection History"
        verbose_name_plural = "Connections History"  

    def __str__(self):
        return f"{self.user} connection status"