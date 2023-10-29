from django.urls import  path
from . import views
urlpatterns=[
    path("daily",views.Daily.as_view(),name='daily'),


]