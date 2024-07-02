from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

from users.forms import UserLoginForm, UserRegistrationForm, ContactForm
from users.models import OneTimeLink
from users.utils import generate_one_time_link


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
            user = request.user
            link = generate_one_time_link(user)

            subject = 'Welcome!'
            to_email = form.cleaned_data['from_email']
            full_link = request.build_absolute_uri(link)
            message = f'Here is your one-time link: {full_link}'
            # `message = form.cleaned_data['message']
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [to_email])
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('/success/')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, "users/email.html", {'form': form})

def success_view(request):
    return HttpResponse('Приняли! Спасибо за вашу заявку.')

def use_one_time_link(request, token):
    one_time_link = get_object_or_404(OneTimeLink, token=token)

    if one_time_link.is_used:
        return HttpResponseForbidden("This link has already been used.")
    
    
    # Дополнительная проверка срока действия токена
    # if timezone.now() > one_time_link.created_at + timedelta(hours=1):
    #     return HttpResponseForbidden("This link has expired.")

    one_time_link.is_used = True
    one_time_link.save()

    # Выполните нужное действие, например, перенаправление на защищенную страницу
    return redirect('/password_reset_confirm/')