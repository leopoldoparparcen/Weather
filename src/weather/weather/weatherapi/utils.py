import csv
from weather.weatherapi.models import WeatherReport

# Esta Funcion lee un archivo csv, y guarda los reportes en una base de datos
def csv_to_db(file):
	reader = csv.reader(file)
	data = list(reader)
	# Se ignora la primera fila de csv porque es el encabezado
	for report in data[1:]:
		# Se crea nuevo objeto del modelo
		new_report = WeatherReport(	date=report[0],
		 							temperature= report[1],
		 							rainfall= report[2],
		 							barometricPressure= report[3],
		 							humidity= report[4],
		 							windSpeed= report[5],
		 							windDirection= report[6])

		new_report.save()