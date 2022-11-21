from django.urls import path
from . import views

urlpatterns = [
    path('', views.GamerMatchViewSet.as_view())
]
