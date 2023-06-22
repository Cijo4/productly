from django.urls import path
from . import views  # de la carpeta en la que me encuentro (.) importa views

urlpatterns = [
    path('', views.index, name='index')
]
