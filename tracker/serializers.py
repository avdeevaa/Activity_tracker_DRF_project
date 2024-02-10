from rest_framework import serializers

from tracker.models import Activity


class ActivitySerializer(serializers.ModelSerializer):  # Generics

    class Meta:
        model = Activity
        fields = '__all__'
