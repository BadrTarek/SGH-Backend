from .models import Actuator, ActuatorsAction
from rest_framework import serializers
from products.validations import product_user_validation,product_validation
from .validations import actuator_validation
from .models_serializers import ActuatorActionsSerializer


class TakeActionSerializer(serializers.Serializer):

    product_id = serializers.IntegerField()
    password = serializers.CharField()
    actuator_id = serializers.IntegerField()
    value = serializers.CharField()
    duration = serializers.CharField(required=False, allow_null=True)

    def validate(self, data):
        self.product = product_validation(data["product_id"],data["password"])
        self.actuator = actuator_validation(data["actuator_id"])

        return data

    def save(self,  **kwargs):

        action = ActuatorsAction.objects.create(
            actuator=self.actuator,
            product=self.product,
            value=self.data["value"],
            duration=self.data["duration"]
        )

        return action




class GetActionsSerializer(serializers.Serializer):

    # product_id = serializers.IntegerField()
    # password = serializers.CharField(max_length=10)

    def validate(self, data):

        self.product = product_user_validation(product_id = self.context["product_id"],user= self.context["user"])

        # self.product_actuators = ProductActuator.get_product_actuators(self.product)

        return data


    def get_all_actions(self):

        actions = ActuatorsAction.objects.filter(product =self.product)
        # for product_actuator in self.product_actuators:
        #     action = ActuatorsAction.get_all_actuator_actions(self.product,product_actuator.actuator)
        #     actions.append(ActuatorActionsSerializer(action , many=True).data)

        return ActuatorActionsSerializer(actions , many=True).data
