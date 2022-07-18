from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # Authetication urls
    path('user/', include([
        path('register', views.RegisterView.as_view(), name="register"),
        path('login', views.LoginView.as_view(), name="login"),
        path('logout', views.LogoutView.as_view(), name="logout"),
        path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    ])),

]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)