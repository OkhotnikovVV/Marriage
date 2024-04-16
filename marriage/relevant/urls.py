from django.urls import path

from .views import about
from .views import CalculateAPI
from .views import index

urlpatterns = [
    path('', index),
    path('calculate/', CalculateAPI.as_view(), name='calculate'),
    path('about/', about, name='about'),
]
