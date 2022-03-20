from django.urls import path, include
from . import views


urlpatterns = [
    path('greenhouse/', include([
        path('configure', views.ConfigureGreenhouseView.as_view()),
        path('get', views.GetUserGreenhousesView.as_view()),
        path('get/<int:id>', views.GetUserGreenhousesView.as_view()),
        path('update/<int:id>', views.UpdateGreenhouseView.as_view()),
        
        path('login', views.GreenhouseLoginView.as_view()),
        path('logout', views.GreenhouseLogoutView.as_view()),

    ]))
]
