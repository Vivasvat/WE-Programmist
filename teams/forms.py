from .models import Team
from django import forms

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'max_members']
