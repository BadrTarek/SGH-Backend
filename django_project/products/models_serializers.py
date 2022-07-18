from .models import Product
from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin


class ProductSerializers(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True},
            'user': {'write_only': True},
            'is_active': {'write_only': True},
            'token': {'write_only': True},
        }

        def update(self, product, validated_data):
            product.country = validated_data.get("country", product.country)
            product.automated_control = validated_data.get("automated_control", product.automated_control)
            product.time_between_automated_action = validated_data.get("time_between_automated_action",
                                                                       product.time_between_automated_action)
            product.save()

            return product