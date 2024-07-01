from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import View
from django import forms

from .models import Tournaments

# Class that allows to use pagination along with filtering
class PaginatedFilterViews(View):
    def get_context_data(self, **kwargs):
        context = super(PaginatedFilterViews, self).get_context_data(**kwargs)
        if self.request.GET:
            querystring = self.request.GET.copy()
            if self.request.GET.get('page'):
                del querystring['page']
            context['querystring'] = querystring.urlencode()
        return context

# Class for filtering
class TournamentFilterForm(forms.Form):
    AREA_CHOICES = [
        ('Active', 'Текущие турниры'),
        ('Archive', 'Архивные турниры')
    ]

    GAME_CHOICES = [
        ('all', 'Все игры'),
        ('Dota 2', 'Dota 2'),
        ('CS2', 'Counter Strike 2'),
        ('HS', 'Hearthstone Battlegrounds'),
        ('Valorant', 'Valorant'),
    ]

    area = forms.ChoiceField(choices=AREA_CHOICES, widget=forms.RadioSelect, required=False)
    game = forms.ChoiceField(
        choices=GAME_CHOICES,
        required=False
    )

    # Set the initial value of filter
    def __init__(self, *args, **kwargs):
        super(TournamentFilterForm, self).__init__(*args, **kwargs)
        self.initial['area'] = 'Active'

# View for list of tournaments
class TournamentsListView(PaginatedFilterViews, ListView):
    model = Tournaments
    template_name = 'list_tournament.html'
    context_object_name = 'tournaments'
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset()
        area = self.request.GET.get('area', 'Active')
        game = self.request.GET.get('game')

        if area == 'Archive':
            queryset = queryset.filter(status='Archive').order_by('tournament_start_date')
        else:
            queryset = queryset.filter(status='Active').order_by('tournament_start_date')

        if game and game != 'all':
            queryset = queryset.filter(game=game).order_by('tournament_start_date')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = TournamentFilterForm(self.request.GET)
        context['area'] = self.request.GET.get('area', 'Active')
        return context

# View for detail of tournament
class TournamentDetailView(DetailView):
    model = Tournaments
    pk_url_kwarg = 'tournament_id'
    template_name = 'tournament_detail.html'
    context_object_name = 'tournament'

