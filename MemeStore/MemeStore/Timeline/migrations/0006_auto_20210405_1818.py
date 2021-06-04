# Generated by Django 3.1.3 on 2021-04-05 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Timeline', '0005_auto_20210405_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.ManyToManyField(related_name='content', to='Timeline.Postfiles'),
        ),
        migrations.RemoveField(
            model_name='tag',
            name='post_id',
        ),
        migrations.AddField(
            model_name='tag',
            name='post_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Timeline.post'),
        ),
    ]
