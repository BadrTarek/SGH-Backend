import socketio
from Library.api_response import ApiResponse
from rest_framework import status
from SocketIO.socketio_server_settings import HARDWARE_NAMESPACE, WEB_NAMESPACE, MOBILE_NAMESPACE

from Apps.Hardware.serializers.models_serializers import SensorValueSerializer
from Apps.Hardware.serializers.requests_serializers import StoreSensorValuesSerializer

# ------------------------------------------------------ Hardware Client
class HardwareNamespace(socketio.Namespace):

    def on_connect(self, sid, message):

        print("Hardware Connected Successfully")

        clients_response = ApiResponse()

        response = clients_response.set_status_code(200).set_data('message', 'Hardware connected successfully').get()

        
        self.enter_room(sid, namespace=HARDWARE_NAMESPACE,  room="myGreenhouse")
        self.emit('hardware_connection', response, namespace=WEB_NAMESPACE,  room="myGreenhouse")
        self.emit('hardware_connection', response, namespace=MOBILE_NAMESPACE, room="myGreenhouse")


    def on_sensors_values(self, sid, data):
        print("Hardware Sent Sensor Values Successfully")

        api_response = ApiResponse()

        serializer = StoreSensorValuesSerializer(data=data)

        if not serializer.is_valid():
            print(serializer.errors)
            response = api_response.set_status_code(status.HTTP_400_BAD_REQUEST).set_data("errors", serializer.errors).get()
            self.emit('send_sensor_values_status', response, namespace=HARDWARE_NAMESPACE, room="myGreenhouse")

        else:
            print("Successfully ya mega")
            sensor_values = serializer.save()
            print(sensor_values)
            api_response.set_status_code(status.HTTP_200_OK).set_data("sensors", SensorValueSerializer(sensor_values, many=True).data)

            response = api_response.get()
            
        self.emit('sensors_values', response, namespace=WEB_NAMESPACE,  room='myGreenhouse')
        self.emit('sensors_values', response, namespace=MOBILE_NAMESPACE,  room='myGreenhouse')

    def on_disconnect(self, sid):
        print("Hardware Disconnected")

        api_response = ApiResponse()

        response = api_response.set_status_code(status.HTTP_501_NOT_IMPLEMENTED).set_data(
            'message', 'Hardware disconnected').get()

        self.emit('hardware_connection', response, namespace=WEB_NAMESPACE,  room='myGreenhouse')
        self.emit('hardware_connection', response, namespace=MOBILE_NAMESPACE,  room='myGreenhouse')


