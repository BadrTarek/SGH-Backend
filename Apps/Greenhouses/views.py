from rest_framework.views import APIView 
from rest_framework.permissions import IsAuthenticated
from Library import permissions 
from Library.permissions import HasGreenhouse , IsGreenhouseAuthenticated
from Apps.Greenhouses.models import Greenhouse
from .serializers import GreenhouseSerializers, ConfigureGreenhouseSerializer, GetUserGreenhouseSerializer  , GreenhouseAuthSerializer
from Library.api_response import ApiResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
api_response = ApiResponse()


class ConfigureGreenhouseView(APIView):
    permission_class = [IsAuthenticated]

    def post(self, request):

        api_response.__init__()

        serializer = ConfigureGreenhouseSerializer(data=request.data, context={'request': request})

        if not serializer.is_valid():
            return Response(serializer.errors)

        greenhouse = GreenhouseSerializers(serializer.save()).data

        return api_response.set_status_code(status.HTTP_200_OK).set_data("greenhouse", greenhouse).set_data("message",  f"The greenhouse with ID [ {greenhouse.get('id')} ] is configured successfully").response()


class GetUserGreenhousesView(APIView):
    permission_classes = [  HasGreenhouse & IsAuthenticated]

    def get(self, request , id = None):
        
        api_response.__init__()

        serializer = GetUserGreenhouseSerializer(data = request.data ,  context={'request':request , 'id':id} )
        
        if not serializer.is_valid():
            return Response(serializer.errors)
        
        greenhouses = GreenhouseSerializers( serializer.save() , many=True ).data
        
        return api_response.set_status_code(status.HTTP_200_OK).set_data("greenhouses", greenhouses).response()
    

class UpdateGreenhouseView(APIView):
    permission_classes = [ IsAuthenticated & HasGreenhouse]

    def post(self, request , id):
        api_response.__init__()

        try:
            greenhouse = Greenhouse.objects.get( pk = id, user = self.request.user , is_active = True)
        except Greenhouse.DoesNotExist:
            return api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("message", "This greenhouse not found").response()
        
            
        serializer = GreenhouseSerializers(instance = greenhouse ,  data = request.data , context={'request':request , 'id':id} ,  partial=True)
        
        if not serializer.is_valid():
            return api_response.set_status_code(status.HTTP_400_BAD_REQUEST).set_data("errors", serializer.errors).response()
        
        greenhouse = serializer.save()
        
        return api_response.set_status_code(status.HTTP_200_OK).set_data("message","Updated successfully").set_data("greenhouse", serializer.data).response()


class GreenhouseLoginView(APIView):

    def post(self , request):
    
        serializer = GreenhouseAuthSerializer(data = request.data)
        if not serializer.is_valid():
            return api_response.set_status_code(status.HTTP_400_BAD_REQUEST).set_data("errors", serializer.errors).response()
        
        greenhouse , token = serializer.login()
        
        return api_response.set_status_code(status.HTTP_200_OK ).set_data("greenhouse", GreenhouseSerializers(greenhouse).data).set_data("token",token).response()


class GreenhouseLogoutView(APIView):

    permission_classes = [ IsGreenhouseAuthenticated ]

    def get(self , request):
        api_response.__init__()
        
        token = request.headers["Token"]
        greenhouse = Greenhouse.objects.get(token=token)
        greenhouse.token = None
        greenhouse.save()

        return api_response.set_status_code(status.HTTP_200_OK ).set_data("message", "Loggedout successfully").response()
