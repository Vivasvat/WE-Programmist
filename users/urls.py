from django.urls import path
from users import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns=[
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.logout, name='logout'),
   
]