from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import TakeAutomatedActionSerializer
from library.helper import print_error_in_console
from library.api_response import ApiResponse
from rest_framework import status
from library.permissions import IsProductAuthenticated


class TakeAutomatedAction(APIView):
    permission_classes = [IsProductAuthenticated]

    def post(self, request):
        api_response = ApiResponse()

        serializer = TakeAutomatedActionSerializer(data=request.data)

        if not serializer.is_valid():
            print_error_in_console("Take Automated Action Request", serializer.errors)
            return api_response.set_status_code(status.HTTP_400_BAD_REQUEST).merge_dict(serializer.errors).response()

        actions = serializer.save()

        return api_response.set_status_code(status.HTTP_200_OK).set_data("actions", actions).response()

# Create your views here.
