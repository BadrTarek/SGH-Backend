from django.urls import path, include
from .views import hardware_views
# from . import views


urlpatterns = [
    
    # path('product/', include([
    #     path('configure', views.ConfigureGreenhouseView.as_view()),
    #     path('get', views.GetUserGreenhousesView.as_view()),
    #     path('get/<int:id>', views.GetUserGreenhousesView.as_view()),
    #     path('update/<int:id>', views.UpdateGreenhouseView.as_view()),
        
    #     path('login', views.GreenhouseLoginView.as_view()),
    #     path('logout', views.GreenhouseLogoutView.as_view()),

    # ])),
    
    path('hardware/', include([
        path('sensors/values/store',hardware_views.StoreSensorsValuesView.as_view()),    
        path('sensor/values/get',hardware_views.GetAllSensorValuesView.as_view()),    
        
        path('actuator/action',hardware_views.TakeAcionView.as_view()),    
        path('actuators/actions/get',hardware_views.GeAllActionsView.as_view()),          
        
    ])),
    
    # path('plants/', include([
    #     path('get/supported', views.SupportedPlantsView.as_view()),
    # ]))

]



