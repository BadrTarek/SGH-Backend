from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from Library.permissions import HasGreenhouse
from .models import Plant
from rest_framework.response import Response
from .serializers import PlantsSerializer
from Library.api_response import ApiResponse

from rest_framework import status

# Create your views here.

api_response = ApiResponse()

class SupportedPlantsView(APIView):
    
    permission_classes = [ IsAuthenticated &  HasGreenhouse ]

    def get(self , request):

        api_response.__init__()

        plants = Plant.objects.filter(is_supported = True)
        
        if len(plants) == 0:
            return api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("message", "There are no supported plants right now").response()

        
        serializer = PlantsSerializer(plants , many = True)
        
        return api_response.set_status_code(status.HTTP_200_OK ).set_data("planys", serializer.data).response()

