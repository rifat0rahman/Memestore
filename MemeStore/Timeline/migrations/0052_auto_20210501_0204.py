# Generated by Django 3.1.3 on 2021-04-30 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Timeline', '0051_auto_20210501_0202'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='liked',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='Timeline.likes'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.ManyToManyField(related_name='content', to='Timeline.Postfiles'),
        ),
    ]
