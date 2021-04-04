"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'pizza_online'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all pizzas.
    path('pizzas/', views.pizzas, name='pizzas'),
]