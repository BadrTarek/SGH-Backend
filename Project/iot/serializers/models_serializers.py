from ..models import Product , Sensor, Actuator, SensorValues, ActuatorsAction
from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin



class ProductSerializers(CountryFieldMixin , serializers.ModelSerializer):
    # sensors = SensorSerializer(many=True)
    # actuators = ActuatorSerializer(many=True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sensors'].write_only = True
            
    class Meta:
        model = Product
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True },  
            'user': {'write_only': True},
            'is_active':{'write_only':True},
            'token':{'write_only':True},
        }
        def update(self, product ,validated_data):
            
            product.country = validated_data.get("country" , product.country)
            product.automated_control = validated_data.get("automated_control" , product.automated_control)
            product.time_between_automated_action = validated_data.get("time_between_automated_action" , product.time_between_automated_action)
            
            product.save()
            

            return product

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'messure']
        
class ActuatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actuator
        fields = ['id', 'name', 'action']
        
class SensorValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorValues
        fields = ["value", "created_at", "sensor"]


class ActuatorActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActuatorsAction
        fields = ["value", "duration", "created_at", "actuator","is_automated_action"]