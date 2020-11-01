from django.urls import path

from drf_day3 import views

urlpatterns = [
    path("books/", views.BookAPIView.as_view()),
    path("books/<str:id>/", views.BookAPIView.as_view()),

    path("v2/books/", views.BookAPIViewV2.as_view()),
    path("v2/books/<str:id>/", views.BookAPIViewV2.as_view()),

    path("gen/", views.BookGenericAPIView.as_view()),
    path("gen/<str:pk>/", views.BookGenericAPIView.as_view()),

    path("v3/", views.BookGenericAPIViewV3.as_view()),
    path("v3/<str:pk>/", views.BookGenericAPIViewV3.as_view()),

    path("set/", views.BookViewSetView.as_view({'post':'user_login'})),
    path("set/<str:pk>/", views.BookViewSetView.as_view({'post':'user_login'})),
]
