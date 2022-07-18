from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.models_serializers import UserSerializer
from users.requests_serializers import UserLoginSerializer, UserLogoutSerializer
from library.api_response import ApiResponse
from library.helper import print_error_in_console
from rest_framework import status
from rest_framework.authentication import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

api_response = ApiResponse()


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        api_response.__init__()

        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            print_error_in_console("Register Request", serializer.errors)
            return api_response.set_status_code(status.HTTP_400_BAD_REQUEST).merge_dict(serializer.errors).response()

        serializer.save()

        return api_response.success_response("Registered successfully")


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        api_response.__init__()
        print(request.data)
        serializer = UserLoginSerializer(data=request.data)

        if not serializer.is_valid():
            print_error_in_console("Login Request", serializer.errors)
            return api_response.set_status_code(status.HTTP_400_BAD_REQUEST).merge_dict(serializer.errors).response()

        data = serializer.validated_data

        user, refresh, token = self.login(data["email"], data["password"])

        return api_response.set_status_code(status.HTTP_200_OK).set_data("user", user).set_data("refresh",
                                                                                                refresh).set_token(
            token).response()

    def login(self, email, password) -> tuple:
        user = authenticate(email=email, password=password)

        refresh = RefreshToken.for_user(user)

        return (
            UserSerializer(user).data,
            str(refresh),
            str(refresh.access_token)
        )


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        api_response.__init__()

        serializer = UserLogoutSerializer(data=request.data)

        if not serializer.is_valid():
            print_error_in_console("Logout Request", serializer.errors)
            return api_response.set_status_code(status.HTTP_400_BAD_REQUEST).merge_dict(serializer.errors).response()

        data = serializer.validated_data

        self.logout(data["refresh"])

        return api_response.success_response("Logged out successfully")

    def logout(self, token):
        RefreshToken(token).blacklist()


