from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Team, Invitation
from django.urls import reverse
from django.conf import settings

from teams.forms import TeamForm

@login_required
def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.captain = request.user
            team.save()
            team.members.add(request.user)
            return redirect('teams:team_detail', team_id=team.id)
    else:
        form = TeamForm()
    return render(request, 'create_team.html', {'form': form})


@login_required
def create_invitation(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.user in team.members.all():
        if team.can_add_member():
            active_invitation = Invitation.objects.filter(team=team, used=False)
            invitation = Invitation.objects.create(team=team)
            invite_url = request.build_absolute_uri(reverse('teams:accept_invitation', args=[invitation.token]))
            return render(request, 'invitation_link.html', {'invite_url': invite_url})
        else:
            return render(request, 'error.html', {'message': 'Team has reached the maximum number of members.'})
    return redirect('teams:team_detail', team_id=team_id)


def accept_invitation(request, token):
    invitation = get_object_or_404(Invitation, token=token, used=False)
    team = invitation.team
    if request.user.is_authenticated:
        if team.can_add_member():
            team.members.add(request.user)
            invitation.used = True
            invitation.save()
            return redirect('teams:team_detail', team_id=team.id)
        else:
            return render(request, 'error.html', {'message': 'Team has reached the maximum number of members.'})
    else:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")


def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    return render(request, 'team_detail.html', {'team': team})



# Create your views here.
