from django.db import models

#Modelo usado para reporte del clima
class WeatherReport(models.Model):

	date = models.DateTimeField() # fecha
	temperature = models.FloatField() # temperatura
	rainfall = models.FloatField() # lluvia
	barometricPressure = models.FloatField() #presion barometrica
	humidity =  models.IntegerField() #humedad
	windSpeed =  models.IntegerField() #velocidad de viento
	windDirection =  models.CharField(max_length=5) #direccion del viento maximo 5 caracteres
