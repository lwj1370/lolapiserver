from django.urls import path
from . import views

urlpatterns = [
    path('match-api', views.GamerMatchViewSet.as_view())
]
