from django.urls import path
from . import views

urlpatterns = [
    path('netflix_list', views.NetflixListViewSet.as_view()),
]
