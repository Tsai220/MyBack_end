from django.db import models
from Register.models import User
from django.core.validators import EmailValidator, MinLengthValidator, MinValueValidator, MaxValueValidator


# Create your models here.
class UserInfo(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE,unique=True)
    email = models.EmailField(max_length=254, validators=[EmailValidator()])
    nickName = models.CharField(max_length=10, validators=[MinLengthValidator(4)])
    member = models.IntegerField(validators=[MinLengthValidator(1), MinValueValidator(3)])
    # user_id = models.ForeignKey(to_fields="user_id")