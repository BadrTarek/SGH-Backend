from iot.models import Sensor , Actuator , SensorValues , Product
from .required_hardware import SENSORS, ACTUATORS
from ...apps import AutomatedControlConfig
from ...helper import make_automated_action , get_sensor_value
from ...validations import check_date
from library.api_response import ApiResponse
from rest_framework import serializers 
from rest_framework import status
from library.helper import print_error_in_console

def validation(product):
    for actuator_id in ACTUATORS:
        actuator = Actuator.get_actuator(actuator_id)
        if not check_date(product, actuator):
            api_response = ApiResponse()
            print_error_in_console("Automated Action","Cannot apply automated action in this time")
            response = api_response.set_status_code(status.HTTP_400_BAD_REQUEST).set_data("errors", "Cannot apply automated action in this time").get()
            raise serializers.ValidationError(detail=response)


def get_actions(product:Product)->list:

    validation(product)

    ph_value = get_sensor_value(product,SENSORS[0])
    water_level = get_sensor_value(product,SENSORS[1])
    
    
    
    model = AutomatedControlConfig.ph_model
    model.set_input_values(ph_value,water_level)
    model.defuzzification()
    output = model.get_ouput_values()

    return [
        make_automated_action(product,ACTUATORS[0],  1 if output["ph_pump"] > 0 else 0  ,output["ph_pump"]),
        make_automated_action(product,ACTUATORS[1],1 if output["alkaline_pump"] > 0 else 0,output["alkaline_pump"]),
    ]