from rest_framework import serializers , status
from Library.api_response import ApiResponse


ID = 2

def input_validation(value):
    
    light_values = [1,0]
        
    if value in light_values:
        return True
    api_response = ApiResponse()
    response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("errors", "Invalid Sensor Value").get()
    raise serializers.ValidationError(detail=response)