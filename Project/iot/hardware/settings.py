from .sensors import dht11_sensor, ldr_light_sensor, mq135_sensor, ph_sensor, water_level_sensor
from .actuators import alkaline_pump_actuator, fan_actuator, led_actuator, ph_pump_actuator,water_pump_actuator


SENSORS = [
    ph_sensor, 
    dht11_sensor,
    water_level_sensor,
    mq135_sensor,
    ldr_light_sensor
]

ACTUATORS = [
    alkaline_pump_actuator,
    fan_actuator, 
    ph_pump_actuator, 
    led_actuator,
    water_pump_actuator
]