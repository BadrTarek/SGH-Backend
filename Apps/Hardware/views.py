from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from Library.permissions import HasGreenhouse , IsGreenhouseAuthenticated
from .serializers import SensorValueSerializer  ,GetActionsSerializer , ActuatorActionsSerializer ,TakeActionSerializer,  StoreSensorValuesSerializer , GetSensorValuesSerializer
from Apps.Greenhouses.serializers import GreenhouseSerializers
from Library.api_response import ApiResponse

api_response = ApiResponse()

class StoreSensorsValuesView(APIView):
    # permission_classes = [IsGreenhouseAuthenticated]
    
    def post(self , request):
        api_response.__init__()
        
        serializer = StoreSensorValuesSerializer(data = request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors)
        
        sensor_values = serializer.save()
        greenhouse = serializer.get_greenhouse()
        
        api_response.set_status_code(status.HTTP_200_OK)
        # api_response.set_data("greenhouse",GreenhouseSerializers(greenhouse).data)
        api_response.set_data("sensor_values",SensorValueSerializer(sensor_values,many=True).data)

        return api_response.response()


class GetLastSensorValuesView(APIView):
    
    permission_classes = [IsAuthenticated & HasGreenhouse  ]
    
    def post(self , request ):
        api_response.__init__()
    
        serializer = GetSensorValuesSerializer(data=request.data)    
        
        if not serializer.is_valid():
            return Response(serializer.errors)
        
        values = serializer.get_last_values()
        
        api_response.set_status_code(status.HTTP_200_OK).set_data("data",values)

        return api_response.response()

class GetAllSensorValuesView(APIView):
    
    permission_classes = [IsAuthenticated & HasGreenhouse  ]
    
    def post(self , request ):
        
        api_response.__init__()

        serializer = GetSensorValuesSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors)
        
        values = serializer.get_all_values()

        api_response.set_status_code(status.HTTP_200_OK).set_data("data",values)

        return api_response.response()




class TakeAcionView(APIView):
    # permission_classes = [IsAuthenticated & HasGreenhouse  ]

    def post(self , request):

        api_response.__init__()

        serializer = TakeActionSerializer(data = request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        
        action = serializer.save()
        
        api_response.set_status_code(status.HTTP_200_OK)
        api_response.set_data("action",ActuatorActionsSerializer(action).data)

        return api_response.response()

    

class GetLastActionsView(APIView):
    
    # permission_classes = [IsAuthenticated & HasGreenhouse  ]
    
    def post(self , request ):
        api_response.__init__()
    
        serializer = GetActionsSerializer(data=request.data)    
        
        if not serializer.is_valid():
            return Response(serializer.errors)
        
        values = serializer.get_last_actions()
        
        api_response.set_status_code(status.HTTP_200_OK).set_data("data",values)

        return api_response.response()

class GetAllActionsView(APIView):
    
    # permission_classes = [IsAuthenticated & HasGreenhouse  ]
    
    def post(self , request ):
        
        api_response.__init__()

        serializer = GetActionsSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors)
        
        values = serializer.get_all_actions()

        api_response.set_status_code(status.HTTP_200_OK).set_data("data",values)

        return api_response.response()


