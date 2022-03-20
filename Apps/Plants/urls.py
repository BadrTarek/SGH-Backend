from django.urls import path, include
from . import views


urlpatterns = [
    # path('greenhouse/', include([
    #     path('configure', views.ConfigureGreenhouseView.as_view()),
    #     path('get/', views.GetUserGreenhousesView.as_view()),
    #     path('get/<int:id>', views.GetUserGreenhousesView.as_view()),
    #     path('update/<int:id>', views.UpdateGreenhouseView.as_view()),
    # ]))
    path('plants/', include([
        path('get/supported', views.SupportedPlantsView.as_view()),
        # path('get/', views.GetUserGreenhousesView.as_view()),
    ]))

]
