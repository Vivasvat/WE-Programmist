from django.db import models
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
import uuid

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Телефон")
    # birth_date = models.DateField(null=True, blank=True)

class OneTimeLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True,)
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return str(self.token)