from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from main.models import Categories, Products

# def index(request):
# person=Person.objects.all()
# next_page_url=reverse("main:next_page")
# context={
# 'Login': 'Таблица',
# 'description': 'Список пользователей',
# 'person': person,
# 'next_page_url' : next_page_url,
# }
# return render(request, "main/main.html", context)

def index_auth(request):
    context={
        'None':None
    }
    return render(request, "index_auth.html", context)

def index(request):
    cate = Categories.objects.all()
    prod = Products.objects.all()
    context={
        'prod':prod,
        'cate':cate,
    }
    return render(request, "index.html", context)

def create(request):
    if request.method=="POST":
        cate=Categories()
        cate.name=request.POST.get("name")
        cate.name_two=request.POST.get("name_two")
        cate.save()
    #return render(request, "main/main.html")
    return HttpResponseRedirect('/')

def edit(request, id):
    try:
        cate=Categories.objects.get(id=id)
        if request.method=="POST":
            cate.name=request.POST.get("name")
            cate.name_two=request.POST.get("name_two")
            cate.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "main/next.html", {"cate" : cate})

    except cate.DoesNotExist:
        return HttpResponseRedirect("<h2>Not found page :(</h2>")

def delete(request, id):
    try:
        cate=Categories.objects.get(id=id)
        cate.delete()
        return HttpResponseRedirect("/")
    except cate.DoesNotExist:
        return HttpResponseRedirect("<h2>Not found page 😦 </h2>")

# def next_page(request):
# index_url=reverse("main:index")
# context={
# 'index_url' : index_url,
# }
# return render(request, "main/next.html", context)

# Create your views here.

