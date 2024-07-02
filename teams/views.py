from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Team
from users.models import User
from django.urls import reverse
from teams.forms import TeamForm
import uuid

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
        if team.invitation_token is None:
            team.invitation_token = uuid.uuid4()
            team.save()
        invite_url = request.build_absolute_uri(
            reverse('teams:accept_invitation',
                    args=[team.invitation_token]))
        return render(request, 'invitation_link.html',
                      {'invite_url': invite_url, 'team': team})
    return redirect('teams:team_detail', team_id=team.id)


@login_required
def accept_invitation(request, token):
    team = get_object_or_404(Team, invitation_token=token)
    if request.user not in team.members.all():
        if team.can_add_member():
            team.members.add(request.user)
            team.save()
            return redirect('teams:team_detail', team_id=team.id)
        else:
            return render(request, 'error.html', {
                'message': 'В команде достигнуто максимальное число игроков',
                'team_id': team.id})
    else:
        return render(request, 'error.html',
                      {'message': 'Игрок уже находится в команде.',
                       'team_id': team.id})


def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    return render(request, 'team_detail.html', {'team': team})

@login_required
def team_update(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.user == team.captain:
        if request.method == 'POST':
            form = TeamForm(request.POST, instance=team)

            if 'remove_member' in request.POST:
                member_id = request.POST.get('remove_member')
                member_to_remove = get_object_or_404(User, id=member_id)
                team.members.remove(member_to_remove)
                return redirect('teams:team_update', team_id=team.id)

            if 'new_captain' in request.POST:
                new_captain_id = request.POST.get('new_captain')
                new_captain = get_object_or_404(User, id=new_captain_id)
                team.captain = new_captain
                team.save()
                return redirect('teams:team_detail', team_id=team.id)

            if form.is_valid():
                if form.cleaned_data['max_members'] < team.members.count():
                    return render(request, 'error.html', {
                        'message': 'Невозможно уменьшить размер команды, количество игроков превышает максимальное.',
                        'team_id': team_id
                    })

                form.save()
                return redirect('teams:team_detail', team_id=team.id)
        else:
            form = TeamForm(instance=team)

        return render(request, 'team_update.html', {
            'form': form,
            'team': team})
    else:
        return render(request, 'error.html', {
            'message': 'Только капитан может редактировать команды',
            'team_id': team_id})

@login_required
def team_delete(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.user == team.captain:
        team.delete()
        return redirect('acc:acc')
    else:
        return render(request, 'error.html', {
            'message': 'Только капитан команды может удалить команду',
            'team_id': team_id})
