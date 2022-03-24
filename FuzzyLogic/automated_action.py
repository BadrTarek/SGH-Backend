from xmlrpc.client import ResponseError
from Apps.Hardware.serializers.requests_serializers import TakeAutomatedActionSerializer
from Library.api_response import ApiResponse
from rest_framework.response import Response
from rest_framework import serializers




def request(greenhouse_id:int,password:str,actuator_id:int,value:str,duration:str=None):
    json = {
        "greenhouse_id":greenhouse_id,
        "password":password,
        "actuator_id":actuator_id,
        "value":value,
        "duration":duration,
    }
    serializer = TakeAutomatedActionSerializer(data = json)
    serializer.is_valid(raise_exception=True)
    
    serializer.save()
    
    
