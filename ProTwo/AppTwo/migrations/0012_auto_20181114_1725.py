# Generated by Django 2.1.2 on 2018-11-15 01:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0011_auto_20181114_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal1',
            name='user',
            field=models.OneToOneField(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
