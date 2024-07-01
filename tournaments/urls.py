from django.urls import path
from tournaments import views

app_name = 'tournaments'

urlpatterns = [
    path('tournaments/', views.TournamentsListView.as_view(),
         name='list_tournament'),
    path('tournaments/<int:tournament_id>/', views.TournamentDetailView.as_view(),
         name='tournament_detail'),
]
