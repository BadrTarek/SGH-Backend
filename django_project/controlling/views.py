from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from library.permissions import HasProduct , IsProductAuthenticated
from rest_framework import status
from .requests_serializers import TakeActionSerializer,  GetActionsSerializer
from .models_serializers import ActuatorSerializer,ActuatorActionsSerializer
from library.api_response import ApiResponse
from library.helper import print_error_in_console

api_response = ApiResponse()


class TakeAcionView(APIView):
    permission_classes = [IsAuthenticated & HasProduct  ]

    def post(self , request):
        api_response.__init__()

        serializer = TakeActionSerializer(data = request.data)
        if not serializer.is_valid():
            print_error_in_console("Take Action Request",serializer.errors)
            return api_response.set_status_code(status.HTTP_400_BAD_REQUEST).merge_dict(serializer.errors).response()

        action = serializer.save()

        api_response.set_status_code(status.HTTP_200_OK)
        api_response.set_data("action",ActuatorActionsSerializer(action).data)

        return api_response.response()




class GeAllActionsView(APIView):
    permission_classes = [IsAuthenticated & HasProduct]

    def get(self , request , id ):
        api_response.__init__()

        serializer = GetActionsSerializer(data=request.data,context={
            'product_id':id,
            'user':request.user
        })

        if not serializer.is_valid():
            print_error_in_console("Get All Actions Request",serializer.errors)
            return api_response.set_status_code(status.HTTP_400_BAD_REQUEST).merge_dict(serializer.errors).response()


        actions = serializer.get_all_actions()

        api_response.set_status_code(status.HTTP_200_OK).set_data("actions",actions)

        return api_response.response()
