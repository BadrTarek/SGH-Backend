import pickle
from controlling.actuators import alkaline_pump_actuator,ph_pump_actuator
from monitoring.sensors import ph_sensor , water_level_sensor
from controlling.models import Actuator
from monitoring.models import Sensor, SensorValues
from library.api_response import ApiResponse
from rest_framework import serializers 

PH_MODEL_PATH = r"E:\Graduation Project\Backend\Project\automated_control\sav_models\ph_fuzzy_model.sav"

SENSORS = [
    Sensor.get_sensor(ph_sensor.ID),
    Sensor.get_sensor(water_level_sensor.ID)
]

ACTUATORS = [
    Actuator.get_actuator( ph_pump_actuator.ID),
    Actuator.get_actuator( alkaline_pump_actuator.ID)
]

class PhFuzzyLogicModel():    
    def __init__(self,product):
        self.model = pickle.load(open(PH_MODEL_PATH, 'rb'))
        
        self.actuators = ACTUATORS
        self.sensors = SENSORS
        
        self.product = product
        
        self.ph_value = self.get_last_sensor_values(self.sensors[0])
        self.water_level_value = self.get_last_sensor_values(self.sensors[1])
        
        
    def get_last_sensor_values(self,sensor):

        sensor_value = SensorValues.get_last_sensor_values(self.product,sensor)     
        
        if sensor_value:
            return sensor_value.value

        return False
        
        
    def get_actions(self):

        try:
            
            self.model.input['ph'] = float(self.ph_value)
            self.model.input['water_level'] =float(self.water_level_value)
            self.model.compute()

            return [
                {
                    "actuator": self.actuators[0],
                    "value": 1 if round(self.model.output['ph_pump'],1) > 0 else 0 ,
                    "duration":round(self.model.output['ph_pump'],1)
                },
                {
                    "actuator": self.actuators[1],
                    "value": 1 if round(self.model.output['alkaline_pump'],1) > 0 else 0,
                    "duration": round(self.model.output['alkaline_pump'],1)
                }
            ]
            
        except:
            api_response = ApiResponse()
            response = api_response.set_data("errors", "Error in PH Fuzzy Logic Model").get()
            raise serializers.ValidationError(detail=response)
        
        
        


