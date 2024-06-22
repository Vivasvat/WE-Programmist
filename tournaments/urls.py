from django.urls import path
from tournaments import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'tournaments'

urlpatterns = [
    path('tournaments/', views.TournamentsListView.as_view(),
         name='list_tournament'),
    path('tournaments/<int:tournament_id>/', views.TournamentDetailView.as_view(),
         name='tournament_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
