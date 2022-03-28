from Apps.Hardware.models import ActuatorsAction
from Apps.Hardware.models import SensorValues


class ActuatorActionsHelper:
    def __init__(self) -> None:
        self.actuators_actions = []
    
    def set_actuator_action(self, actuator_action:ActuatorsAction ) -> 'ActuatorActionsHelper':
        self.actuators_actions.append(actuator_action)
        return self
    
    def set_actuators_actions(self, actuators_actions ) -> 'ActuatorActionsHelper':
        for actuator_action in actuators_actions:
            self.actuators_actions.append(actuator_action)
        return self
    
    def get_actuator_action(self,id:int) -> ActuatorsAction:
        for sensor_value in self.actuators_actions:
            if sensor_value.id == id:
                return sensor_value
            
        return None
    
    def get_action_value(self,id:int) -> ActuatorsAction:
        actuator_action = self.get_actuator_action(id)
        
        if actuator_action:
            return actuator_action.value
        
        return None




class SensorValuesHelper:
    def __init__(self) -> None:
        self.sensors_values = []
    
    def set_sensor_value(self, sensor_value:SensorValues ) -> 'SensorValuesHelper':
        self.sensors_values.append(sensor_value)
        return self
    
    def set_sensors_values(self, sensors_values ) -> 'SensorValuesHelper':
        for sensor_value in sensors_values:
            self.sensors_values.append(sensor_value)
        return self
    
    def get_sensor_value(self,id:int) -> SensorValues:
        for sensor_value in self.sensors_values:
            if sensor_value.id == id:
                return sensor_value
            
        return None
    
    def get_value(self,id:int) -> SensorValues:
        sensor_value = self.get_sensor_value(id)
        
        if sensor_value:
            return sensor_value.value
        
        return None
    