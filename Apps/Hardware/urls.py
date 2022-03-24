from django.urls import path , include
from . import views

urlpatterns = [
    path('hardware/', include([
        path('sensors/values/store',views.StoreSensorsValuesView.as_view()),    
        path('actuator/action',views.TakeAcionView.as_view()),    
        path('actuator/action/auto',views.TakeAutomatedActionView.as_view()),    
        # path('sensors/values/get/last',views.GetLastSensorValuesView.as_view()),    
        # path('sensors/values/get',views.GetAllSensorValuesView.as_view()),    
        # path('actuators/actions/get/last',views.GetLastActionsView.as_view()),    
        # path('actuators/actions/get',views.GetAllActionsView.as_view()),    
    ])),
    
]
