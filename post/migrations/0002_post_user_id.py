# Generated by Django 3.2.8 on 2023-06-25 21:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]