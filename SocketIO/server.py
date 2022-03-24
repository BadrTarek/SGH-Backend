import os
import socketio
from .clients import hardware , web , mobile
from .socketio_server_settings import HARDWARE_NAMESPACE, WEB_NAMESPACE, MOBILE_NAMESPACE
basedir = os.path.dirname(os.path.realpath(__file__))

sio = socketio.Server(async_mode=None  ,cors_allowed_origins = '*' , logger=True, engineio_logger=True)

thread = None   

    
sio.register_namespace(hardware.HardwareNamespace(HARDWARE_NAMESPACE))
sio.register_namespace(web.WebNamespace(WEB_NAMESPACE))
sio.register_namespace(mobile.MobileNamespace(MOBILE_NAMESPACE))



