from django.urls import include, path
from django.urls import path
from .views import RegisterUser, logout_user, me_user, get_user, UserUpdate
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register', RegisterUser.as_view()),
    path('refresh_token', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout', logout_user),
    path('me', me_user),
    path('user/<int:pk>', get_user, name='get_user'),
    path('user/update/<int:pk>', UserUpdate.as_view(), name='auth_user_detail')
]
