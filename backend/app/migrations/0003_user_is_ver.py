# Generated by Django 4.1.3 on 2024-05-18 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_feedback_verifymessage_contactmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_ver',
            field=models.BooleanField(default=False),
        ),
    ]
