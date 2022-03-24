from rest_framework import serializers , status
from Library.api_response import ApiResponse


ID = 5
        

def input_validation(value):
    
    if value in range(0,14):
        return True

    api_response = ApiResponse()
    response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("errors", "Invalid Sensor Value").get()
    raise serializers.ValidationError(detail=response)