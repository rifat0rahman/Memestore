# Generated by Django 3.1.3 on 2021-04-26 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Timeline', '0044_auto_20210427_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.ManyToManyField(related_name='content', to='Timeline.Postfiles'),
        ),
    ]
