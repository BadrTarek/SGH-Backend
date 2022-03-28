from Apps.Greenhouses.greenhouse_data_model import GreenhouseDataModel
from .fuzzy_logic_system_settings import CONTROLLERS


def implement(greenhouse_data:GreenhouseDataModel):
    actions = []
    for controller in CONTROLLERS:
        controller.set_greenhouse_data_model(greenhouse_data).make_actions()
        actions += controller.get_greenhouse_data_model().get_automated_actions()
        
    return actions
    
