from datetime import timedelta
from Apps.Hardware.hardware_library.sensors import TempratureSensor , PHSensor , WaterLevelSensor
from Apps.Hardware.hardware_library.actuators import FanActuator , AlkalinePumpActuator , PHPumpActuator
from .models.ph_model import PHFuzzyLogic
from .models.temperature_model import TempFuzzyLogic


TIME_BETWEEN_FUZZY_ACTIONS = timedelta(minutes=10)


CONTROLLERS = [
    {
        "sensors": [TempratureSensor.ID],
        "model":TempFuzzyLogic,
        "actuators":[
            FanActuator.ID
        ]
    },
    {
        "sensors": [PHSensor.ID, WaterLevelSensor.ID],
        "model":PHFuzzyLogic,
        "actuators":[ 
            PHPumpActuator.ID,
            AlkalinePumpActuator.ID
        ]
    }
]