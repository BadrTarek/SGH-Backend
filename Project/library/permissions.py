from sys import api_version
from rest_framework.permissions import BasePermission
from iot.models import Product
from rest_framework import exceptions
from .api_response import ApiResponse
from rest_framework import status

class HasProduct(BasePermission):
    def has_permission(self, request, view):
        
        has_product = Product.objects.filter(user = request.user , is_active = True).exists()
        
        if not has_product:
            api_response = ApiResponse()
            
            response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("message","Undefind any product configured with this account").get()
            
            raise exceptions.PermissionDenied(response)    
            
        return has_product
    
    
class IsProductAuthenticated(BasePermission):
    def has_permission(self, request, view):
        api_response = ApiResponse()
        if "Token" in request.headers.keys():
            if request.headers["Token"] is not None:

                token = request.headers["Token"]
                is_loggedin = Product.objects.filter(token=token).exists()
                
                if is_loggedin:
                    return is_loggedin
        
        response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("message","Not authenticated").get()
        raise exceptions.PermissionDenied(response)  
    