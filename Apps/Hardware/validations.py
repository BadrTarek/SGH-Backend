from .models import Sensor , Actuator , SensorValues, ActuatorsAction
from rest_framework import serializers , status
from Library.api_response import ApiResponse
from .hardware_library.values_validations import sensor_value_validations ,actuator_value_validations

def sensor_validation(id:int , value:str = None , raise_exception:bool = True ):
    try:
        Sensor.objects.get(pk=id)
        if value != None:
            sensor_value_validations(id , value)
        return True
    except Sensor.DoesNotExist:
        if raise_exception:
            api_response = ApiResponse()
            response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("errors", "This sensor not integrated with this greenhouse or not exist").get()
            raise serializers.ValidationError(detail=response)
        
    return False

def actuator_validation(id:int ,value:str = None , raise_exception:bool = True):
    try:
        Actuator.objects.get(pk=id)
        if value != None:
            actuator_value_validations(id , value)
        return True
    except Actuator.DoesNotExist:
        if raise_exception:
            api_response = ApiResponse()
            response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("errors", "This actuator not integrated with this greenhouse or not exist").get()
            raise serializers.ValidationError(detail=response)
    return False

