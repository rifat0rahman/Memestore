# Generated by Django 3.1.3 on 2021-04-05 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Timeline', '0007_auto_20210405_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.ManyToManyField(related_name='content', to='Timeline.Postfiles'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
