# Generated by Django 5.0.3 on 2024-08-08 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_alter_user_image_connectionhistory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='connectionhistory',
            options={'verbose_name': 'Connection History', 'verbose_name_plural': 'Connections History'},
        ),
    ]
