# Generated by Django 4.2.5 on 2023-10-08 08:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usrInfo', '0007_alter_userinfo_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('list_id', models.AutoField(primary_key=True, serialize=False)),
                ('list_name', models.CharField(max_length=10, null=True)),
                ('listThumbnails', models.URLField(max_length=254, null=True, validators=[django.core.validators.URLValidator()])),
            ],
        ),
        migrations.CreateModel(
            name='MusicDB',
            fields=[
                ('video_id', models.AutoField(primary_key=True, serialize=False)),
                ('channel_id', models.CharField(max_length=75, null=True)),
                ('channel_name', models.CharField(max_length=50, null=True)),
                ('videoThumbnails', models.URLField(max_length=254, validators=[django.core.validators.URLValidator()])),
                ('videoTitle', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MusicList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_Views', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('list_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserMusicList.list')),
                ('video_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserMusicList.musicdb')),
            ],
        ),
        migrations.AddField(
            model_name='list',
            name='inListMusic',
            field=models.ManyToManyField(through='UserMusicList.MusicList', to='UserMusicList.musicdb'),
        ),
        migrations.AddField(
            model_name='list',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usrInfo.userinfo', to_field='user_id'),
        ),
    ]
