# Generated by Django 3.1.3 on 2021-04-25 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Timeline', '0041_auto_20210426_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.ManyToManyField(related_name='content', to='Timeline.Postfiles'),
        ),
    ]
