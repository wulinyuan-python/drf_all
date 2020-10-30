from django.urls import path

from drf_day2 import views

urlpatterns = [
    path("user/", views.UserView.as_view()),
    path("student/", views.StudentAPIView.as_view()),
    path("student/<str:id>/", views.StudentAPIView.as_view()),

    path("emp/", views.EmployeeAPIView.as_view()),
    path("emp/<str:id>/", views.EmployeeAPIView.as_view()),

    path("teacher/", views.TeacherAPIView.as_view()),
    path("teacher/<str:id>/", views.TeacherAPIView.as_view()),
]
