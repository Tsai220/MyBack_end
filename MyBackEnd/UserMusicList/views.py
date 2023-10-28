from .models import List, MusicDB, MusicList
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from usrInfo.models import UserInfo
from django.utils.html import escape
from rest_framework_simplejwt.exceptions import TokenError


# Create your views here.
class MyMusicList(APIView):

    def post(self, request):

        try:
            decode = RefreshToken(request.data.get('rToken'))
            Response(status=status.HTTP_403_FORBIDDEN)
        except Exception as err:
            return Response(str(err), status.HTTP_403_FORBIDDEN)
        else:

            userId = decode.payload.get('id')
            Getlist = List.objects.filter(user_id=userId)
            # null?
            # 無列表時可以返回JSON，但有表時會因JSON解析錯誤
            if Getlist.exists():
                # 開啟加入歌曲加入列表功能
                print("該使用者有音樂列表")
                return Response(Getlist.values(), status=status.HTTP_200_OK)

            else:
                # 開啟新增表流程
                print("該使用者無任何音樂列表")
                return Response({"Resources are not available"}, status=status.HTTP_200_OK)


class CreateList(APIView):
    def post(self, request):
        data = request.data
        title = escape(data.get('listTitle'))

        try:

            decode = RefreshToken(request.data.get('rToken'))
            userId = decode.payload.get('id')
            user_instance = UserInfo.objects.get(user_id=userId)
            user_list_count = List.objects.filter(user_id=userId).count()
            if user_list_count < 3:

                List(list_name=title, user_id=user_instance, listThumbnails=None).save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except TokenError as err:
            print(f"Token error: {err}")
            return Response({'Err': str(err)}, status=status.HTTP_401_UNAUTHORIZED)


# 將Search頁面按下收藏呼叫此post 並收藏 先判定是否有音樂列表 若有新增此歌 若無先創造新列表
class ShowPlayerList(APIView):
    def post(self, request):

        try:
            decode = RefreshToken(request.data.get('rToken'))
            Response(status=status.HTTP_403_FORBIDDEN)
        except Exception as err:
            return Response(str(err), status.HTTP_403_FORBIDDEN)
        else:
            userId = decode.payload.get('id')

            GetUserVal = List.objects.filter(user_id=userId).values()
            print(GetUserVal)
            return Response(GetUserVal, status=status.HTTP_200_OK)


class AddtoList(APIView):
    def post(self, request):
        data = request.data
        getSelectedListId = data.get('selectedListId')
        getVideoId = data.get('videoId')
        getVideoChannelId = data.get('videoChannelId')

        getVideoTitle = data.get('VideoTitle')
        getVideoThumbnail = data.get('VideoThumbnails')
        getChannelTitle = data.get('ChannelTitle')

        get_or_create = MusicDB.objects.get_or_create(videoId=getVideoId, channel_id=getVideoChannelId,
                                                      channel_name=getChannelTitle, videoThumbnails=getVideoThumbnail,
                                                      videoTitle=getVideoTitle)
        musicGet0 = MusicDB.objects.get(videoId=getVideoId).video_id
        listg0 = List.objects.get(list_id=getSelectedListId)

        GetRelationMapExists = MusicList.objects.filter(list_id=listg0.list_id, video_id=musicGet0).exists()
        print(GetRelationMapExists)
        if GetRelationMapExists:
            # 若有 返回"以新增過"
            print("存在")
            return Response(status=status.HTTP_200_OK)
        else:
            # 若無 連接關係
            relation = listg0.inListMusic.add(musicGet0)
            print("不存在")

            # 檢查這首歌是否已在列表中  先檢查中介表 用戶的音樂表裡是否這首歌 -> 若無 連接關係，若有 返回"以新增過"

            return Response(status=status.HTTP_200_OK)


class ShowList(APIView):
    def post(self, request):
        data = request.data
        print(data,"...")
        try:

            decode = RefreshToken(request.data.get('rToken'))
            Response(status=status.HTTP_403_FORBIDDEN)
        except Exception as err:
            return Response(str(err), status.HTTP_403_FORBIDDEN)
        else:
            userId = decode.payload.get('id')
            lists = List.objects.filter(user_id=userId).values()
            listBox = []
            for obj in lists:
                element = {
                    "listId": obj['list_id'],
                    "listName": obj['list_name'],
                    "listThumb": obj['listThumbnails'],
                }
                listBox.append(element)

            return Response(listBox, status=status.HTTP_200_OK)


class SongInList(APIView):
    def post(self, request):

        data = request.data
        GlistId = data.get('listId')

        GsongCount = MusicList.objects.filter(list_id=GlistId).values("video_id")
        print(GsongCount)
        videoIdList = []
        videoInfo = []
        for iid in GsongCount:
            videoIdList.append(iid['video_id'])
            print(videoIdList)
        for music in videoIdList:
            GetvideoInfo = MusicDB.objects.get(video_id=music)
            obj = {
                "videoId": GetvideoInfo.videoId,
                "videoThumbnails": GetvideoInfo.videoThumbnails,
                "videoTitle": GetvideoInfo.videoTitle,
                "channel_id": GetvideoInfo.channel_id,
                "channel_name": GetvideoInfo.channel_name

            }
            videoInfo.append(obj)
        print(videoInfo)

        return Response(videoInfo, status=status.HTTP_200_OK)

class DeleteThis(APIView):
    def post(self,request):
        # list_id  AND  video_id 需符合刪除目標
        data=request.data
        try:

            decode = RefreshToken(request.data.get('rToken'))
            Response(status=status.HTTP_403_FORBIDDEN)
        except Exception as err:
            return Response(str(err), status.HTTP_403_FORBIDDEN)
        else:

            userId = decode.payload.get('id')
            thisList= escape(data.get('thisList'))
            thisSongId=escape(data.get('video_id'))
            getThisMusicId=MusicDB.objects.filter(videoId=thisSongId).values("video_id")
            MusicList.objects.filter(list_id_id__in=thisList,video_id_id__in=getThisMusicId).delete()
            return Response(status.HTTP_200_OK)
