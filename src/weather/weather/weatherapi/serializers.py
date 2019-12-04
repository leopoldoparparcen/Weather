from rest_framework import serializers
from weather.weatherapi.models import WeatherReport

#Se uso serializer porque trae las funciones de lista y vista detallada
class  WeatherReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherReport
        # se toman todos los campos del modelo
        fields = ['id','date','temperature','rainfall','barometricPressure','humidity','windSpeed','windDirection']