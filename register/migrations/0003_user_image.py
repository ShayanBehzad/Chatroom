# Generated by Django 5.0.3 on 2024-04-03 07:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("register", "0002_user_connections"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="image",
            field=models.ImageField(blank=True, upload_to="media/profiles"),
        ),
    ]
