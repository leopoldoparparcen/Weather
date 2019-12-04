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


class WeatherFiles(models.Model):

	created = models.DateTimeField(auto_now_add = True)#fecha
	archive_file = models.CharField(max_length = 200) 
	file = models.FileField(blank=False, null=False) # se crea este campo para guardar de archivos a base de datos
    # Para crear las opciones para el campo status
	PENDING = 'PE'
	RUNNING = 'RU'
	COMPLETE = 'CO'
	FAILURE = 'FA' 
	STATUS_CHOICES = [
		(PENDING, 'Pending'),
		(RUNNING, 'Running'),
		(COMPLETE, 'Complete'),
		(FAILURE, 'Failure'),
	]

	status = models.CharField(max_length=2, choices = STATUS_CHOICES, default = PENDING,)




