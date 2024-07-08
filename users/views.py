from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

from users.forms import UserLoginForm, UserRegistrationForm, ContactForm, UserPasswordResent
from users.models import User, OneTimeLink
from users.utils import generate_one_time_link
from django.contrib.auth.hashers import make_password

email_current = ""

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect("/tournaments/")
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
            return redirect('/tournaments/')

        else:
            return render(request, 'users/registration.html', {'form': form})
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))

def contact_view(request):
    global email_current
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
            to_email = form.cleaned_data['from_email']
            try:
                user = User.objects.get(email=to_email)
                email_current = to_email
            except Exception:
                user = False
                # return HttpResponse(f'Не существует пользователя с такой почтой: {to_email}')
                context = f'Не существует пользователя с такой почтой: {to_email}'
                return render(request, "users/errors.html", { 'context' : context })
            if user:
                link = generate_one_time_link(user)
                full_link = request.build_absolute_uri(link)

                subject = 'Welcome!'
                message = f'Here is your one-time link: {full_link}'
                send_mail(subject, message, settings.EMAIL_HOST_USER, [to_email])

                return redirect('/success/')
    else:
        # return HttpResponse('Неверный запрос.')
        context = 'Неверный запрос'
        return render(request, "users/errors.html", { 'context' : context })
    return render(request, "users/email.html", {'form': form})

def success_view(request):
    # return HttpResponse(f'Приняли! Спасибо за вашу заявку: {email_current}')
    context = f'Приняли! Спасибо за вашу заявку: {email_current}'
    return render(request, "users/errors.html", { 'context' : context })

def use_one_time_link(request, token):
    one_time_link = get_object_or_404(OneTimeLink, token=token)

    if one_time_link.is_used:
        context = f'Ваша ссылка, отрпвленная на почту: {email_current} уже использована'
        return render(request, "users/errors.html", { 'context' : context })
        # return HttpResponseForbidden("This link has already been used.")

    one_time_link.is_used = True
    one_time_link.save()

    return redirect(reverse('users:password_reset_confirm'))
    # Дополнительная проверка срока действия токена
    # if timezone.now() > one_time_link.created_at + timedelta(hours=1):
    #     return HttpResponseForbidden("This link has expired.")

    # Выполните нужное действие, например, перенаправление на защищенную страницу
    
def password_reset_confirm(request):
    if request.method == "POST":
        form = UserPasswordResent(request.POST)
        if form.is_valid():
            # email = OneTimeLink.objects.get(request.user.id)
            user = User.objects.get(email=email_current)
            password_old = user.password
            password_new = form.cleaned_data['new_password1']
            password_new = make_password(password_new)
            if password_old==password_new:
                return redirect(reverse('users:password_reset_confirm'))
            else:
                user.password = password_new
                user.save(update_fields=["password"])
                return redirect('users:compete')
        else:
            return render(request, 'users/password_reset_confirm.html', {'form' : form})
    else:
        form = UserPasswordResent()
        return render(request, 'users/password_reset_confirm.html', {'form' : form})
    
def complete_reset_password(request):
    return render(request, 'users/password_reset_complete.html')