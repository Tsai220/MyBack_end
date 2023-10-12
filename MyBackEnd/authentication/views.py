from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework.views import APIView
from rest_framework.response import Response
from usrInfo.models import UserInfo
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
# Create your views here.

class verify(TokenVerifyView):
    def post(self,request,*args,**kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code==200:
            UsrToken=RefreshToken(request.data.get('rToken'))
            userId=UsrToken.payload.get('id')

            GetId=UserInfo.objects.filter(user_id=userId).values().first()
            nickName=GetId['nickName']
            print(GetId['nickName'])
            return Response(nickName,status=status.HTTP_200_OK)

