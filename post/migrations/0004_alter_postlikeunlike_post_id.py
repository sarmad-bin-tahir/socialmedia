# Generated by Django 3.2.8 on 2023-06-25 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_postlikeunlike'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postlikeunlike',
            name='post_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='post_like_unlike', to='post.post'),
        ),
    ]