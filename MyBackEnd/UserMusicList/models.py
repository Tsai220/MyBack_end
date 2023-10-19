from django.db import models
from usrInfo.models import UserInfo
from django.core.validators import URLValidator, MinValueValidator


# Create your models here.
class MusicDB(models.Model):  # 音樂庫
    video_id = models.AutoField(primary_key=True)  # video_id
    videoId = models.CharField(max_length=50, null=True)
    channel_id = models.CharField(max_length=75, null=True)
    channel_name = models.CharField(max_length=50, null=True)
    videoThumbnails = models.URLField(max_length=254, validators=[URLValidator()])
    videoTitle = models.CharField(max_length=100, null=True)


class List(models.Model):
    inListMusic = models.ManyToManyField(MusicDB, through="MusicList")
    list_id = models.AutoField(primary_key=True)  # 沒自動生成?
    user_id = models.ForeignKey(UserInfo, to_field="user_id", on_delete=models.CASCADE)
    list_name = models.CharField(max_length=15, null=True)
    listThumbnails = models.URLField(max_length=254, null=True, validators=[URLValidator()])


class Singer(models.Model):
    inSingerList = models.ManyToManyField(MusicDB, through="SingerList")
    id = models.AutoField(primary_key=True)
    channel_id = models.CharField(max_length=75, null=True)
    channel_name = models.CharField(max_length=50, null=True)
    channel_Thumb = models.URLField(max_length=254, null=True, validators=[URLValidator()])


class MusicList(models.Model):
    list_id = models.ForeignKey(List, on_delete=models.CASCADE)
    video_id = models.ForeignKey(MusicDB, on_delete=models.CASCADE)
    video_Views = models.IntegerField(validators=[MinValueValidator(0)], default=0)


class SingerList(models.Model):
    video_id = models.ForeignKey(MusicDB, on_delete=models.CASCADE)
    channel_id = models.ForeignKey(Singer, on_delete=models.CASCADE)
    Singer_Views = models.IntegerField(validators=[MinValueValidator(0)], default=0)
