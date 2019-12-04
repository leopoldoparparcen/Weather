from django.urls import path
from weather.weatherapi import views # se importa el view del apps


urlpatterns = [
    path('weatherreport/', views.WeatherReport_list), # para ver la lista del apps
    path('weatherreport/<int:pk>/', views.WeatherReport_detail), # para ver la lista detallada
	path('weatherfiles/', views.WeatherFiles_list), # para ver la lista del apps
    path('weatherfiles/<int:pk>/', views.WeatherFiles_detail), # para ver la lista detallada
    path('upload/', views.FileUploadView.as_view()) # para la subida de archivos a base de datos
    ]