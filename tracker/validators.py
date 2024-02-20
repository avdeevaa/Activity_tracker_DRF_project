from rest_framework.serializers import ValidationError


class ActivityTimeValidator:
    """Время выполнения должно быть не больше 20 минут"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        activity_time = value.get(self.field)
        if activity_time > 20:
            raise ValidationError('Время для привычки не может быть более 20 минут.')


class NoEnjoyableActionRewardValidator:
    """Исключить одновременный выбор приятной привычки и указания вознаграждения"""

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        if self.field1 and self.field2:
            raise ValidationError('У приятной привычки не может быть вознаграждения')


class NoEnjoyableUsefulActionValidator:
    """У приятной привычки не может быть связанной привычки"""

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        if self.field1 == True and self.field2 == True:  # not "is" nor "=="
            raise ValidationError('У приятной привычки не может быть связанной (полезной) привычки.')


class PeriodsValidator:
    """Нельзя выполнять привычку реже, чем 1 раз в 7 дней."""

    def __init__(self, field1):
        self.field1 = field1

    def __call__(self, value):
        possible_values = {'daily', 'once a week', 'twice a week'}

        if value not in possible_values:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')
#
