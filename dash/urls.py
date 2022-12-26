from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('survey/', views.survey, name="survey"),
    path('story/', views.story, name="story"),
    path('about/', views.about, name="about"),
]
