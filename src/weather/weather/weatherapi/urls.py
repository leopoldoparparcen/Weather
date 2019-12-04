from django.urls import path
from weather.weatherapi import views # se importa el view del apps

urlpatterns = [
    path('weatherreport/', views.WeatherReport_list), # para ver la lista del apps
    path('weatherreport/<int:pk>/', views.WeatherReport_detail), # para ver la lista detallada

    ]