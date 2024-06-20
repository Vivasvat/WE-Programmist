from django.db import models
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Телефон")
    # birth_date = models.DateField(null=True, blank=True)


# class Connetion_model(SocialAccount):
#     user = models.ForeignKey(to=User, on_delete = models.CASCADE,
#     )