# Generated by Django 3.2.8 on 2023-06-25 22:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0002_post_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostLikeUnlike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction', models.BooleanField(default=False)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_like_unlike', to='post.post')),
                ('user_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_like_unlike', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]