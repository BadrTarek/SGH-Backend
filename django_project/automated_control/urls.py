from django.urls import path, include
from . import views

urlpatterns = [

    path('hardware/', include([
        path('automated/action', views.TakeAutomatedAction.as_view()),
    ])),

]


