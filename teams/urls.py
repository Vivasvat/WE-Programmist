from django.urls import path
from teams import views
from django.contrib.auth import views as auth_views

app_name = 'teams'

urlpatterns=[
    path('team/<int:team_id>/', views.team_detail, name='team_detail'),
    path('create_team/', views.create_team, name='create_team'),
    path('invite/<int:team_id>/', views.create_invitation, name='create_invitation'),
    path('accept_invitation/<uuid:token>/', views.accept_invitation, name='accept_invitation'),
    path('team/<int:team_id>/update/', views.team_update, name='team_update'),
    path('team/<int:team_id>/delete/', views.team_delete, name='team_delete'),
]