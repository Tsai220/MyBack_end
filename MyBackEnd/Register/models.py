from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator, MinLengthValidator


# Create your models here.
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.EmailField(max_length=254, validators=[EmailValidator()], unique=True)
    email = models.EmailField(max_length=254, validators=[EmailValidator()])
    password = models.CharField(max_length=200, validators=[MinLengthValidator(4)])
    nickName = models.CharField(max_length=10, validators=[MinLengthValidator(4)])
    birthday = models.DateField(help_text="YYYY-MM-DD")
    gender = models.CharField(max_length=7, validators=[MinLengthValidator(3)])
