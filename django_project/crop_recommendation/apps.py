from django.apps import AppConfig
from .models import CropSuggestionModel


class CropRecommendationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crop_recommendation'
    crop_suggestion_model = CropSuggestionModel()
