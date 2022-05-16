from ..models import Product , ProductActuator, Sensor, Actuator, ActuatorsAction, SensorValues
from rest_framework import serializers
from ..validations.products_validations import product_validation, product_sensor_validation, product_actuator_validation , is_allow_automated_control
from ..validations.hardware_validations import sensor_validation , actuator_validation 
from .models_serializers import ActuatorActionsSerializer 



class SensorWithValueSerializer(serializers.Serializer):
    sensor_id = serializers.IntegerField()
    value = serializers.CharField()
    
class StoreSensorValuesSerializer(serializers.Serializer):
    # Token instead of id,password
    product_id = serializers.IntegerField()
    password = serializers.CharField()
    sensors = serializers.ListField(child = SensorWithValueSerializer())
            
    def validate(self, data):
        product_validation(data["product_id"] , data["password"])
        for sensor in data["sensors"]:
            sensor_validation(id = sensor['sensor_id'],value = sensor["value"])
            product_sensor_validation(sensor['sensor_id'],data["product_id"])
        return data

    def save(self,**kwargs):
        
        self.sensor_values_response = []
        self.product = Product.get_product(self.data['product_id'],self.data['password'])

        for sensor in self.data["sensors"]:
            my_sensor = Sensor.get_sensor(sensor['sensor_id'])
            
            sensor_value = SensorValues()
            sensor_value.product=self.product
            sensor_value.sensor=my_sensor
            sensor_value.value=sensor["value"]
            sensor_value.save()
            
            self.sensor_values_response.append(sensor_value)

        return self.sensor_values_response


class TakeActionSerializer(serializers.Serializer):

    product_id = serializers.IntegerField()
    password = serializers.CharField()
    actuator_id = serializers.IntegerField()
    value = serializers.CharField()
    duration = serializers.CharField(required=False, allow_null=True)
    
    def validate(self, data):
        product_validation(data["product_id"],data["password"])
        actuator_validation(data["actuator_id"])
        product_actuator_validation(data["actuator_id"],data["product_id"])
        return data

    def save(self,  **kwargs):
        self.actuator = Actuator.get_actuator(self.data["actuator_id"])
        self.product = Product.get_product(self.data["product_id"],self.data["password"])
        action = ActuatorsAction.objects.create(
            actuator=self.actuator,
            product=self.product,
            value=self.data["value"],
            duration=self.data["duration"]
        )

        return action


class GetSensorValuesSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    password = serializers.CharField(max_length=10)
    sensor_id = serializers.IntegerField(required=False, allow_null=True)

    def validate(self, data):
        product_validation(data["product_id"] ,data["password"] )
        product_sensor_validation(data["sensor_id"],data["product_id"])
        
        return data

    def get_all_values(self):
        self.product = Product.get_product(self.data["product_id"] ,self.data["password"])
        self.sensor = Sensor.get_sensor(self.data["sensor_id"])
        return SensorValues.get_all_sensor_values(self.product, self.sensor)


class GetActionsSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    password = serializers.CharField(max_length=10)

    def validate(self, data):

        product_validation(id = data["id"], password=data["password"])
        self.product = Product.get_product(data["id"], data["password"])
        self.product_actuators = ProductActuator.get_product_actuators(self.product)
        
        return data


    def get_all_actions(self):

        actions = []

        for product_actuator in self.product_actuators:
            action = ActuatorsAction.get_all_actuator_actions(self.product,product_actuator.actuator)
            actions.append(ActuatorActionsSerializer(action , many=True).data)
        print(actions)
        return actions
