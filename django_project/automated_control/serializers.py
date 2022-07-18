from rest_framework import serializers
from products.validations import is_allow_automated_control
from controlling.models import ActuatorsAction
from .models import MODELS
from .validations import check_date_for_actuators
from controlling.models_serializers import ActuatorActionsSerializer
from library.api_response import ApiResponse


# def product_sensor_validation(sensor_id: int, product_id:int , raise_exception:bool = True):


class TakeAutomatedActionSerializer(serializers.Serializer):
    # Token instead of id,password
    product_id = serializers.IntegerField()
    password = serializers.CharField()

    def validate(self, data):

        # check date

        self.product = is_allow_automated_control(data["product_id"], data["password"])

        self.actions = []

        for model in MODELS:
            model = model(self.product)

            if not check_date_for_actuators(self.product, model.actuators):
                continue

            model_actions = model.get_actions()

            if not model_actions:
                continue

            self.actions += model_actions

        if self.actions == []:
            api_response = ApiResponse()
            response = api_response.set_data("errors", "No Automated Actions Can apply now ").get()
            raise serializers.ValidationError(detail=response)

        # Extra validations : validate that the sensors & actuators integrate with the product

        return data

    def save(self, **kwargs):
        results = []
        for action in self.actions:
            results.append(ActuatorActionsSerializer(ActuatorsAction.objects.create(
                value=action["value"],
                duration=action["duration"],
                actuator=action["actuator"],
                product=self.product,
                is_automated_action=True)
            ).data)

        return results

# {
#     "status_code": 200,
#     "action": {
#         "value": "10",
#         "duration": "10",
#         "created_at": "2022-04-28T01:44:40.397415",
#         "actuator": 1,
#         "is_automated_action": false
#     }
# }
