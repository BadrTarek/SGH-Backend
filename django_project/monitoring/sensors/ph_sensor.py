from rest_framework import serializers , status
from library.api_response import ApiResponse

ID = 5
        

def input_validation(value):
    
    if float(value) >= 0 and float(value) <= 20:
        return True

    api_response = ApiResponse()
    response = api_response.set_data("errors", "Invalid PH Sensor Value").get()
    raise serializers.ValidationError(detail=response)