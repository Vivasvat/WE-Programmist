from django.contrib import auth
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.http import HttpResponseRedirect

from acc.models import MyAccount

from acc.forms import ProfileForm

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user) # files=request.FILES
        if form.is_valid():
            # user = form.save()
            return HttpResponseRedirect(reverse('acc:profile'))
    else:
        form = ProfileForm(instance=request.user)
    context = {
        'title': 'Home - Кабинет',
        'form': form
    }
    return render(request, 'acc/account.html', context) 

@login_required
def edit_profile(request, username):
    try:
        pro=MyAccount.objects.get(username=username)
        if request.method=="POST":
            pro.name=request.POST.get("name")
            pro.name_two=request.POST.get("name_two")
            pro.save()
            return HttpResponseRedirect("/main/")
        else:
            return render(request, "main/next.html", {"pro" : pro})

    except pro.DoesNotExist:
        return HttpResponseRedirect("<h2>Not found page :(</h2>")
    

@login_required
def profile_delete_view(request):
    user = request.user
    if request.method == "POST":
        auth.logout(request)
        user.delete()
        messages.success(request, 'Account deleted, what a pity')
        return redirect('/')
    
    return render(request, 'acc/account.html')