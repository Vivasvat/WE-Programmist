from .models import Team
from users.models import User
from django import forms

class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ['name', 'max_members']

    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)