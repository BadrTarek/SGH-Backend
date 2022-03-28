from .models import Greenhouse , GreenhouseSensor,GreenhouseActustor
from Apps.Hardware.models import Sensor,SensorValues,Actuator,ActuatorsAction



class GreenhouseDataModel:
    def __init__(self) -> None:
        self.__actuators_actions = []
        self.__automated_actions = []
        
    def set_greehouse(self , greenhouse:Greenhouse) -> 'GreenhouseDataModel':
        self.__greenhouse = greenhouse
        return self
    
    def get_greenhouse(self) -> Greenhouse:
        return self.__greenhouse
    
    def set_sensors_values(self , sensors_values:list) -> 'GreenhouseDataModel':
        self.__sensors_values = []
        for sensor_value in sensors_values:
            self.__sensors_values.append(sensor_value)
        return self
    
    def get_sensors_values(self)-> list:
        return self.__sensors_values
    
    def get_sensor_object(self , sensor_id:int)-> SensorValues:
        for sensor_value in self.__sensors_values:
            if sensor_value.sensor.id == sensor_id:
                return sensor_value
        return SensorValues()
            
    def set_actuator_action(self , actuator_action:ActuatorsAction,is_automated_action:bool = False)-> 'GreenhouseDataModel':
        if is_automated_action:
            self.__automated_actions.append(actuator_action)
        else:
            self.__actuators_actions.append(actuator_action)
        
        return self
                
    def get_actuators_actions(self):
        return  self.__actuators_actions
    
    def get_automated_actions(self):
        return  self.__automated_actions
    
    
    