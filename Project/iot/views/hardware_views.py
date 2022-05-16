from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from library.permissions import HasProduct , IsProductAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from ..serializers.hardware_requests_serializers import TakeActionSerializer,  StoreSensorValuesSerializer  , GetSensorValuesSerializer , GetActionsSerializer
from ..serializers.models_serializers import SensorSerializer, ActuatorSerializer,SensorValueSerializer,ActuatorActionsSerializer 
from library.api_response import ApiResponse
from library.helper import print_error_in_console

api_response = ApiResponse()

class StoreSensorsValuesView(APIView):
    # permission_classes = [IsProductAuthenticated]
    
    def post(self , request):
        api_response.__init__()
        
        serializer = StoreSensorValuesSerializer(data= request.data)
        
        if not serializer.is_valid():
            print_error_in_console("Store Sensor Values Request",serializer.errors)
            return api_response.set_status_code(status.HTTP_400_BAD_REQUEST).merge_dict(serializer.errors).response()

        
        sensor_values = serializer.save()
            
        api_response.set_status_code(status.HTTP_200_OK)
        api_response.set_data("sensors",SensorValueSerializer(sensor_values,many=True).data)
        
        return api_response.response()
    

class TakeAcionView(APIView):
    # permission_classes = [IsAuthenticated & HasProduct  ]

    def post(self , request):
        api_response.__init__()
        
        serializer = TakeActionSerializer(data = request.data)
        if not serializer.is_valid():
            print_error_in_console("Take Action Request",serializer.errors)
            return api_response.set_status_code(status.HTTP_400_BAD_REQUEST).merge_dict(serializer.errors).response()

        action = serializer.save()
        
        api_response.set_status_code(status.HTTP_200_OK)
        api_response.set_data("action",ActuatorActionsSerializer(action).data)
        
        return api_response.response()

        
            



class GetAllSensorValuesView(APIView):
    # permission_classes = [IsAuthenticated & HasProduct  ]

    def post(self , request ):
        api_response.__init__()

        serializer = GetSensorValuesSerializer(data=request.data)
        
        if not serializer.is_valid():
            print_error_in_console("Get All Sensors Request",serializer.errors)
            return api_response.set_status_code(status.HTTP_400_BAD_REQUEST).merge_dict(serializer.errors).response()

        
        values = serializer.get_all_values()

        api_response.set_status_code(status.HTTP_200_OK).set_data("data",values)

        return api_response.response()


class GeAllActionsView(APIView):
    # permission_classes = [IsAuthenticated & HasProduct  ]

    def post(self , request ):
        api_response.__init__()

        serializer = GetActionsSerializer(data=request.data)
        
        if not serializer.is_valid():
            print_error_in_console("Get All Actions Request",serializer.errors)
            return api_response.set_status_code(status.HTTP_400_BAD_REQUEST).merge_dict(serializer.errors).response()

        
        actions = serializer.get_all_actions()

        api_response.set_status_code(status.HTTP_200_OK).set_data("data",actions)

        return api_response.response()


    






