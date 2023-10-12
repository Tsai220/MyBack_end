from django.urls import  path
from . import views
urlpatterns=[
    path("list",views.MyMusicList.as_view(),name='list'),
    path("listCr",views.CreateList.as_view(),name='listCr'),
    path('listShow',views.ShowPlayerList.as_view(),name='listShow'),
    path('listAdd',views.AddtoList.as_view(),name='listAdd'),
    path('ShowList',views.ShowList.as_view(),name='ShowList'),

]