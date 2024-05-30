from django.urls import path
from . import views

app_name = 'acc'

urlpatterns = [
    # path('', views.index_auth, name = 'index_auth'),
    path('acc/', views.index, name = 'acc'),
]