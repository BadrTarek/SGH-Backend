from .models import Actuator
from rest_framework import serializers
from library.api_response import ApiResponse
from .actuators_config import ACTUATORS


# Hardware validations


def actuator_validation(id: int, value: str = None, raise_exception: bool = True):
    try:
        Actuator.objects.get(pk=id)
        if value != None:
            actuator_value_validations(id, value)
        return Actuator.objects.get(pk=id)
    except Actuator.DoesNotExist:
        if raise_exception:
            api_response = ApiResponse()
            response = api_response.set_data("errors",
                                             "This actuator or not exist").get()
            raise serializers.ValidationError(detail=response)
    return False


# Hardware values validations

def actuator_value_validations(actuator_id, value: str, raise_exception: bool = True):
    for actuator in ACTUATORS:
        if actuator_id == actuator.ID:
            actuator.input_validation(value)
            return True

    if raise_exception:
        api_response = ApiResponse()
        response = api_response.set_data("errors", "This actuator not found").get()
        raise serializers.ValidationError(detail=response)

    return False
