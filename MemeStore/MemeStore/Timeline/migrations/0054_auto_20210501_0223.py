# Generated by Django 3.1.3 on 2021-04-30 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Timeline', '0053_auto_20210501_0222'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='liked',
            field=models.ManyToManyField(blank=True, null=True, related_name='likes', to='Timeline.Likes'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.ManyToManyField(related_name='content', to='Timeline.Postfiles'),
        ),
    ]
