from iot.models import Product , Sensor, SensorValues
from rest_framework import serializers
from iot.validations.products_validations import is_allow_automated_control
from .fuzzy_logic_models.implementation import implements
from iot.models import Product
    
class TakeAutomatedActionSerializer(serializers.Serializer):
    # Token instead of id,password
    product_id = serializers.IntegerField()
    password = serializers.CharField()
            
    def validate(self, data):
        is_allow_automated_control(data["product_id"] , data["password"])
        
        # Extra validations : validate that the sensors & actuators integrate with the product
        return data

    def save(self,  **kwargs):
        product = Product.get_product(self.data["product_id"], self.data["password"])
        return implements(product)

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
# class AutomatedActionsSerializer(serializers.Serializer):
#     actions = ActuatorActionsSerializer(many=True)