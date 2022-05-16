from iot.models import Actuator, ActuatorsAction, Sensor , SensorValues
from rest_framework import serializers
from library.api_response import ApiResponse
from iot.serializers.models_serializers import ActuatorActionsSerializer
 

def make_automated_action(product,actuator_id,value,duration) -> ActuatorsAction:
    actuator = Actuator.get_actuator(actuator_id)
    return ActuatorActionsSerializer(ActuatorsAction.objects.create(
            actuator=actuator,
            product=product,
            value=value,
            duration=duration,
            is_automated_action = True
        )).data
    
def get_sensor_value(product, sensor_id):
    senor = Sensor.get_sensor(sensor_id)

    sensor_value = SensorValues.get_last_sensor_values(product,senor)
    
    if sensor_value == None:
        api_response = ApiResponse()
        response = api_response.set_data("errors", "Error").get()
        raise serializers.ValidationError(detail=response)
        
    
    return sensor_value.value