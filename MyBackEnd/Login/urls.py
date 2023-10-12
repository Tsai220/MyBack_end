from django.urls import  path
from . import views
urlpatterns=[
    path("api/Login",views.LoginAPI.as_view(),name="Login")
]