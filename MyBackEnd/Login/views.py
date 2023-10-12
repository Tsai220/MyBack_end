

from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import generics,permissions,status
from rest_framework.response import Response
from usrInfo.models import UserInfo
from django.contrib import auth
# Create your views here.
class LoginAPI(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        if request.method=='POST':
            data = request.data
            email = data.get('email')
            password = data.get('password')
            user= authenticate( username=email, password=password)
            print(email," ",password )
            if user:

                login(request,user)
                #token = Token.objects.create(user=user)
                refresh=RefreshToken.for_user(user)
                refresh['id']=user.id


                username=UserInfo.objects.get(user_id=user.id).nickName
                print(username)
                Tokendata = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'username': username ,

                }
                print(email + "登入成功。 Token:"+Tokendata['refresh']," and "+ Tokendata['access'])
                return Response(Tokendata, status=status.HTTP_200_OK)



            else:
                print(email+"登入失败")
                return Response({"fail"},status=status.HTTP_401_UNAUTHORIZED)

