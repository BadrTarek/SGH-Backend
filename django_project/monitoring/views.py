from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from library.permissions import HasProduct , IsProductAuthenticated
from rest_framework import status
from .requests_serializers import StoreSensorValuesSerializer, GetSensorValuesSerializer
from .models_serializers import SensorSerializer, SensorValueSerializer
from library.api_response import ApiResponse
from library.helper import print_error_in_console
from rest_framework_simplejwt.authentication import JWTAuthentication

api_response = ApiResponse()

class StoreSensorsValuesView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny & IsProductAuthenticated  ]

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



class GetAllSensorValuesView(APIView):
    permission_classes = [IsAuthenticated & HasProduct  ]

    def post(self , request ):
        api_response.__init__()

        serializer = GetSensorValuesSerializer(data=request.data)

        if not serializer.is_valid():
            print_error_in_console("Get All Sensors Request",serializer.errors)
            return api_response.set_status_code(status.HTTP_400_BAD_REQUEST).merge_dict(serializer.errors).response()


        # values = SensorValueSerializer( serializer.get_all_values(),many=True).data
        # print(list(serializer.get_all_values()))
        values = []
        for i in list(serializer.get_all_values()):
            values.append(float(i[0]))
        # print(values)
        # plt.figure(figsize=(50,8))
        # plt.plot(values)
        # plt.legend()
        # plt.savefig("plot.png")
        # plt.show()

        api_response.set_status_code(status.HTTP_200_OK).set_data("data",values)

        return api_response.response()
