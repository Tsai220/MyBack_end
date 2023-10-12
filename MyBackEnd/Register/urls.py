from django.urls import  path
from . import views
urlpatterns=[
    path("api/Register",views.RegisterAPI.as_view(),name="Register")
]