from django.urls import path, include
from . import views

urlpatterns = [

    path('hardware/', include([
        path('sensors/values/store', views.StoreSensorsValuesView.as_view()),
        path('sensor/values/get', views.GetAllSensorValuesView.as_view()),
    ])),

]



