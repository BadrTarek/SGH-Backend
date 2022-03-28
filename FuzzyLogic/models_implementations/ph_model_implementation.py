from Apps.Hardware.models import Actuator, ActuatorsAction
from FuzzyLogic.models.ph_model import PHFuzzyLogic
from rest_framework import serializers 
from Apps.Greenhouses.greenhouse_data_model import GreenhouseDataModel
from Apps.Hardware.sensors import PHSensor , WaterLevelSensor
from Apps.Hardware.actuators import PHPumpActuator , AlkalinePumpActuator
from Apps.Hardware.serializers.requests_serializers import TakeAutomatedActionSerializer
# from Apps.Hardware.requests import TakeAutomatedActionSerializer, take_automated_action

class PHModelImplementation:
    def __init__(self) -> None:
        self.model = PHFuzzyLogic()
        self.model.fuzzification()
        self.model.apply_rules()
    
    def set_greenhouse_data_model(self , greenhouse_data :GreenhouseDataModel)->'PHModelImplementation':
        self.__greenhouse_data = greenhouse_data
        return self
    
    def get_greenhouse_data_model(self )->GreenhouseDataModel:
        return  self.__greenhouse_data
    
    def make_actions(self) -> 'PHModelImplementation':
        
        ph_value = self.__greenhouse_data.get_sensor_object(PHSensor.ID).value
        water_level_value = self.__greenhouse_data.get_sensor_object(WaterLevelSensor.ID).value
        
        self.model.set_input_values(ph_value = ph_value, water_level_value= water_level_value)
        self.model.defuzzification()
        
        ph_pump_duration = self.__get_ph_pump_value() 
        alkaline_pump_duration = self.__get_alkaline_pump_value() 
        
        if ph_pump_duration == 0.0:
            ph_actuator_action = self.__save_action(PHPumpActuator.ID, 0 ,  duration=ph_pump_duration)
        else:
            ph_actuator_action = self.__save_action(PHPumpActuator.ID, 1 ,  duration=ph_pump_duration)
        
        if alkaline_pump_duration == 0.0:
            alkaline_actuator_action = self.__save_action(AlkalinePumpActuator.ID,0 , duration=alkaline_pump_duration)
        else:
            alkaline_actuator_action = self.__save_action(AlkalinePumpActuator.ID,1 , duration=alkaline_pump_duration)
        
        self.__greenhouse_data.set_actuator_action(ph_actuator_action ,is_automated_action=True)
        self.__greenhouse_data.set_actuator_action(alkaline_actuator_action ,is_automated_action=True)

        return True
    
    def __get_ph_pump_value(self):
        if self.model.get_ouput_values():
            return self.model.get_ouput_values()["ph_pump"]
        raise serializers.ValidationError(detail="Error on PH model defuzzification process")
    
    def __get_alkaline_pump_value(self):
        if self.model.get_ouput_values():
            return self.model.get_ouput_values()["alkaline_pump"]
        raise serializers.ValidationError(detail="Error on PH model defuzzification process")
    
    
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
    
    

    