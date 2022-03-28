from FuzzyLogic.models.temperature_model import TempFuzzyLogic
from rest_framework import serializers 
from Apps.Greenhouses.greenhouse_data_model import GreenhouseDataModel
from Apps.Hardware.sensors import TempratureSensor
from Apps.Hardware.actuators import FanActuator
from Apps.Hardware.serializers.requests_serializers import TakeAutomatedActionSerializer
from Apps.Hardware.models import SensorValues
class TemperatureModelImplementation:
    def __init__(self) -> None:
        self.model = TempFuzzyLogic()
        self.model.fuzzification()
        self.model.apply_rules()
    
    def set_greenhouse_data_model(self , greenhouse_data :GreenhouseDataModel)->'TemperatureModelImplementation':
        self.__greenhouse_data = greenhouse_data
        return self
    
    def get_greenhouse_data_model(self )->GreenhouseDataModel:
        return  self.__greenhouse_data
    
    def make_actions(self) -> 'TemperatureModelImplementation':
        
        temp_value = self.__greenhouse_data.get_sensor_object(TempratureSensor.ID).value
        temperature_rate = SensorValues.get_before_last_sensor_values(self.__greenhouse_data.get_greenhouse(),
                                    self.__greenhouse_data.get_sensor_object(TempratureSensor.ID).sensor).value
        print(f"Temperature Rate --> {temperature_rate}")
        self.model.set_input_values(temperature=temp_value , temperature_rate=temperature_rate)
        self.model.defuzzification()
        
        fan_actuator_action = self.__save_action(FanActuator.ID, self.__get_fan_value() ,  duration=None)
        
        self.__greenhouse_data.set_actuator_action(fan_actuator_action ,is_automated_action=True)

        return True
    
    def __get_fan_value(self):
        if self.model.get_ouput_values():
            return self.model.get_ouput_values()["fan_speed"]
        raise serializers.ValidationError(detail="Error on Temperature model defuzzification process")
        
    def __save_action(self, actuator_id:int,value:str,duration:str=None):
        json = {
            "greenhouse_id":self.__greenhouse_data.get_greenhouse().id,
            "password":self.__greenhouse_data.get_greenhouse().password,
            "actuator_id":actuator_id,
            "value":value,
            "duration":duration,
        }
        serializer = TakeAutomatedActionSerializer(data = json)
        serializer.is_valid(raise_exception=True)
        return serializer.save()
    
    

    