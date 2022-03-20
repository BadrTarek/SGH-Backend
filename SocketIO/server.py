import os
import socketio
from .clients import hardware , web , mobile

basedir = os.path.dirname(os.path.realpath(__file__))

sio = socketio.Server(async_mode=None  ,cors_allowed_origins = '*' , logger=True, engineio_logger=True)

thread = None   

    
sio.register_namespace(hardware.HardwareNamespace('/hardware'))
sio.register_namespace(web.WebNamespace('/web'))
sio.register_namespace(mobile.MobileNamespace('/mobile'))



