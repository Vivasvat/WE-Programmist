
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

# from social_django.utils import load_social_backends

from users.forms import UserLoginForm, UserRegistrationForm
# ProfileForm, UserLoginForm, 
from users.models import Profile

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return render(request, 'main/main.html')
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
            # сохранение номера
            Profile.objects.create(user=user, phone_number=form.cleaned_data.get('phone_number'))
            raw_password = form.cleaned_data.get('password1')
            user = auth.authenticate(username=user.username, password=raw_password)
            auth.login(request, user)
            return redirect('/main/')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index_auth'))

#Create your views here.

