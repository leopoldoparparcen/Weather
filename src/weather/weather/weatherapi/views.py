from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from weather.weatherapi.models import WeatherReport
from weather.weatherapi.serializers import WeatherReportSerializer


# Funcion para mostar la lista de reporte 
@csrf_exempt #decorador para que no sea necesario usar token CSRF al hacer post
def WeatherReport_list(request):

    # si el metodo es get, toma todo los objetos, los serializa y los regresa como Json
    if request.method == 'GET':
        limit = request.GET.get('limit', 20) # se obtiene el limite del request, queda por defecto 20
        report = WeatherReport.objects.all()[0:int(limit)] 
        serializer = WeatherReportSerializer(report, many=True)
        return JsonResponse(serializer.data, safe=False)

    # si el metodo es POST, toma el Json, lo serializa, verifica si es valido y de serlo lo guarda en la base de datos    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = WeatherReportSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# Funcion para un mostar reporte detallado
@csrf_exempt
def WeatherReport_detail(request, pk):

    try:
        report = WeatherReport.objects.get(pk=pk)
    except WeatherReport.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET': # toma un registro, lo serializa y retorna Json
        serializer = WeatherReportSerializer(report)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT': # para agregar registros uno a uno
        data = JSONParser().parse(request)
        serializer = WeatherReportSerializer(report, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE': # para borrar un registro
        report.delete()
        return HttpResponse(status=204)

