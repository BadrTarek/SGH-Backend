from os import stat
from rest_framework.views import exception_handler
from rest_framework.exceptions import AuthenticationFailed , NotAuthenticated
from library.api_response import ApiResponse
from rest_framework import status


api_response = ApiResponse()

def custom_exception_handler(exc, context):
    # to get the standard error response.
    response = exception_handler(exc, context)

    if isinstance(exc, AuthenticationFailed):  
        response.data = api_response.set_status_code(status.HTTP_401_UNAUTHORIZED).set_data("message","Token is invalid or expired").get()
        
    if isinstance(exc, NotAuthenticated):  
        response.data = api_response.set_status_code(status.HTTP_403_FORBIDDEN).set_data("message","Not authenticated").get()

    return response