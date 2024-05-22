# Generated by Django 4.1.3 on 2024-05-19 18:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_property_location_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='host', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
