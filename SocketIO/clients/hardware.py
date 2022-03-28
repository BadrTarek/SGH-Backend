from numpy import empty
from Apps.Hardware.requests import store_sensors_values_with_fuzzy
import socketio
from Library.api_response import ApiResponse
from rest_framework import status
from SocketIO.socketio_server_settings import HARDWARE_NAMESPACE, WEB_NAMESPACE, MOBILE_NAMESPACE
from Apps.Hardware.serializers.models_serializers import ActuatorActionsSerializer

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

        actions , response = store_sensors_values_with_fuzzy(data)
        if actions:
            for action in actions:
                api_response = ApiResponse()
                api_response.set_status_code(status.HTTP_200_OK)
                action_reponse = api_response.set_data("action",ActuatorActionsSerializer(action).data).get()
                self.emit('take_action', action_reponse, namespace=HARDWARE_NAMESPACE,  room='myGreenhouse')
            
        self.emit('sensors_values', response, namespace=WEB_NAMESPACE,  room='myGreenhouse')
        self.emit('sensors_values', response, namespace=MOBILE_NAMESPACE,  room='myGreenhouse')

    def on_disconnect(self, sid):
        print("Hardware Disconnected")

        api_response = ApiResponse()

        response = api_response.set_status_code(status.HTTP_501_NOT_IMPLEMENTED).set_data(
            'message', 'Hardware disconnected').get()

        self.emit('hardware_connection', response, namespace=WEB_NAMESPACE,  room='myGreenhouse')
        self.emit('hardware_connection', response, namespace=MOBILE_NAMESPACE,  room='myGreenhouse')


