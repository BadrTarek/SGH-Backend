from .sensors import PHSensor , TempratureSensor , WaterLevelSensor, GasSensor,LightSensor
from .actuators import AlkalinePumpActuator, FanActuator, PHPumpActuator, LEDActuator


SENSORS = [
    PHSensor, 
    TempratureSensor,
    WaterLevelSensor,
    GasSensor,
    LightSensor
]

ACTUATORS = [
    AlkalinePumpActuator,
    FanActuator, 
    PHPumpActuator, 
    LEDActuator
]