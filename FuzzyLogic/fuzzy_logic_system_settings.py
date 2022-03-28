from datetime import timedelta
from .models_implementations.ph_model_implementation import PHModelImplementation
from .models_implementations.temperature_model_implementation import TemperatureModelImplementation

TIME_BETWEEN_FUZZY_ACTIONS = timedelta(minutes=10)

ALLOW_AUTOMATED_CONTROL = True

CONTROLLERS = [
    PHModelImplementation(),
    # TemperatureModelImplementation()
]