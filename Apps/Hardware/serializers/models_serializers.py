from rest_framework import serializers
from Apps.Hardware.models import Sensor, Actuator, ActuatorsAction, SensorValues

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'messure']
        
class ActuatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actuator
        fields = "__all__"
        fields = ['id', 'name', 'action']
        
class SensorValueSerializer(serializers.ModelSerializer):
    # sensor = SensorSerializer()
    class Meta:
        model = SensorValues
        fields = ["value", "created_at", "sensor"]


class ActuatorActionsSerializer(serializers.ModelSerializer):
    # actuator = ActuatorSerializer()
    class Meta:
        model = ActuatorsAction
        fields = ["value", "duration", "created_at", "actuator","is_automated_action"]