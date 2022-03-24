from .sensors import PHSensor , TempratureSensor , WaterLevelSensor, GasSensor,LightSensor
from .actuators import AlkalinePumpActuator, FanActuator, PHPumpActuator, LEDActuator
from rest_framework import serializers , status
from Library.api_response import ApiResponse


def sensor_value_validations( sensor_id  , value:str , raise_exception:bool = True):
    match sensor_id:
        case PHSensor.ID:
            PHSensor.input_validation(value)
            return
        case TempratureSensor.ID:
            TempratureSensor.input_validation(value)
            return 
        case WaterLevelSensor.ID:
            WaterLevelSensor.input_validation(value)
            return
        case GasSensor.ID:
            GasSensor.input_validation(value)
            return
        case LightSensor.ID:
            LightSensor.input_validation(value)
            return
        case _:
            if raise_exception:
                api_response = ApiResponse()
                response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("errors", "This sensor not found").get()
                raise serializers.ValidationError(detail=response)
            
    return False

def actuator_value_validations(actuator_id  , value:str , raise_exception:bool = True):
    match actuator_id:
        case AlkalinePumpActuator.ID:
            AlkalinePumpActuator.input_validation(value)
            return
        case PHPumpActuator.ID:
            PHPumpActuator.input_validation(value)
            return 
        case FanActuator.ID:
            FanActuator.input_validation(value)
            return
        case LEDActuator.ID:
            LEDActuator.input_validation(value)
            return
        case _:
            if raise_exception:
                api_response = ApiResponse()
                response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("errors", "This actuator not found").get()
                raise serializers.ValidationError(detail=response)
            
    return False



        
