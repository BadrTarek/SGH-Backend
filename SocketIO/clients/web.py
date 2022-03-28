import socketio
from Library.api_response import ApiResponse
from rest_framework import status
from Apps.Hardware.serializers.requests_serializers import TakeActionSerializer 
from Apps.Hardware.serializers.models_serializers import  ActuatorActionsSerializer
from Library.api_response import ApiResponse
from rest_framework import status
from SocketIO.socketio_server_settings import HARDWARE_NAMESPACE, WEB_NAMESPACE, MOBILE_NAMESPACE



#------------------------------------------------------ Frontend Client
class WebNamespace(socketio.Namespace):
    
    def on_connect(self, sid, environ):
        print("Web Connected Successfully")
        api_response = ApiResponse()
        response = api_response.set_status_code(200).set_data('message','Connected to server successfully').get()
        self.enter_room(sid, 'myGreenhouse' , namespace=WEB_NAMESPACE)
        self.emit('connection_status', response , room="myGreenhouse" , namespace=WEB_NAMESPACE)
        
    def on_take_action(self,sid,data):
        
        serializer = TakeActionSerializer(data = data)
        if not serializer.is_valid():
            api_response = ApiResponse()
            errors_response = api_response.set_status_code(status.HTTP_400_BAD_REQUEST).set_data("errors" , serializer.errors).get()
            self.emit('take_action_status' , errors_response ,room="myGreenhouse",namespace=WEB_NAMESPACE)
        else:
            
            api_response = ApiResponse()
            action = serializer.save()
            api_response.set_status_code(status.HTTP_200_OK)
            api_response.set_data("action",ActuatorActionsSerializer(action).data)
            

            response = api_response.set_status_code(200).get()
            print(response)
            
            self.emit('take_action', response  ,room='myGreenhouse', namespace=HARDWARE_NAMESPACE)
            self.emit('action_taked', response  ,room='myGreenhouse', namespace=MOBILE_NAMESPACE)

    
    def on_disconnect(self, sid):
        print("Web Disconnected")
    



