# Generated by Django 3.2.8 on 2023-06-25 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='geolocation',
            field=models.JSONField(),
        ),
    ]
