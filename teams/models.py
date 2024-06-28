from django.db import models
import uuid
from users.models import User
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название команды")
    captain = models.ForeignKey(User, on_delete=models.CASCADE, related_name='captain_teams')
    members = models.ManyToManyField(User, related_name="teams")
    max_members = models.PositiveIntegerField(default=5)

    def __str__(self):
        return self.name

    def can_add_member(self):
        return self.members.count() < self.max_members


class Invitation(models.Model):
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='invitations')
    used = models.BooleanField(default=False)

    def __str__(self):
        return f"Invitation to {self.team.name} (used: {self.used})"
from django.db import models

# Create your models here.
