from django.db import models

from config import settings


class Activity(models.Model):

    PLACES = [
        ('home', 'home'),
        ('outside', 'outside'),
        ('work', 'work')
    ]

    PERIODS = [
        ('daily', 'daily'),
        ('once a week', 'once a week'),
        ('twice a week', 'twice a week')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    place = models.CharField(verbose_name="место для привычки", choices=PLACES, default="home")
    time = models.DateTimeField(verbose_name="время для привычки")
    action = models.CharField(max_length=500, verbose_name='действие привычки')

    is_enjoyable_action = models.BooleanField(default=False, verbose_name="Признак приятной привычки", null=True, blank=True)
    is_useful_action = models.BooleanField(default=False, verbose_name="Связанная, полезная привычка", null=True, blank=True)

    periodicity = models.CharField(verbose_name="Периодичность", choices=PERIODS, default="daily")
    reward = models.CharField(max_length=500, verbose_name='Вознаграждение', null=True, blank=True)
    activity_time = models.PositiveIntegerField(verbose_name='Время на выполнение')
    public = models.BooleanField(verbose_name='Признак публичности', default=False)

    def __str__(self):
        return f'я буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"
