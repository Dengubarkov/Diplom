from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('authors/', views.authors, name='authors'),
    path('manual-page/<int:pk>/', views.manual, name='manual'),


    ]