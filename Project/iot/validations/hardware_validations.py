from ..models import Sensor , Actuator
from rest_framework import serializers 
from library.api_response import ApiResponse
from ..hardware.settings import SENSORS , ACTUATORS



# Hardware validations
def sensor_validation(id:int , value:str = None , raise_exception:bool = True ):
    try:
        Sensor.objects.get(pk=id)
        if value != None:
            sensor_value_validations(id , value)
        return True
    except Sensor.DoesNotExist:
        if raise_exception:
            api_response = ApiResponse()
            response = api_response.set_data("errors", "This sensor not integrated with this product or not exist").get()
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
            response = api_response.set_data("errors", "This actuator not integrated with this product or not exist").get()
            raise serializers.ValidationError(detail=response)
    return False



# Hardware values validations

def sensor_value_validations( sensor_id  , value:str , raise_exception:bool = True):
    for sensor in SENSORS:
        if sensor_id == sensor.ID:
            sensor.input_validation(value)
            return True
        
    if raise_exception:
        api_response = ApiResponse()
        response = api_response.set_data("errors", "This sensor not found").get()
        raise serializers.ValidationError(detail=response)
    
    return False


def actuator_value_validations(actuator_id  , value:str , raise_exception:bool = True):
    
    for actuator in ACTUATORS:
        if actuator_id == actuator.ID:
            actuator.input_validation(value)
            return True
        
    if raise_exception:
        api_response = ApiResponse()
        response = api_response.set_data("errors", "This actuator not found").get()
        raise serializers.ValidationError(detail=response)
    
    return False
