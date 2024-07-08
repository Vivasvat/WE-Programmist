from django.urls import path
from . import views
from teams.views import user_teams_view

app_name = 'acc'

urlpatterns = [
    # path('', views.index_auth, name = 'index_auth'),
    path('acc/', views.profile, name = 'acc'),
    path('del_acc/', views.profile_delete_view, name='del_acc'),
    path('my_events/', views.UserTournamentsListView.as_view(), name='my_events'),
    path('my_teams/', user_teams_view, name='user_teams'),
]