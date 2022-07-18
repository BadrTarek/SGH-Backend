from rest_framework import serializers
from library.api_response import ApiResponse
from .required_sensors import SENSORS
from products.validations import product_user_validation
from .apps import CropRecommendationConfig
from monitoring.models import SensorValues, Sensor
from products.models import  Product


class CropPrecentageSerializer(serializers.Serializer):
    crop_name = serializers.CharField()
    precentage = serializers.CharField()


class CropsSerializer(serializers.Serializer):
    crops = serializers.ListField(child=CropPrecentageSerializer())


class CropSuggestionSerializer(serializers.Serializer):

    def validate(self, data):
        # self.product = product_user_validation(self.context["product_id"],self.context["request"].user)
        self.product = Product.objects.get(pk=self.context["product_id"])

        self.sensor_value = []
        for sensor in SENSORS:
            # ProductSensor
            sensor = Sensor.objects.get(pk=sensor.ID)
            sensor_value = SensorValues.get_last_sensor_values(self.product, sensor)
            if sensor_value:
                self.sensor_value.append(sensor_value.value)
            else:
                self.sensor_value.append(0)
        return data

    def save(self, **kwargs):
        model = CropRecommendationConfig.crop_suggestion_model
        print(self.sensor_value)

        return {"crops": model.prediction_as_list(
            model.predict(
                temperature=self.sensor_value[0],
                humidity=self.sensor_value[1],
                ph=self.sensor_value[2],
                rainfal=0,
            )
        )}

