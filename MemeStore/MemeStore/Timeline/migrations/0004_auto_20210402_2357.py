# Generated by Django 3.1.3 on 2021-04-02 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Timeline', '0003_auto_20210402_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.ManyToManyField(related_name='content', to='Timeline.Postfiles'),
        ),
        migrations.RemoveField(
            model_name='stream',
            name='post',
        ),
        migrations.AddField(
            model_name='stream',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Timeline.post'),
        ),
    ]
