from django.urls import path, include
from . import views

urlpatterns = [
    path('hardware/', include([
        path('actuator/action', views.TakeAcionView.as_view()),
        path('actuators/actions/get/<int:id>', views.GeAllActionsView.as_view()),

    ])),
]



