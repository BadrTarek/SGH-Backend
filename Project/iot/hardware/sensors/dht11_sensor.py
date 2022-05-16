from rest_framework import serializers , status
from library.api_response import ApiResponse


ID = 1
        

MIN_TEMP = -60
MAX_TEMP = 60

def input_validation(value):
    try:
        if float(value) >= MIN_TEMP and float(value)<=MAX_TEMP:
            return True
    except :
        pass
    
    api_response = ApiResponse()
    response = api_response.set_data("errors", "Invalid Temprature Sensor Value").get()
    raise serializers.ValidationError(detail=response)
    
    