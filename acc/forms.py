from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
# from django.contrib.auth import models

class ProfileForm(UserChangeForm):

    avatar  = forms.ImageField(required=False)

    username = forms.CharField(
        max_length=15,
        # help_text='Используйте',
        label='Никнейм'
    )

    name = forms.CharField(
        max_length=15,
        # help_text='Используйте',
        label='Имя'
    )

    surname = forms.CharField(
        max_length=15,
        # help_text='Используйте',
        label='Фамилия'
    )

    lastname = forms.CharField(
        max_length=15,
        # help_text='Используйте',
        label='Отчество'
    )

    email = forms.CharField(
        max_length=25,
        #help_text='example@mail.ru' , 
        label='Ваша електронная почта'
    )

    phone_number = forms.CharField(
        max_length=15,
        #help_text='Номер телефона. Формат +7910...', 
        label='Ваш номер телефона'
    )

    google = forms.CharField(
        max_length=50, 
        label='Gmail',
        )
    yandex = forms.CharField(
        max_length=50, 
        label='Ymail',
        )
    github = forms.CharField(
        max_length=50, 
        label='Github',
        )

    class Meta:
        model = User
        fields = (
            'avatar',
            'username', 
            'name', 
            'surname',
            'lastname',
            'email',
            'phone_number',
            'google',
            'yandex',
            'github',
            )