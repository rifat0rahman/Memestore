# Generated by Django 3.1.3 on 2021-04-24 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Timeline', '0024_auto_20210425_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.ManyToManyField(related_name='content', to='Timeline.Postfiles'),
        ),
    ]
