from rest_framework import serializers , status
from Library.api_response import ApiResponse


ID = 1
        

MIN_TEMP = -60
MAX_TEMP = 60

def input_validation(value):
    try:
        if float(value) in range(MIN_TEMP,MAX_TEMP):
            return True
    except :
        pass
    
    api_response = ApiResponse()
    response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("errors", "Invalid Sensor Value").get()
    raise serializers.ValidationError(detail=response)
    
    