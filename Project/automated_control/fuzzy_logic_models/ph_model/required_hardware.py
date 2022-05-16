from iot.hardware.sensors import ph_sensor,water_level_sensor
from iot.hardware.actuators import alkaline_pump_actuator, ph_pump_actuator


SENSORS = [
    ph_sensor.ID,
    water_level_sensor.ID
]


ACTUATORS = [
    ph_pump_actuator.ID,
    alkaline_pump_actuator.ID
]