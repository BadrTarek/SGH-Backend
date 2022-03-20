from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
from rest_framework.authentication import authenticate
from rest_framework import status
from Library.api_response import ApiResponse
from rest_framework_simplejwt.tokens import RefreshToken , TokenError
from django_countries.serializers import CountryFieldMixin

class UserSerializer(CountryFieldMixin,serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'phone', 'image', 'country','date_joined']
        extra_kwargs = {
            'password': {'write_only': True},  # For not return the password
            'country': {'name_only':True}       # For return country name not code
        }

    def create(self, validated_data) -> User:
        user = User.objects.create(
            email = validated_data['email'],
            name = validated_data['name'],
            password = make_password(validated_data['password']),
            phone = validated_data['phone'],
            image = ( validated_data['image'] if "image" in validated_data else None ),
            country = validated_data['country']
        )
        return user


class UserLoginSerializer(serializers.Serializer) :

    email = serializers.EmailField()
    password = serializers.CharField(max_length=255 )

    
    def login(self) -> tuple :

        email = self.data["email"]
        password = self.data["password"]
        
        api_response = ApiResponse()

        user = authenticate(email=email, password=password)

        if user is None:
            response = api_response.set_status_code(status.HTTP_400_BAD_REQUEST).set_data(
                "message", 'A user with this email and password is not found.').get()
            raise serializers.ValidationError(detail=response)

        refresh = RefreshToken.for_user(user)

        return (
            UserSerializer(user).data,
            str(refresh) ,
            str(refresh.access_token)
        )


class UserLogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(write_only = True)

    def validate(self , data):
        self.token = data['refresh']
        return data
        
    def save(self,**kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            api_response = ApiResponse()
            response = api_response.set_status_code(status.HTTP_401_UNAUTHORIZED).set_data(
                "message", "Token is invalid or expired" ).get()
            raise serializers.ValidationError(detail=response)
