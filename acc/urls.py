from django.urls import path
from . import views

app_name = 'acc'

urlpatterns = [
    # path('', views.index_auth, name = 'index_auth'),
    path('acc/', views.profile, name = 'acc'),
    path('del_acc/', views.profile_delete_view, name='del_acc'),
    path('my_events/', views.my_events, name='my_events')
]