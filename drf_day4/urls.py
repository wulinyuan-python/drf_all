from django.urls import path
from drf_day4 import views

urlpatterns = [
    path('workers/login',views.WorkersViewSetView.as_view({'post':'login'})),
    path('workers/register',views.WorkersViewSetView.as_view({'post':'register'})),
]