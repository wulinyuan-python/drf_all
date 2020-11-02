from django.urls import path

from drf_day5 import views

urlpatterns = [
    path("demo/", views.Demo.as_view()),
    path("user/", views.UserAPIView.as_view()),
]