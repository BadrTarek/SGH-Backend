from .ph_model.model import PHFuzzyLogic
from datetime import timedelta
# from .ph_model import * 
#ph_model import implementation
from .ph_model import implementation as ph_implementation


TIME_BETWEEN_FUZZY_ACTIONS = timedelta(minutes=10)

ALLOW_AUTOMATED_CONTROL = True

MODELS = [
    PHFuzzyLogic
]

MODELS_IMPLEMENTATIONS = [
    ph_implementation
]
