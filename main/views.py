from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from main.models import Categories, Products

def index(request):
    return render(request, "main/index.html", {'None' : None})

def main(request):
    cate = Categories.objects.all()
    prod = Products.objects.all()
    context={
        'prod':prod,
        'cate':cate,
    }
    return render(request, "main/main.html", context)

def create(request):
    if request.method=="POST":
        cate=Categories()
        cate.name=request.POST.get("name")
        cate.name_two=request.POST.get("name_two")
        cate.save()
    #return render(request, "main/main.html")
    return HttpResponseRedirect("/main/")

def edit(request, id):
    try:
        cate=Categories.objects.get(id=id)
        if request.method=="POST":
            cate.name=request.POST.get("name")
            cate.name_two=request.POST.get("name_two")
            cate.save()
            return HttpResponseRedirect("/main/")
        else:
            return render(request, "main/next.html", {"cate" : cate})

    except cate.DoesNotExist:
        return HttpResponseRedirect("<h2>Not found page :(</h2>")

def delete(request, id):
    try:
        cate=Categories.objects.get(id=id)
        cate.delete()
        return HttpResponseRedirect("/main/")
    except cate.DoesNotExist:
        return HttpResponseRedirect("<h2>Not found page 😦 </h2>")