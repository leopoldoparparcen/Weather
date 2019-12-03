from rest_framework import serializers

class WeatherReportSerializer(serializers.Serializer):

	id = serializers.IntegerField(read_only=True)
	date = serializers.DateTimeField()
	temperature = serializers.FloatField()
	rainfall = serializers.FloatField()
	barometricPressure = serializers.FloatField()
	humidity = serializers.IntegerField()
	windSpeed = serializers.IntegerField()
	windDirection = serializers.CharField(max_length=5)