"""
WSGI config for SGHProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SGHProject.settings')

application = get_wsgi_application()

# For Socket.io Settings


# from Apps.HardwareApp.views import sio
from SocketIO.server import sio
from SocketIO.socketio_server_settings import PORT

import socketio


application = socketio.WSGIApp(sio, application)

import eventlet
import eventlet.wsgi

eventlet.wsgi.server(eventlet.listen(('', PORT)), application)


