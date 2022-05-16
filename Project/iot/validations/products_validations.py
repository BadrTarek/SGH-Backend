from ..models import Product, ProductActuator, ProductSensor
from ..models import Sensor, Actuator
from rest_framework import serializers 
from library.api_response import ApiResponse


def product_validation(id:int , password:str , raise_exception:bool = True):
    try:

        Product.objects.get(pk=id, password=password , is_active = True)
        return True
    except Product.DoesNotExist:
        if raise_exception:
            api_response = ApiResponse()
            response = api_response.set_data("errors", "A product with this ID and password is not found.").get()
            raise serializers.ValidationError(detail=response)
    return False



def product_sensor_validation(sensor_id: int, product_id:int , raise_exception:bool = True):
    try:
        sensor = Sensor.objects.get(pk = sensor_id)
        product = Product.objects.get(pk = product_id)
        ProductSensor.objects.get(sensor=sensor, product=product)
        return True
    except (ProductSensor.DoesNotExist , Sensor.DoesNotExist , Product.DoesNotExist):
        if raise_exception:
            api_response = ApiResponse()
            response = api_response.set_data("errors", "This sensor not integrated with this product or not exist").get()
            raise serializers.ValidationError(detail=response)
    return False



def product_actuator_validation(actuator_id: int, product_id:int , raise_exception:bool = True):
    try:
        actuator = Actuator.objects.get(pk = actuator_id)
        product = Product.objects.get(pk = product_id)
        ProductActuator.objects.get(actuator=actuator, product=product)
        return True
    except (ProductActuator.DoesNotExist , Actuator.DoesNotExist , Product.DoesNotExist):
        if raise_exception:
            api_response = ApiResponse()
            response = api_response.set_data("errors", "This actuator not integrated with this product or not exist").get()
            raise serializers.ValidationError(detail=response)  
    return False



def is_allow_automated_control(id:int , password:str, raise_exception:bool = True ):
    try:
        Product.objects.get(pk=id, password=password , is_active = True, automated_control=True)
        return True
    except (Product.DoesNotExist):
        if not raise_exception:
            return False
        api_response = ApiResponse()
        response = api_response.set_data("errors", "Cannot apply automated control.").get()
        raise serializers.ValidationError(detail=response)
    
    # if not product.automated_control:
    #     if raise_exception:
    #         api_response = ApiResponse()
    #         response = api_response.set_data("errors", "Cannot apply automated control.").get()
    #         raise serializers.ValidationError(detail=response)
    #     return False
    
    # return True