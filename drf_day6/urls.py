from django.urls import path
from rest_framework_jwt.views import ObtainJSONWebToken, obtain_jwt_token

from drf_day6 import views

urlpatterns = [
    path("login/", ObtainJSONWebToken.as_view()),
    path("detail/", views.UserDetailAPIView.as_view()),
    path("user/", views.LoginAPIView.as_view()),
    path("com/", views.ComputerListAPIView.as_view()),
]
