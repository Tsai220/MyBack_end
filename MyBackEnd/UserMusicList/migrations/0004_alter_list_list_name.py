# Generated by Django 4.2.5 on 2023-10-14 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserMusicList', '0003_alter_musiclist_video_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='list_name',
            field=models.CharField(max_length=15, null=True),
        ),
    ]