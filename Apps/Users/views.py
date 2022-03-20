from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer, UserLoginSerializer , UserLogoutSerializer
from Library.api_response import ApiResponse
from rest_framework import status 

# Create your views here.

api_response = ApiResponse()



class RegisterView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        api_response.__init__()

        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return api_response.set_status_code(status.HTTP_400_BAD_REQUEST).set_data("errors", serializer.errors).response()

        user = serializer.save()

        login_serializer =  UserLoginSerializer(data = request.data)
        
        if not login_serializer.is_valid():
            user.delete()
            return api_response.set_status_code(status.HTTP_501_NOT_IMPLEMENTED).set_data("message","Unexpected error please try again later").response()
        
        user , refresh , token = login_serializer.login()
        
        return api_response.set_status_code(status.HTTP_200_OK).set_data( "user",user).set_data("refresh",refresh).set_token(token).response()


class LoginView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        api_response.__init__()

        serializer = UserLoginSerializer(data = request.data)
        
        if not serializer.is_valid():
            print(serializer.errors)
            return api_response.set_status_code(status.HTTP_400_BAD_REQUEST).set_data("errors", serializer.errors).response()

        user , refresh , token = serializer.login()

        return api_response.set_status_code(status.HTTP_200_OK).set_data( "user", user).set_data("refresh",refresh).set_token(token).response()


class LogoutView(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]   
    
    def get(self, request):        
        api_response.__init__()
        
        serializer = UserLogoutSerializer(data = request.data)
        
        if not serializer.is_valid():
            return api_response.set_status_code(status.HTTP_400_BAD_REQUEST).set_data("errors", serializer.errors).response()

        serializer.save()
        
        
        return api_response.set_status_code(status.HTTP_200_OK).set_data("message", "Logged out successfully").response()



