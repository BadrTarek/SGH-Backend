from django.urls import path
from . import views


urlpatterns = [
    path('crop/recommendations/<int:product_id>',views.CropRecommendationsView.as_view())
]



