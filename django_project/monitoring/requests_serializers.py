from .models import Sensor, SensorValues
from rest_framework import serializers
from products.validations import product_validation
from .validations import sensor_validation




class SensorWithValueSerializer(serializers.Serializer):
    sensor_id = serializers.IntegerField()
    value = serializers.CharField()

class StoreSensorValuesSerializer(serializers.Serializer):
    # Token instead of id,password
    product_id = serializers.IntegerField()
    password = serializers.CharField()
    sensors = serializers.ListField(child = SensorWithValueSerializer())

    def validate(self, data):
        self.product = product_validation(data["product_id"] , data["password"])
        for sensor in data["sensors"]:
            sensor_validation(id = sensor['sensor_id'],value = sensor["value"])
        return data

    def save(self,**kwargs):

        self.sensor_values_response = []

        for sensor in self.data["sensors"]:
            my_sensor = Sensor.get_sensor(sensor['sensor_id'])
            sensor_value = SensorValues()
            sensor_value.product=self.product
            sensor_value.sensor=my_sensor
            sensor_value.value=sensor["value"]
            sensor_value.save()

            self.sensor_values_response.append(sensor_value)

        return self.sensor_values_response


class GetSensorValuesSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    password = serializers.CharField(max_length=10)
    sensor_id = serializers.IntegerField(required=False, allow_null=True)

    def validate(self, data):
        self.product = product_validation(data["product_id"] ,data["password"] )

        return data

    def get_all_values(self):
        # self.product = Product.get_product(self.data["product_id"] ,self.data["password"])
        self.sensor = Sensor.get_sensor(self.data["sensor_id"])
        # return SensorValues.get_all_sensor_values(self.product, self.sensor)

        return SensorValues.objects.values_list('value').filter(product =  self.product ,sensor = self.sensor)
