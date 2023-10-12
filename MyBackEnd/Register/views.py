from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from django.utils.html import escape
from django.contrib.auth.hashers import make_password
from usrInfo.models import UserInfo
# Create your views here.


class RegisterAPI(APIView):
    def post(self, request):  # post方法
        data = request.data
        IsRegiseter = request.data.get("email")
        try:
            CheckRegistered = User.objects.get(email=IsRegiseter)
            return Response({"already registered"} ,status=status.HTTP_409_CONFLICT)
        except User.DoesNotExist:
            email = escape(data.get('email'))
            password = make_password(data.get('password'))
            nickName = escape(data.get('user'))
            birthday = escape(data.get('birthday'))
            gender = escape(data.get('gender'))
            usr = User.objects.create(username=email, email=email,password=password, nickName=nickName, birthday=birthday,
                                      gender=gender)
            usrInfo = UserInfo.objects.create(user_id=usr, email=email, nickName=nickName, member=1)
            return Response({"註冊完成"}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'Err': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
