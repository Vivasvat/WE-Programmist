from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class UserLoginForm(AuthenticationForm):

    username = forms.CharField()
    password = forms.CharField()

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
    class Meta:
        model=User
        fields = ['username', 'password']

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        max_length=15,
        # help_text='Используйте',
        label='Имя пользователя'
    )

    email = forms.CharField(
        max_length=25,
        help_text='example@mail.ru' , label='Введите вашу електронную почту'
    )

    phone_number = forms.CharField(
        max_length=15,
        help_text='Номер телефона. Формат +7910...', label='Phone'
    )
    password1 = forms.CharField(
        label='Введите пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text="Пароль должен быть длинной не менне 8 символов, содержать различные символы.",
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        # help_text='Одна большая буква и т.д.',
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2', )