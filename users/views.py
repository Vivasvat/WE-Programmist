from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
# from social_django.utils import load_social_backends
from django.conf import settings
from django.core import mail

from users.forms import UserLoginForm, UserRegistrationForm, ContactForm
# ProfileForm, UserLoginForm, 

# from users.models import Profile

# from acc.models import MyAccount

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect("/acc/")
                # return render(request, 'acc/account.html')
                # return HttpResponseRedirect(reverse('main:main'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'Home - Авторизация',
        'form': form,
        }
    return render(request, 'users/login.html', context) 

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # messages.success(self.request, 'Регистрация прошла успешно')
            # сохранение номера
            # MyAccount.objects.create(user=user, phone_number=form.cleaned_data.get('phone_number'))
            raw_password = form.cleaned_data.get('password1')
            user = auth.authenticate(username=user.username, password=raw_password)
            auth.login(request, user)
            return redirect('/acc/')

        else:
            return render(request, 'users/registration.html', {'form': form})
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))

def contact_view(request):
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
            # subject = form.cleaned_data['subject']
            subject = 'Welcome!'
            to_email = form.cleaned_data['from_email']
            message = "12345"
            
            # `message = form.cleaned_data['message']
            try:
                send_mail( subject, message, settings.EMAIL_HOST_USER, [to_email])
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('/success/')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, "users/email.html", {'form': form})

def success_view(request):
    return HttpResponse('Приняли! Спасибо за вашу заявку.')