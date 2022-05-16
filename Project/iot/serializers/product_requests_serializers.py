from ..models import Product 
from rest_framework import serializers
from library.api_response import ApiResponse
from rest_framework import status
import jwt
import datetime
from ..validations.products_validations import product_validation


class ConfigureProductSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    password = serializers.CharField(max_length=10)

    def validate(self, data):
        
        product_validation(data["id"],data["password"])
        
        self.product = Product.get_product(self.data["product_id"],self.data["password"])
        
        if self.product.user != self.context["request"].user:
            api_response = ApiResponse()    
            response = api_response.set_data("errors", "Invalid inputs, please enter valid ID and password.").get()
            raise serializers.ValidationError(response)

        return data

    def save(self,  **kwargs):
        product = self.product  
        product.user = self.context["request"].user
        product.save()
        return product


class GetUserProductSerializer(serializers.Serializer):    
    
    def validate(self, data):

        if self.context["id"] is not None:
            
            try:
                Product.objects.get( pk=self.context["id"], user=self.context["request"].user , is_active = True)

            except Product.DoesNotExist:
                api_response = ApiResponse()
                response = api_response.set_data("errors", "This product not found").get()
                raise serializers.ValidationError(detail=response)

                    
        return data
    
    def save(self , **kwargs):
        product = Product.get_user_products(self.context["request"].user)
        
        if self.context["id"] is not None:
            product = Product.objects.filter( pk=self.context["id"], user=self.context["request"].user , is_active = True)
            
        return product




class ProductAuthSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    password = serializers.CharField(max_length=10)
    
    def validate(self,data):
        
        try:
            self.product = Product.objects.get(pk=self.data["id"], password=self.data["password"] , is_active = True , user = not None, token = None)
        except Product.DoesNotExist:
            api_response = ApiResponse()
            response = api_response.set_data("errors", "Invalid id or password").get()
            raise serializers.ValidationError(detail=response) 
        
        return data
    
    def login(self):

        payload = {
            'id':  self.product.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(year=1),
            'iat': datetime.datetime.utcnow(),
        }
        token  = jwt.encode(payload,"secret",algorithm="HS256")

        self.product.token = token 
        self.product.save()
        
                
        return ( self.product , token)

