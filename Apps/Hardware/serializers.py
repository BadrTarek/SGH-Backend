from rest_framework import serializers
from Apps.Greenhouses.models import Greenhouse , GreenhouseActustor , GreenhouseSensor
from .models import Sensor , Actuator , ActuatorsAction , SensorValues  
from rest_framework import status
from Library.api_response import ApiResponse


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id','name','messure']
        


class ActuatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actuator
        fields = "__all__"
        fields = ['id','name','action']
        

class SensorValueSerializer(serializers.ModelSerializer):
    # sensor = SensorSerializer()
    class Meta:
        model = SensorValues
        fields = ["value","created_at","sensor"]


class ActuatorActionsSerializer(serializers.ModelSerializer):
    # actuator = ActuatorSerializer()
        
    class Meta:
        model = ActuatorsAction
        fields = ["value","duration","created_at","actuator"]


class StoreSensorValuesSerializer(serializers.Serializer):
    
    greenhouse_id = serializers.IntegerField()
    password = serializers.CharField()
    sensors = serializers.ListField()

    def validate(self, data):
        api_response = ApiResponse()

        try:
            self.greenhouse = Greenhouse.objects.get(pk = data["greenhouse_id"] , password = data["password"])
        except Greenhouse.DoesNotExist:
            response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("errors", "A greenhouse with this ID and password is not found.").get()
            raise serializers.ValidationError(detail=response)
        
        for sensor in data["sensors"]:
            try:
                my_sensor = Sensor.objects.get(pk = sensor['sensor_id']) 
                GreenhouseSensor.objects.get(sensor = my_sensor , greenhouse = self.greenhouse)
            
            except ( Sensor.DoesNotExist , GreenhouseSensor.DoesNotExist ):
                response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("errors", "This sensor not integrated with this greenhouse or not exist").get()
                raise serializers.ValidationError(detail=response)
            
        return data
        
    def save(self,  **kwargs):
        
        response = []
        for sensor in self.data["sensors"]:
            my_sensor = Sensor.objects.get(pk = sensor['sensor_id'])
            sensor_value = SensorValues.objects.create(
                greenhouse = self.greenhouse,
                sensor = my_sensor ,
                value = sensor["value"]
            )
            response.append(sensor_value)

        return response
    
    def get_greenhouse(self):
        return self.greenhouse


class GetSensorValuesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    password = serializers.CharField(max_length=10)
    
    def validate(self, data):
        api_response = ApiResponse()
        
        try:
            self.greenhouse = Greenhouse.objects.get(pk=data["id"], password=data["password"] , is_active = True)
        
        except Greenhouse.DoesNotExist:
            response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("errors", "A greenhouse with this ID and password is not found.").get()
            raise serializers.ValidationError(detail=response)    
        
        return self.greenhouse
        
    
    def get_last_values(self):

        greenhouse_sensors = GreenhouseSensor.objects.filter(greenhouse = self.greenhouse)
        
        values = []
                
        if greenhouse_sensors.exists():
            for greenhouse_sensor in greenhouse_sensors:
                sensor_values = SensorValues.objects.filter(sensor = greenhouse_sensor.sensor).order_by('-id')[0]
                values.append(SensorValueSerializer(sensor_values).data)
                
            return values
        api_response = ApiResponse()

        return api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("message", "Undefind").get()

    def get_all_values(self):

        greenhouse_sensors = GreenhouseSensor.objects.filter(greenhouse = self.greenhouse)
        
        values = []
        
        if greenhouse_sensors.exists():
        
            for greenhouse_sensor in greenhouse_sensors:
                sensor_values = SensorValues.objects.filter(sensor = greenhouse_sensor.sensor).order_by('-id')
                values.append(SensorValueSerializer(sensor_values, many = True).data )
                
            return values
        
        api_response = ApiResponse()

        return api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("message", "Undefind").get()


class TakeActionSerializer(serializers.Serializer):
    
    
    
    greenhouse_id = serializers.IntegerField()
    password = serializers.CharField()
    actuator_id = serializers.IntegerField()
    value = serializers.CharField()
    duration = serializers.CharField(required=False, allow_null=True)
    
    def validate(self, data):
        api_response = ApiResponse()

        try:
            self.greenhouse = Greenhouse.objects.get(pk = data["greenhouse_id"] , password = data["password"] , is_active = True)
        except Greenhouse.DoesNotExist:
            response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("errors", "A greenhouse with this ID and password is not found.").get()
            raise serializers.ValidationError(detail=response)
        
        try:
            self.actuator = Actuator.objects.get(pk = data["actuator_id"])

        except Actuator.DoesNotExist:
            response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("errors", "Undefind this actuator").get()
            raise serializers.ValidationError(detail=response)
        
        return data
    
    def save(self,  **kwargs):
        action = ActuatorsAction.objects.create(
            actuator = self.actuator,
            greenhouse = self.greenhouse,
            value  = self.data["value"],
            duration = self.data["duration"]
        )
        
        return action


class GetActionsSerializer(serializers.Serializer):
    
    id = serializers.IntegerField()
    password = serializers.CharField(max_length=10)
    
    def validate(self, data):
        api_response = ApiResponse()
        
        try:
            self.greenhouse = Greenhouse.objects.get(pk=data["id"], password=data["password"] , is_active = True)
        
        except Greenhouse.DoesNotExist:
            response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("errors", "A greenhouse with this ID and password is not found.").get()
            raise serializers.ValidationError(detail=response)    
        
        return self.greenhouse
        
    
    def get_last_actions(self):

        greenhouse_actuators = GreenhouseActustor.objects.filter(greenhouse = self.greenhouse)
        
        actions = []
                
        if greenhouse_actuators.exists():
            for greenhouse_actuator in greenhouse_actuators:
                action = ActuatorsAction.objects.filter(actuator = greenhouse_actuator.actuator).order_by('-id')[0]
                actions.append(ActuatorActionsSerializer(action).data)
                
            return actions
        api_response = ApiResponse()

        return api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("message", "Undefind").get()

    def get_all_actions(self):

        greenhouse_actuators = GreenhouseActustor.objects.filter(greenhouse = self.greenhouse)
        
        actions = []
        
        if greenhouse_actuators.exists():
        
            for greenhouse_actuator in greenhouse_actuators:
                action = ActuatorsAction.objects.filter(actuator = greenhouse_actuator.actuator).order_by('-id')
                actions.append(ActuatorActionsSerializer(action, many = True).data )
                
            return actions
        
        api_response = ApiResponse()

        return api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("message", "Undefind").get()
