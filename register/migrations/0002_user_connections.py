# Generated by Django 5.0.3 on 2024-04-02 09:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("register", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="connections",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
