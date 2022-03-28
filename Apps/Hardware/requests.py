from rest_framework import status
from rest_framework.response import Response
from .serializers.requests_serializers import TakeActionSerializer,  StoreSensorValuesSerializer , TakeAutomatedActionSerializer
from .serializers.models_serializers import SensorSerializer, ActuatorSerializer,SensorValueSerializer,ActuatorActionsSerializer 
from Apps.Greenhouses.greenhouse_data_model import GreenhouseDataModel
from Library.api_response import ApiResponse
from FuzzyLogic.fuzzy_logic_system_imlementation import implement

api_response = ApiResponse()


def store_sensors_values(data):
    api_response.__init__()
    
    serializer = StoreSensorValuesSerializer(data = data)
    
    if not serializer.is_valid():
        print(serializer.errors)
        return Response(serializer.errors)
    
    sensor_values = serializer.save()
        
    api_response.set_status_code(status.HTTP_200_OK)
    api_response.set_data("sensor_values",SensorValueSerializer(sensor_values,many=True).data)

    return api_response.response()


def store_sensors_values_with_fuzzy(data):
    api_response.__init__()
    
    serializer = StoreSensorValuesSerializer(data = data)
    
    if not serializer.is_valid():
        print(serializer.errors)
        return Response(serializer.errors)
    
    sensor_values = serializer.save()
    
    greenhouse = serializer.get_greenhouse()
    
    greenhouse_data = GreenhouseDataModel()
    greenhouse_data.set_greehouse(greenhouse).set_sensors_values(sensor_values)
    
    actions = implement(greenhouse_data)
    
    
    api_response.set_status_code(status.HTTP_200_OK)
    api_response.set_data("sensor_values",SensorValueSerializer(sensor_values,many=True).data)

    return actions ,api_response.response()



def take_automated_action(data):

    api_response.__init__()

    serializer = TakeAutomatedActionSerializer(data = data)
    
    if not serializer.is_valid():
        print(serializer.errors)
        return Response(serializer.errors)
    
    action = serializer.save()
    
    api_response.set_status_code(status.HTTP_200_OK)
    api_response.set_data("action",ActuatorActionsSerializer(action).data)
    
    return api_response.response()


def take_action(data):

    api_response.__init__()

    serializer = TakeActionSerializer(data = data)
    
    if not serializer.is_valid():
        print(serializer.errors)
        return Response(serializer.errors)
    
    action = serializer.save()
    
    api_response.set_status_code(status.HTTP_200_OK)
    api_response.set_data("action",ActuatorActionsSerializer(action).data)

    return api_response.response()



















# class GetLastSensorValuesView(APIView):
    
#     # permission_classes = [IsAuthenticated & HasGreenhouse  ]
    
#     def post(self , request ):
#         api_response.__init__()
    
#         serializer = GetSensorValuesSerializer(data=request.data)    
        
#         if not serializer.is_valid():
#             return Response(serializer.errors)
        
#         values = serializer.get_last_values()
        
#         api_response.set_status_code(status.HTTP_200_OK).set_data("data",values)

#         return api_response.response()

# class GetAllSensorValuesView(APIView):
    
#     # permission_classes = [IsAuthenticated & HasGreenhouse  ]
    
#     def post(self , request ):
        
#         api_response.__init__()

#         serializer = GetSensorValuesSerializer(data=request.data)
        
#         if not serializer.is_valid():
#             return Response(serializer.errors)
        
#         values = serializer.get_all_values()

#         api_response.set_status_code(status.HTTP_200_OK).set_data("data",values)

#         return api_response.response()




# class GetLastActionsView(APIView):
    
#     # permission_classes = [IsAuthenticated & HasGreenhouse  ]
    
#     def post(self , request ):
#         api_response.__init__()
    
#         serializer = GetActionsSerializer(data=request.data)    
        
#         if not serializer.is_valid():
#             return Response(serializer.errors)
        
#         values = serializer.get_last_actions()
        
#         api_response.set_status_code(status.HTTP_200_OK).set_data("data",values)

#         return api_response.response()

# class GetAllActionsView(APIView):
    
#     # permission_classes = [IsAuthenticated & HasGreenhouse  ]
    
#     def post(self , request ):
        
#         api_response.__init__()

#         serializer = GetActionsSerializer(data=request.data)
        
#         if not serializer.is_valid():
#             return Response(serializer.errors)
        
#         values = serializer.get_all_actions()

#         api_response.set_status_code(status.HTTP_200_OK).set_data("data",values)

#         return api_response.response()


