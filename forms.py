"""
    Файл, для создания форм.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User

# AuthenticationForm
# forms.ModelForm

class UserLoginForm(AuthenticationForm):

    username = forms.CharField()
    password = forms.CharField()

    #
    username = forms.CharField(
        label = 'Имя', 
        widget=forms.TextInput(attrs={"autofocus": True,
                                      'class': 'form-control',
                                      'placeholder': 'Введите ваше имя пользователя'})
    )
    password = forms.CharField(
        label = 'Пароль', 
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                          'class': 'form-control',
                                          'placeholder': 'Введите ваш пароль'})
    )
    #
    class Meta:
        model=User
        fields = ['username', 'password']


class UserRegustrationForm(UserCreationForm):
    class Meta:
        model=User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        )

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

class ProfileForm(UserChangeForm):
    class Meta:
        model=User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
        )

    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()

    #
    image=forms.ImageField(
        widget=forms.FileInput(attrs={"class": "form-control mt-3"}), required=False
    )

    first_name=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваше имя",
            }
        )
    )

    last_name=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите вашу фамилию",
            }
        )
    )
    #