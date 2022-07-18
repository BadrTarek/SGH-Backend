from .models import Actuator, ActuatorsAction
from rest_framework import serializers


class ActuatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actuator
        fields = ['id', 'name', 'action']



class ActuatorActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActuatorsAction
        fields = ["value", "duration", "created_at", "actuator", "is_automated_action"]