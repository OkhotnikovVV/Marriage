from django.urls import path

from .views import index, about, CalculateAPI

urlpatterns = [
    path('', index),
    # path('calculate/', calculate, name='calculate'),
    path('calculate/', CalculateAPI.as_view(), name='calculate'),
    path('about/', about, name='about'),
]