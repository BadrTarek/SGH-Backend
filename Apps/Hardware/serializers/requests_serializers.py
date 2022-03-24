from rest_framework import serializers
from Apps.Greenhouses.models import Greenhouse, GreenhouseActustor, GreenhouseSensor
from Apps.Hardware.models import Sensor, Actuator, ActuatorsAction, SensorValues
from rest_framework import status
from Library.api_response import ApiResponse
from .models_serializers import SensorSerializer,SensorValueSerializer, ActuatorSerializer, ActuatorActionsSerializer 

from Apps.Greenhouses.validations import greenhouse_validation , greenhouse_sensor_validation, greenhouse_actuator_validation
from Apps.Hardware.validations import sensor_validation , actuator_validation
from datetime import  datetime
from FuzzyLogic.fuzzy_logic_system_settings import TIME_BETWEEN_FUZZY_ACTIONS


class SensorWithValueSerializer(serializers.Serializer):
    sensor_id = serializers.IntegerField()
    value = serializers.CharField()
    
class StoreSensorValuesSerializer(serializers.Serializer):
    greenhouse_id = serializers.IntegerField()
    password = serializers.CharField()
    sensors = serializers.ListField(child = SensorWithValueSerializer())
            
    def validate(self, data):
        greenhouse_validation(data["greenhouse_id"] , password=data["password"])
        for sensor in data["sensors"]:
            # sensor_validation(id = sensor['sensor_id'],value = sensor["value"])
            greenhouse_sensor_validation(sensor['sensor_id'],data["greenhouse_id"])
        return data
    
    def get_sensor_value(self , id):
        for sensor_value in self.sensor_values_response :
            if  sensor_value.sensor == Sensor.get_sensor(id):
                return sensor_value.value
        return False
        
    
    def save(self,   **kwargs):

        self.sensor_values_response = []
        self.greenhouse = Greenhouse.get_greenhouse(self.data['greenhouse_id'],self.data['password'])

        for sensor in self.data["sensors"]:
            my_sensor = Sensor.get_sensor(sensor['sensor_id'])
            
            sensor_value = SensorValues.objects.create(
                greenhouse=self.greenhouse,
                sensor=my_sensor,
                value=sensor["value"]
            )
            self.sensor_values_response.append(sensor_value)

        return self.sensor_values_response

    def get_greenhouse(self):
        return self.greenhouse


# class GetSensorValuesSerializer(serializers.Serializer):
#     greenhouse_id = serializers.IntegerField()
#     password = serializers.CharField(max_length=10)
#     sensor_id = serializers.IntegerField(required=False, allow_null=True)
    
#     # def check_greenhouse_sensors(self,data):
#     #     self.greenhouse_sensors = GreenhouseSensor.get_greenhouse_sensors(self.greenhouse)
#     #     if not self.greenhouse_sensors:
#     #         api_response = ApiResponse()
#     #         response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("errors", "Undefind.").get()
#     #         raise serializers.ValidationError(detail=response)
#     #     return True
    
#     def validate(self, data):
#         greenhouse_validation(data["id"] ,data["password"] )
#         if data["sensor_id"]:
#             greenhouse_sensor_validation(data["sensor_id"],data["greenhouse_id"])
        
#         return data

#     def get_last_values(self):            
#         values = []

#         for greenhouse_sensor in self.greenhouse_sensors:
#             sensor_values = SensorValues.get_last_sensor_values(sensor=greenhouse_sensor.sensor , greenhouse= self.greenhouse )
#             values.append(SensorValueSerializer(sensor_values ).data)

#         return values


#     def get_all_values(self):
#         values = []

#         for greenhouse_sensor in self.greenhouse_sensors:
#             sensor_values = SensorValues.get_all_sensor_values(sensor=greenhouse_sensor.sensor , greenhouse= self.greenhouse )
#             print(sensor_values)
#             values.append(SensorValueSerializer(sensor_values , many=True).data)

#         return values


class TakeActionSerializer(serializers.Serializer):

    greenhouse_id = serializers.IntegerField()
    password = serializers.CharField()
    actuator_id = serializers.IntegerField()
    value = serializers.CharField()
    duration = serializers.CharField(required=False, allow_null=True)
    
    def validate(self, data):
        greenhouse_validation(data["greenhouse_id"],data["password"])
        actuator_validation(data["actuator_id"])
        return data

    def save(self,  **kwargs):
        self.actuator = Actuator.get_actuator(self.data["actuator_id"])
        self.greenhouse = Greenhouse.get_greenhouse(self.data["greenhouse_id"],self.data["password"])
        action = ActuatorsAction.objects.create(
            actuator=self.actuator,
            greenhouse=self.greenhouse,
            value=self.data["value"],
            duration=self.data["duration"]
        )

        return action

class TakeAutomatedActionSerializer(serializers.Serializer):

    greenhouse_id = serializers.IntegerField()
    password = serializers.CharField()
    actuator_id = serializers.IntegerField()
    value = serializers.CharField()
    duration = serializers.CharField(required=False, allow_null=True)
    
    def check_date(self, action_date):
        difference  = datetime.now() - datetime.strptime(str(action_date)[:19] , '%Y-%m-%d %H:%M:%S')
        
        if  difference < TIME_BETWEEN_FUZZY_ACTIONS:
            return False
        return True
            
    
    def validate(self, data):
        greenhouse_validation(data["greenhouse_id"],data["password"])
        actuator_validation(data["actuator_id"])
        self.actuator = Actuator.get_actuator(data["actuator_id"])
        self.greenhouse = Greenhouse.get_greenhouse(data["greenhouse_id"],data["password"])
        last_action = ActuatorsAction.get_last_automated_actions(self.greenhouse , self.actuator)

        
        if last_action:
            if not self.check_date(last_action.created_at):    
                api_response = ApiResponse()
                response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("errors", "Cannot apply automated control.").get()
                raise serializers.ValidationError(detail=response)
        
        return data

    def save(self,  **kwargs):
        action = ActuatorsAction.objects.create(
            actuator=self.actuator,
            greenhouse=self.greenhouse,
            value=self.data["value"],
            duration=self.data["duration"],
            is_automated_action = True
        )

        return action


# class GetActionsSerializer(serializers.Serializer):

#     id = serializers.IntegerField()
#     password = serializers.CharField(max_length=10)

#     def validate(self, data):
#         api_response = ApiResponse()

#         self.greenhouse = Greenhouse.get_greenhouse(id = data["id"], password=data["password"])

#         if not self.greenhouse:
#             response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("errors", "A greenhouse with this ID and password is not found.").get()
#             raise serializers.ValidationError(detail=response)

#         self.greenhouse_actuators = GreenhouseActustor.get_greenhouse_actuators(self.greenhouse)
        
#         if not self.greenhouse_actuators:
#             response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("errors", "Undefind.").get()
#             raise serializers.ValidationError(detail=response)
        
#         return data

    
#     def get_last_actions(self):

#         actions = []

#         for greenhouse_actuator in self.greenhouse_actuators:
#             action = ActuatorsAction.get_last_actuator_actions(self.greenhouse,greenhouse_actuator.actuator)
#             actions.append(ActuatorActionsSerializer(action ).data)

#         return actions

#     def get_all_actions(self):

#         actions = []

#         for greenhouse_actuator in self.greenhouse_actuators:
#             action = ActuatorsAction.get_all_actuator_actions(self.greenhouse,greenhouse_actuator.actuator)
#             print(action)
#             actions.append(ActuatorActionsSerializer(action , many=True).data)

#         return actions