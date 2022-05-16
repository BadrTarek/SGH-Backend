from rest_framework import serializers
from library.api_response import ApiResponse
from ..models import User
from rest_framework.authentication import authenticate


class UserLoginSerializer(serializers.Serializer) :

    email = serializers.EmailField()
    password = serializers.CharField(max_length=255 )

    def validate(self, data):
        
        # try:
        #     authenticate(email=data['email'], password=data['password'])
        # except User.DoesNotExist:
        #     api_response = ApiResponse()
        #     response = api_response.set_data(
        #         "errors", 'A user with this email and password is not found.').get()
        #     raise serializers.ValidationError(detail=response)
        if not authenticate(email=data['email'], password=data['password']):
            api_response = ApiResponse()
            response = api_response.set_data(
                    "errors", 'A user with this email and password is not found.').get()
            raise serializers.ValidationError(detail=response)
        return data


class UserLogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(write_only = True)
