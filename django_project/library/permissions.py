from rest_framework.permissions import BasePermission
from products.models import Product
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
        try:
            if "AUTHORIZATION" in request.headers.keys():
                if request.headers["AUTHORIZATION"] is not None:

                    # token = (request.headers["AUTHORIZATION"]).split(" ")[1]
                    token = request.headers["AUTHORIZATION"]

                    is_loggedin = Product.objects.filter(token=token).exists()

                    if is_loggedin:
                        return is_loggedin
        except:
            api_response = ApiResponse()
            response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("message","Not auعthenticated").get()
            raise exceptions.PermissionDenied(response)
