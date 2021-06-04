# Generated by Django 3.1.3 on 2021-04-27 20:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_chat_directors'),
    ]

    operations = [
        migrations.AddField(
            model_name='directors',
            name='joined',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]