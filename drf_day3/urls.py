from django.urls import path

from drf_day3 import views

urlpatterns = [
    path("books/", views.BookAPIView.as_view()),
    path("books/<str:id>/", views.BookAPIView.as_view()),

    path("v2/books/", views.BookAPIViewV2.as_view()),
    path("v2/books/<str:id>/", views.BookAPIViewV2.as_view()),
]
