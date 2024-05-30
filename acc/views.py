from django.shortcuts import render

def index(request):
    return render(request, "acc/account.html")
# Create your views here.
