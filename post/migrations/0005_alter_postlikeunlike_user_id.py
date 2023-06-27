# Generated by Django 3.2.8 on 2023-06-25 22:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0004_alter_postlikeunlike_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postlikeunlike',
            name='user_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_like_unlike', to=settings.AUTH_USER_MODEL),
        ),
    ]
