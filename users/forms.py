from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User

from django.contrib.auth.hashers import make_password

class UserLoginForm(AuthenticationForm):

    username = forms.CharField()
    password = forms.CharField()
    
    class Meta:
        model=User
        fields = ['username', 'password']

class UserRegistrationForm(UserCreationForm):
    
    username = forms.CharField(
        max_length=15,
        # help_text='Используйте',
        label='Имя пользователя'
        )

    email = forms.EmailField(
        max_length=25,
        help_text='example@mail.ru' , label='Введите вашу электронную почту'
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
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')

class ContactForm(forms.Form):
    from_email = forms.EmailField(
        label='Email', 
        required=True
        )

class UserPasswordResent(forms.Form):
    new_password1 = forms.CharField(
        label='Повторите пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        # help_text='Одна большая буква и т.д.',
        )
    new_password2 = forms.CharField(
        label='Повторите пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        # help_text='Одна большая буква и т.д.',
        )
        
    def check_passwords(self):
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')
        if new_password1 != new_password2:
            raise forms.ValidationError("Пароли не совпадают!")

    class Meta:
        # model = User
        fields = ('new_password1', 'new_password2')
