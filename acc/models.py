from django.db import models
from django.contrib.auth.models import User

class MyAccount(models.Model):
    
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    # desc=models.TextField(null=True, blank=True)

    avatar = models.ImageField(null=True, blank=True, upload_to="images/profile/")

    name = models.CharField(max_length=15, null=True, blank=True)
    surname = models.CharField(max_length=15, null=True, blank=True)
    lastname = models.CharField(max_length=15, null=True, blank=True )

    email = models.CharField(max_length=25, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    google = models.CharField(max_length=50, null=True, blank=True)
    yandex = models.CharField(max_length=50, null=True, blank=True)
    github = models.CharField(max_length=50, null=True, blank=True)

def __str__(self):
    return str(self.user)

