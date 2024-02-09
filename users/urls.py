from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.views import LoginView
from users.apps import UsersConfig
from users.views import RegisterView

app_name = UsersConfig.name


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('login/', LoginView.as_view(), name='login'),  # login endpoint
    path('register/', RegisterView.as_view(), name='register'),  # registration endpoint

]


