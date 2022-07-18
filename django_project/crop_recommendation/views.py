from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from library.api_response import ApiResponse
from library.helper import print_error_in_console
from rest_framework import status
from .serializers import CropSuggestionSerializer, CropsSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

api_response = ApiResponse()


class CropRecommendationsView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, product_id):
        api_response.__init__()

        serializer = CropSuggestionSerializer(data=request.data, context={
            'request': request,
            'product_id': product_id
        })

        if not serializer.is_valid():
            print_error_in_console("Error in Crop Suggestion Request", serializer.errors)
            return api_response.set_status_code(status.HTTP_400_BAD_REQUEST).merge_dict(serializer.errors).response()

        response = CropsSerializer(serializer.save()).data

        return api_response.set_status_code(status.HTTP_200_OK).merge_dict(response).response()

