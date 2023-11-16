from django.urls import path
from theblog import views

urlpatterns = [
    path('', views.index, name="index"), #Donde index es una funcion a mostrar como template
]
