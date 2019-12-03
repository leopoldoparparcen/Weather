from django.db import models

class WeatherReport(models.Model):

	date = models.DateTimeField()
	temperature = models.FloatField()
	rainfall = models.FloatField()
	barometricPressure = models.FloatField()
	humidity =  models.IntegerField()
	windSpeed =  models.IntegerField()
	windDirection =  models.CharField(max_length=5)
