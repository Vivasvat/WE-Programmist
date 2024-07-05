from django.db import models
from users.models import User
from allauth.socialaccount.models import SocialAccount

class Profile(models.Model):

    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    steam_id=models.OneToOneField(SocialAccount, null=True, on_delete=models.CASCADE)

    avatar = models.ImageField(null=True, blank=True)
    username = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return str(self.user)
