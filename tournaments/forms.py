from django import forms
from teams.models import Team

class TeamSelectionForm(forms.Form):
    team = forms.ModelChoiceField(queryset=Team.objects.none(), label='Команда')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['team'].queryset = Team.objects.filter(captain=user)