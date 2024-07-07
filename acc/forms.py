from django import forms
from django.contrib.auth.forms import UserChangeForm
from users.models import User
from acc.models import Profile
# from django.contrib.auth import models

class ProfileForm(UserChangeForm):

    image  = forms.ImageField( required=False)
    username = forms.CharField()
    
    class Meta:
        model = User
        fields = (
            'image',
            'username',
            )