from django.db import models
import uuid
from users.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
class Team(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название команды")
    captain = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='captain_teams')
    members = models.ManyToManyField(
        User,
        related_name="teams")
    max_members = models.PositiveIntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(20)],
        verbose_name="Количество игроков")
    invitation_token = models.UUIDField(
        unique=True,
        blank=True,
        null=True)

    def __str__(self):
        return self.name

    def can_add_member(self):
        return self.members.count() < self.max_members

# Create your models here.
