from .models import Product
from rest_framework import serializers
from library.api_response import ApiResponse
from users.models import User


def product_validation(id: int, password: str, raise_exception: bool = True):
    try:
        return Product.objects.get(pk=id, password=password, is_active=True)
    except Product.DoesNotExist:
        if raise_exception:
            api_response = ApiResponse()
            response = api_response.set_data("errors", "A product with this ID and password is not found.").get()
            raise serializers.ValidationError(detail=response)
    return False


def product_token_validation(token: str, raise_exception: bool = True):
    try:
        return Product.objects.get(token=token, is_active=True)
    except Product.DoesNotExist:
        if raise_exception:
            api_response = ApiResponse()
            response = api_response.set_data("errors", "A product with this Token is not found.").get()
            raise serializers.ValidationError(detail=response)
    return False


def product_user_validation(product_id: int, user: User, raise_exception: bool = True):
    try:
        return Product.objects.get(pk=product_id, user=user, is_active=True)
    except Product.DoesNotExist:
        if raise_exception:
            api_response = ApiResponse()
            response = api_response.set_data("errors", "This product not configured with you").get()
            raise serializers.ValidationError(detail=response)
    return False

#
# def product_sensor_validation(sensor_id: int, product_id: int, raise_exception: bool = True):
#     try:
#         sensor = Sensor.objects.get(pk=sensor_id)
#         product = Product.objects.get(pk=product_id)
#         return ProductSensor.objects.get(sensor=sensor, product=product)
#     except (ProductSensor.DoesNotExist, Sensor.DoesNotExist, Product.DoesNotExist):
#         if raise_exception:
#             api_response = ApiResponse()
#             response = api_response.set_data("errors",
#                                              "This sensor not integrated with this product or not exist").get()
#             raise serializers.ValidationError(detail=response)
#     return False
#
#
# def product_actuator_validation(actuator_id: int, product_id: int, raise_exception: bool = True):
#     try:
#         actuator = Actuator.objects.get(pk=actuator_id)
#         product = Product.objects.get(pk=product_id)
#         return ProductActuator.objects.get(actuator=actuator, product=product)
#     except (ProductActuator.DoesNotExist, Actuator.DoesNotExist, Product.DoesNotExist):
#         if raise_exception:
#             api_response = ApiResponse()
#             response = api_response.set_data("errors",
#                                              "This actuator not integrated with this product or not exist").get()
#             raise serializers.ValidationError(detail=response)
#     return False


def is_allow_automated_control(id: int, password: str, raise_exception: bool = True):
    try:
        return Product.objects.get(pk=id, password=password, is_active=True, automated_control=True)
    except (Product.DoesNotExist):
        if not raise_exception:
            return False
        api_response = ApiResponse()
        response = api_response.set_data("errors", "Cannot apply automated control.").get()
        raise serializers.ValidationError(detail=response)

