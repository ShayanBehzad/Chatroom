# Generated by Django 5.0.3 on 2024-04-04 16:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("register", "0005_user_pv_chat"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="pv_chat",
        ),
    ]
