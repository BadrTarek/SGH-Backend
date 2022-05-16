from django.apps import AppConfig
# from .fuzzy_logic_models.configurations import MODELS

from .fuzzy_logic_models.ph_model.model import PHFuzzyLogic

class AutomatedControlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'automated_control'
    ph_model = PHFuzzyLogic()


