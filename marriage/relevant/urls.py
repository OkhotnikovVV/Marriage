from django.urls import path

from .views import index, calculate, about


urlpatterns = [
    path('', index),
    path('calculate/', calculate, name='calculate'),
    path('about/', about, name='about'),
]