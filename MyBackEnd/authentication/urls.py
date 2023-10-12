from django.urls import  path
from . import views
urlpatterns=[
    path("api/auth",views.verify.as_view(),name="Token")
]