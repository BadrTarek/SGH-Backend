from django.urls import path, include
from . import views


urlpatterns = [

    path('product/', include([
        path('configure', views.ConfigureProductView.as_view()),
        path('get', views.GetUserProductsView.as_view()),
        path('get/<int:id>', views.GetUserProductsView.as_view()),
        path('update/<int:id>', views.UpdateProductView.as_view()),

        path('login', views.ProductLoginView.as_view()),
        path('logout', views.ProductLogoutView.as_view()),

        # path('fire', views.FireView.as_view())
    ])),

]



