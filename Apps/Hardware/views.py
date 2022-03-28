from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from Library.permissions import HasGreenhouse , IsGreenhouseAuthenticated


from .requests import store_sensors_values, take_action



class StoreSensorsValuesView(APIView):
    # permission_classes = [IsGreenhouseAuthenticated]
    
    def post(self , request):
        return store_sensors_values(request.data)



class TakeAcionView(APIView):
    # permission_classes = [IsAuthenticated & HasGreenhouse  ]

    def post(self , request):
        return take_action(request.data)


    









# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
# from Library.permissions import HasGreenhouse , IsGreenhouseAuthenticated
# from .serializers.requests_serializers import TakeActionSerializer,  StoreSensorValuesSerializer , TakeAutomatedActionSerializer
# from .serializers.models_serializers import SensorSerializer, ActuatorSerializer,SensorValueSerializer,ActuatorActionsSerializer 
# # from FuzzyLogic.fuzzy_system_imlementation import FuzzyImplementation
# from Library.api_response import ApiResponse

# api_response = ApiResponse()


# class TakeAutomatedActionView(APIView):
#     def post(self,request):

#         api_response.__init__()

#         serializer = TakeAutomatedActionSerializer(data = request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors)
        
#         action = serializer.save()
        
#         api_response.set_status_code(status.HTTP_200_OK)
#         api_response.set_data("action",ActuatorActionsSerializer(action).data)
        
#         # from FuzzyLogic.automated_action import request as automated_action_request
#         # automated_action_request(1,"mqN9weY",1,"Badoooooor")
        
        
#         # api_response.set_data("Message","sss")
#         # return api_response.response()



# # class StoreSensorsValuesFuzzyView(APIView):
# #     # permission_classes = [IsGreenhouseAuthenticated]
    
# #     def post(self , request):
# #         api_response.__init__()
        
# #         serializer = StoreSensorValuesSerializer(data = request.data)
        
# #         if not serializer.is_valid():
# #             return Response(serializer.errors)
        
# #         sensor_values = serializer.save()

# #         fuzzy = FuzzyImplementation()
        
# #         fuzzy.set_sensors_values(sensor_values)
# #         fuzzy.take_actions()
        
# #         api_response.set_status_code(status.HTTP_200_OK)
# #         # api_response.set_data("greenhouse",GreenhouseSerializers(greenhouse).data)
# #         api_response.set_data("sensor_values",SensorValueSerializer(sensor_values,many=True).data)

# #         return api_response.response()















# class StoreSensorsValuesView(APIView):
#     # permission_classes = [IsGreenhouseAuthenticated]
    
#     def post(self , request):
#         api_response.__init__()
        
#         serializer = StoreSensorValuesSerializer(data = request.data)
        
#         if not serializer.is_valid():
#             return Response(serializer.errors)
        
#         sensor_values = serializer.save()
#         greenhouse = serializer.get_greenhouse()
        
#         api_response.set_status_code(status.HTTP_200_OK)
#         # api_response.set_data("greenhouse",GreenhouseSerializers(greenhouse).data)
#         api_response.set_data("sensor_values",SensorValueSerializer(sensor_values,many=True).data)

#         return api_response.response()


# # class GetLastSensorValuesView(APIView):
    
# #     # permission_classes = [IsAuthenticated & HasGreenhouse  ]
    
# #     def post(self , request ):
# #         api_response.__init__()
    
# #         serializer = GetSensorValuesSerializer(data=request.data)    
        
# #         if not serializer.is_valid():
# #             return Response(serializer.errors)
        
# #         values = serializer.get_last_values()
        
# #         api_response.set_status_code(status.HTTP_200_OK).set_data("data",values)

# #         return api_response.response()

# # class GetAllSensorValuesView(APIView):
    
# #     # permission_classes = [IsAuthenticated & HasGreenhouse  ]
    
# #     def post(self , request ):
        
# #         api_response.__init__()

# #         serializer = GetSensorValuesSerializer(data=request.data)
        
# #         if not serializer.is_valid():
# #             return Response(serializer.errors)
        
# #         values = serializer.get_all_values()

# #         api_response.set_status_code(status.HTTP_200_OK).set_data("data",values)

# #         return api_response.response()





# # class GetLastActionsView(APIView):
    
# #     # permission_classes = [IsAuthenticated & HasGreenhouse  ]
    
# #     def post(self , request ):
# #         api_response.__init__()
    
# #         serializer = GetActionsSerializer(data=request.data)    
        
# #         if not serializer.is_valid():
# #             return Response(serializer.errors)
        
# #         values = serializer.get_last_actions()
        
# #         api_response.set_status_code(status.HTTP_200_OK).set_data("data",values)

# #         return api_response.response()

# # class GetAllActionsView(APIView):
    
# #     # permission_classes = [IsAuthenticated & HasGreenhouse  ]
    
# #     def post(self , request ):
        
# #         api_response.__init__()

# #         serializer = GetActionsSerializer(data=request.data)
        
# #         if not serializer.is_valid():
# #             return Response(serializer.errors)
        
# #         values = serializer.get_all_actions()

# #         api_response.set_status_code(status.HTTP_200_OK).set_data("data",values)

# #         return api_response.response()


