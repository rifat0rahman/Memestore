# Generated by Django 3.1.3 on 2021-04-05 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Timeline', '0009_auto_20210405_1911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='post_id',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.ManyToManyField(related_name='content', to='Timeline.Postfiles'),
        ),
    ]
