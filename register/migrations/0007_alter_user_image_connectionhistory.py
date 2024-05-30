# Generated by Django 5.0.3 on 2024-05-30 14:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("register", "0006_remove_user_pv_chat"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="image",
            field=models.ImageField(blank=True, upload_to="profiles/"),
        ),
        migrations.CreateModel(
            name="ConnectionHistory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("online", "On-line"), ("offline", "Off-line")],
                        default="online",
                        max_length=10,
                    ),
                ),
                ("first_login", models.DateTimeField(auto_now_add=True)),
                ("last_echo", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
