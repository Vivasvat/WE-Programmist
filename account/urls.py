from django.urls import path
from main import views

app_name = 'account'

urlpatterns = [
    # path('', views.index_auth, name = 'index_auth'),
    path('account/', views.account, name = 'account'),
]