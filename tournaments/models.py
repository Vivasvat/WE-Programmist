from django.db import models

# Create your models here.
class Tournaments(models.Model):

    GAME_CHOICES = [
        ('Dota 2', 'Dota 2'),
        ('CS2', 'Counter Strike 2'),
        ('HS', 'Hearthstone Battlegrounds'),
        ('Valorant', 'Valorant'),
    ]

    FORMAT_CHOICES = [
        ('Single Elimination', 'Олимпийская система'),
        ('Double Elimination', 'Выбывание после 2-х поражений'),
        ('Round Robbin', 'Круговая система'),
    ]

    STATUS_CHOICES = [
        ('Active', 'Предстоящий'),
        ('Archive', 'Завершенный'),
    ]

    PARTICIPATION_CHOICES = [
        ('1X1','1X1'),
        ('2X2','2X2'),
        ('5X5', '5X5'),
    ]

    TYPE_CHOICES = [
        ('Online', 'Online'),
        ('Offline', 'Offline'),
    ]

    name = models.CharField(
        max_length=150,
        verbose_name='Название'
    )

    picture = models.ImageField(
        blank=True,
        null=True,
        verbose_name='Изображение',
        upload_to="static/images/tournaments/"
    )

    organizer = models.CharField(
        max_length=150,
        verbose_name='Организатор',
        blank=True,
        null=True
    )

    tournament_start_date = models.DateTimeField(
        verbose_name='Дата начала турнира'
    )

    tournament_end_date = models.DateTimeField(
        verbose_name='Дата окончания турнира'
    )

    registration_start_date = models.DateTimeField(
        verbose_name='Дата начала регистрации'
    )

    registration_end_date = models.DateTimeField(
        verbose_name='Дата окончания регистрации'
    )

    status = models.CharField(
        max_length=150,
        verbose_name='Статус',
        choices=STATUS_CHOICES

    )

    format_of_tournament = models.CharField(
        max_length=150,
        verbose_name='Формат',
        choices=FORMAT_CHOICES
    )

    type_of_tournament = models.CharField(
        max_length=150,
        verbose_name='Тип',
        choices=TYPE_CHOICES
    )

    format_of_participation = models.CharField(
        max_length=150,
        verbose_name='Формат участия',
        choices=PARTICIPATION_CHOICES
    )

    prize_fund = models.DecimalField(
        default=0.00,
        max_digits=7,
        decimal_places=2,
        verbose_name='Призовой фонд'
    )

    game = models.CharField(
        max_length=150,
        verbose_name='Игра',
        choices=GAME_CHOICES
    )