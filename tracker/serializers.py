from rest_framework import serializers

from tracker.models import Activity
from tracker.validators import ActivityTimeValidator, NoEnjoyableActionRewardValidator, PeriodsValidator
    # NoEnjoyableUsefulActionValidator


class ActivitySerializer(serializers.ModelSerializer):  # Generics

    class Meta:
        model = Activity
        fields = '__all__'
        validators = [
            ActivityTimeValidator(field='activity_time'),  # great, it works!
            NoEnjoyableActionRewardValidator(field1='is_enjoyable_action', field2='reward'),
            # NoEnjoyableUsefulActionValidator(field1='is_enjoyable_action', field2='is_useful_action'),
            PeriodsValidator(field1='periodicity')
        ]
