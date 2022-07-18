from rest_framework import serializers
from users.models import User
from django.contrib.auth.hashers import make_password
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
    