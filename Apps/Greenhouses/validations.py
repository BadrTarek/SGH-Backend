from Apps.Greenhouses.models import Greenhouse, GreenhouseActustor, GreenhouseSensor
from Apps.Hardware.models import Sensor, Actuator
from rest_framework import serializers , status
from Library.api_response import ApiResponse



def greenhouse_validation(id:int , password:str , raise_exception:bool = True):
    try:

        Greenhouse.objects.get(pk=id, password=password , is_active = True)
        return True
    except Greenhouse.DoesNotExist:
        if raise_exception:
            api_response = ApiResponse()
            response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("errors", "A greenhouse with this ID and password is not found.").get()
            raise serializers.ValidationError(detail=response)
    return False

def greenhouse_sensor_validation(sensor_id: int, greenhouse_id:int , raise_exception:bool = True):
    try:
        sensor = Sensor.objects.get(pk = sensor_id)
        greenhouse = Greenhouse.objects.get(pk = greenhouse_id)
        GreenhouseSensor.objects.get(sensor=sensor, greenhouse=greenhouse)
        return True
    except (GreenhouseSensor.DoesNotExist , Sensor.DoesNotExist , Greenhouse.DoesNotExist):
        if raise_exception:
            api_response = ApiResponse()
            response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("errors", "This sensor not integrated with this greenhouse or not exist").get()
            raise serializers.ValidationError(detail=response)
    return False

def greenhouse_actuator_validation(actuator_id: int, greenhouse_id:int , raise_exception:bool = True):
    try:
        actuator = Actuator.objects.get(pk = actuator_id)
        greenhouse = Greenhouse.objects.get(pk = greenhouse_id)
        GreenhouseActustor.objects.get(actuator=actuator, greenhouse=greenhouse)
        return True
    except (GreenhouseActustor.DoesNotExist , Actuator.DoesNotExist , Greenhouse.DoesNotExist):
        if raise_exception:
            api_response = ApiResponse()
            response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("errors", "This actuator not integrated with this greenhouse or not exist").get()
            raise serializers.ValidationError(detail=response)  
    return False

def is_allow_automated_control(id:int , password:str ):
    try:
        greenhouse = Greenhouse.objects.get(pk=id, password=password , is_active = True)
        return greenhouse.automated_control
    except (Greenhouse.DoesNotExist):
        api_response = ApiResponse()
        response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("errors", "This actuator not integrated with this greenhouse or not exist").get()
        raise serializers.ValidationError(detail=response)

    return False