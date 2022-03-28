from rest_framework import serializers , status
from Library.api_response import ApiResponse
from .configuration import SENSORS , ACTUATORS


def sensor_value_validations( sensor_id  , value:str , raise_exception:bool = True):
    for sensor in SENSORS:
        if sensor_id == sensor.ID:
            sensor.input_validation(value)
            return
        
    if raise_exception:
        api_response = ApiResponse()
        response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("errors", "This sensor not found").get()
        raise serializers.ValidationError(detail=response)
    
    return False


def actuator_value_validations(actuator_id  , value:str , raise_exception:bool = True):
    
    for actuator in ACTUATORS:
        if actuator_id == actuator.ID:
            actuator.input_validation(value)
            return
        
    if raise_exception:
        api_response = ApiResponse()
        response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("errors", "This actuator not found").get()
        raise serializers.ValidationError(detail=response)
    
    return False

