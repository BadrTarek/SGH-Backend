from .models import Product
from rest_framework import serializers
from library.api_response import ApiResponse
from rest_framework import status
import jwt
import datetime
from .validations import product_validation, product_user_validation, product_token_validation
# from notification.models import SMSVonageNotification, EmailNotification


class ConfigureProductSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    password = serializers.CharField(max_length=10)

    def validate(self, data):
        self.product = product_validation(data["product_id"], data["password"])

        if self.product.user != None:
            api_response = ApiResponse()
            response = api_response.set_data("errors", "Invalid inputs, please enter valid ID and password.").get()
            raise serializers.ValidationError(response)

        return data

    def save(self, **kwargs):
        self.product.user = self.context["request"].user
        self.product.save()
        return self.product


class GetUserProductSerializer(serializers.Serializer):

    def validate(self, data):

        if self.context["id"] is not None:
            self.product = product_user_validation(self.context["id"], user=self.context["request"].user)

            # try:
            #     Product.objects.get( pk=self.context["id"], user=self.context["request"].user , is_active = True)

            # except Product.DoesNotExist:
            #     api_response = ApiResponse()
            #     response = api_response.set_data("errors", "This product not found").get()
            #     raise serializers.ValidationError(detail=response)

        return data

    def save(self, **kwargs):

        if self.context["id"] is not None:
            return self.product

        product = Product.get_user_products(self.context["request"].user)

        return product


class ProductAuthSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    password = serializers.CharField(max_length=10)

    def validate(self, data):
        self.product = product_validation(data["product_id"], data["password"])

        return data

    def login(self):
        payload = {
            'id': self.product.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=360),
            'iat': datetime.datetime.utcnow(),
        }
        token = jwt.encode(payload, "secret", algorithm="HS256")

        self.product.token = token
        self.product.save()

        return (self.product, token)

#
# # SMSVonageNotification, EmailNotification
# class FireSerializer(serializers.Serializer):
#
#     def validate(self, data):
#         self.product = product_token_validation(self.context["token"])
#
#         return data
#
#     def send_mail(self):
#         mail = EmailNotification()
#         mail.send_mail(to=self.product.user.email, subject="Fire Alarm", message="""""
#             Help !!!!!!!!!!
#             Help !!!!!!!!!!
#
#             System sensors detected a fire next to the greenhouse, please intervene immediately so as not to damage the agriculture
#
#
#         """)
#         return True
#
#     def send_sms(self):
#         sms = SMSVonageNotification()
#         sms.send_message("""
#             Help !!!!!!!!!!
#             Help !!!!!!!!!!
#
#             System sensors detected a fire next to the greenhouse, please intervene immediately so as not to damage the agriculture
#
#
#         """)
