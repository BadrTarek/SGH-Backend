from .models import  Sensor, SensorValues
from rest_framework import serializers



class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'messure']


class SensorValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorValues
        fields = ["value", "created_at", "sensor"]