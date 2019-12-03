# Problem 2 - API de observaciones meteorológicas 

Cree un servicio web basado en Python basado en el siguiente Blueprint API definido en [Appendix A](#appendix-a---api-blueprint-weather-observations)). La API solo debe proporcionar la siguiente funcionalidad:
  - ver una sola observación (por ejemplo, vista detallada)
  - ver una lista de observaciones (por ejemplo, vista de lista). La vista de lista debe incluir un parámetro 'Límite' que limita el número de Observaciones devueltas (Predeterminado: 20).


## Appendix A - API Blueprint: observaciones meteorológicas 

(API Blueprint basado en https://apiblueprint.org)


```yaml
FORMAT: 1A

# API de observaciones meteorológicas 
A simple API for displaying weather observations. Readonly.

## Observación [/observation/{id}]
Una observación tiene los siguientes atributos:

+ id - Un id entero unico
+ date - Una fecha en formato ISO8601 the cuando fue recogida.
+ temperature - Temperatura promedio en °F.
+ rainfall - precipitación total durante el período de observación en pulgadas.
+ barometricPressure -  Presión atmosférica en pulgadas Hg.
+ humidity - humedad relativa como porcentaje.
+ windSpeed - velocidad media del viento en mph.
+ windDirection -  etiqueta de dirección del viento predominante (N, NNW, NW, ..., NNE).

+ Parameters
    + id: 1 (required, number) - Un identificador unico de la observación.

### Vista de detalle de una sola observación [GET]

+ Response 200 (application/json)

    + Body

            {
              "id": 1,
              "date": "2016-03-23T18:50:00Z",
              "temperature": 32.3,
              "rainfall": 0.0,
              "barometricPressure": 29.979,
              "humidity": 78,
              "windSpeed": 2,
              "windDirection": "SSW"
            }

## Lista de observaciones [/observation{?limit}]

+ Parameters
    + limit (number, optional) - Numero maximo de observaciones a retornar. 
        + Default: `20`

### Lista de todas las observaciones [GET]

+ Response 200 (application/json)

    + Body

            [
              {
                "id": 1,
                "date": "2016-03-23T18:50:00Z",
                "temperature": 32.3,
                "rainfall": 0.0,
                "barometricPressure": 29.979,
                "humidity": 78,
                "windSpeed": 2,
                "windDirection": "SSW"
              },
              {
                "id": 2,
                "date": "2016-03-23T18:55:00Z",
                "temperature": 32.4,
                "rainfall": 0.0,
                "barometricPressure": 29.977,
                "humidity": 78,
                "windSpeed": 2,
                "windDirection": "SSW"
              },
              {
                "id": 3,
                "date": "2016-03-23T19:00:00Z",
                "temperature": 32.5,
                "rainfall": 0.0,
                "barometricPressure": 29.972,
                "humidity": 78,
                "windSpeed": 3,
                "windDirection": "SSW"
              }
            ]
```
