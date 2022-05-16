from rest_framework.views import APIView 
from rest_framework.permissions import IsAuthenticated
from library.permissions import HasProduct , IsProductAuthenticated
from ..models import Product 
from ..serializers.models_serializers import ProductSerializers
from ..serializers.product_requests_serializers import ConfigureProductSerializer, GetUserProductSerializer  , ProductAuthSerializer
from library.api_response import ApiResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from library.helper import print_error_in_console


api_response = ApiResponse()


class ConfigureProductView(APIView):
    permission_class = [IsAuthenticated]

    def post(self, request):

        api_response.__init__()

        serializer = ConfigureProductSerializer(data=request.data, context={'request': request})

        if not serializer.is_valid():
            print_error_in_console("Store Sensor Values Request",serializer.errors)
            return api_response.set_status_code(status.HTTP_400_BAD_REQUEST).merge_dict(serializer.errors).response()

        product = ProductSerializers(serializer.save()).data

        return api_response.set_status_code(status.HTTP_200_OK).set_data("product", product).set_data("message",  f"The product with ID [ {product.get('id')} ] is configured successfully").response()


class GetUserProductsView(APIView):
    permission_classes = [ HasProduct & IsAuthenticated]

    def get(self, request , id = None):
        
        api_response.__init__()

        serializer = GetUserProductSerializer(data = request.data ,  context={'request':request , 'id':id} )
        
        if not serializer.is_valid():
            print_error_in_console("Store Sensor Values Request",serializer.errors)
            return api_response.set_status_code(status.HTTP_400_BAD_REQUEST).merge_dict(serializer.errors).response()

        products = ProductSerializers( serializer.save() , many=True ).data
        
        return api_response.set_status_code(status.HTTP_200_OK).set_data("products", products).response()
    

class UpdateProductView(APIView):
    permission_classes = [ IsAuthenticated & HasProduct]

    def post(self, request , id):
        api_response.__init__()

        try:
            product = Product.objects.get( pk = id, user = self.request.user , is_active = True)
        except Product.DoesNotExist:
            return api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("message", "This product not found").response()
        
            
        serializer = ProductSerializers(instance = product ,  data = request.data , context={'request':request , 'id':id} ,  partial=True)
        
        if not serializer.is_valid():
            print_error_in_console("Store Sensor Values Request",serializer.errors)
            return api_response.set_status_code(status.HTTP_400_BAD_REQUEST).merge_dict(serializer.errors).response()
        
        product = serializer.save()
        
        return api_response.set_status_code(status.HTTP_200_OK).set_data("message","Updated successfully").set_data("product", serializer.data).response()


class ProductLoginView(APIView):
    permission_classes = [ AllowAny ]

    def post(self , request):
    
        serializer = ProductAuthSerializer(data = request.data)
        if not serializer.is_valid():
            print_error_in_console("Store Sensor Values Request",serializer.errors)
            return api_response.set_status_code(status.HTTP_400_BAD_REQUEST).merge_dict(serializer.errors).response()
        
        product , token = serializer.login()
        
        return api_response.set_status_code(status.HTTP_200_OK ).set_data("product", ProductSerializers(product).data).set_data("token",token).response()


class ProductLogoutView(APIView):

    permission_classes = [ IsProductAuthenticated ]

    def get(self , request):
        api_response.__init__()
        
        token = request.headers["Token"]
        product = Product.objects.get(token=token)
        product.token = None
        product.save()

        return api_response.set_status_code(status.HTTP_200_OK ).set_data("message", "Loggedout successfully").response()

