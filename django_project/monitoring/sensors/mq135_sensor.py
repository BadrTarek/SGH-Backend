from rest_framework import serializers , status
from library.api_response import ApiResponse


ID = 3

def input_validation(value):
    # if float(value) == float:
    return True
    
    api_response = ApiResponse()
    response = api_response.set_data("errors", "Invalid Gas Sensor Value").get()
    raise serializers.ValidationError(detail=response)
    
    