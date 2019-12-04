from rest_framework import serializers
from weather.weatherapi.models import WeatherReport, WeatherFiles

#Se uso serializer porque trae las funciones de lista y vista detallada
class  WeatherReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherReport
        # se toman todos los campos del modelo
        fields = ['id','date','temperature','rainfall','barometricPressure','humidity','windSpeed','windDirection']


class  WeatherFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherFiles
        # se toman todos los campos del modelo
        fields = ['id','created','archive_file','status']        