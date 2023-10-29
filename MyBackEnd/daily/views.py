from django.shortcuts import render
from rest_framework.views import APIView
from UserMusicList.models import MusicList, List,MusicDB
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
import numpy as np


# Create your views here.

class Daily(APIView):
    def post(self, request):

        try:
            decode = RefreshToken(request.data.get('rToken'))
            Response(status=status.HTTP_403_FORBIDDEN)
        except Exception as err:

            return Response(str(err), status=status.HTTP_403_FORBIDDEN)
        else:
            userId = decode.payload.get('id')
            Getlist = List.objects.filter(user_id=userId)
            randomSong= np.array([])
            ShowDaily = np.array([])
            if Getlist.exists():

                for index, listCount in enumerate(Getlist.values()):
                    ShowDaily = np.append(ShowDaily,Getlist.get(list_id=listCount['list_id']).inListMusic.all().values())
                if len(ShowDaily)==1:
                    randomSong=np.append(randomSong,np.random.choice(ShowDaily,size=1 ))
                else:
                    randomSong = np.append(randomSong, np.random.choice(ShowDaily, size=4, replace=False))
                return Response(randomSong, status.HTTP_200_OK)
            else:
                ShowDaily = np.append(ShowDaily, MusicDB.objects.all().values())
                randomSong=np.append(randomSong,np.random.choice(ShowDaily,size=4,replace=False))

                return Response(randomSong,status=status.HTTP_200_OK)
