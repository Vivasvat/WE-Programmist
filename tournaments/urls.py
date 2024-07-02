from django.urls import path
from tournaments import views

app_name = 'tournaments'

urlpatterns = [
    path('tournaments/', views.TournamentsListView.as_view(),
         name='list_tournament'),
    path('tournaments/<int:tournament_id>/', views.TournamentDetailView.as_view(),
         name='tournament_detail'),
    path('register_team_for_tournament/<int:tournament_id>/',
         views.RegisterTeamForTournamentView.as_view(),
         name='register_team_for_tournament'),
]
