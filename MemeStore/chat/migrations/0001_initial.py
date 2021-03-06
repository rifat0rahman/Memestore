# Generated by Django 3.1.3 on 2021-04-26 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Directors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('directors', models.CharField(max_length=100)),
                ('creator1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creatorone', to=settings.AUTH_USER_MODEL)),
                ('creator2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creatortwo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(default='dm')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_seen', models.BooleanField(default=False)),
                ('chat_url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.directors')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='direct_seceiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='direct_sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
