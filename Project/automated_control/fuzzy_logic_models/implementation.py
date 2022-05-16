from .configurations import MODELS,MODELS_IMPLEMENTATIONS


def implements(product):
    actions = []
    for implement in MODELS_IMPLEMENTATIONS:
        action = implement.get_actions(product)
        actions += action
        
    return actions
