# Problem 4 - Procesamiento de archivos asincronicos
Agregue funcionalidad a su API para permitir a un usuario PUBLICAR un archivo en la API. Puede usar el archivo CSV Weather Archive [data/weather_archive.csv](data/weather_archive.csv) para probar su API. Al PUBLICAR un archivo de Observacion Meteorologica en la API, el cuerpo de la solicitud debe ser el contenido CSV del archivo de Weather Archive.

Cuando un archivo se envía a la API, deben ocurrir las siguientes cosas:
   - El contenido del cuerpo de la solicitud debe escribirse en un nuevo archivo en el almacenamiento local
   - Se debe crear un nuevo objeto de recurso de archivo (persistir en una base de datos) y luego verlo a través de la API
   - (OPCIONAL) Se debe crear una tarea [celery](http://www.celeryproject.org/) que analice el archivo y cree objetos de recursos de observación meteorológica individuales.

## cURL Example
El siguiente comando curl se puede usar para probar su API:
```shell
$ curl -i -H 'content-type:text/csv' --data-binary @data/weather_archive.csv localhost:8000/archive/
```

## Appendix C - API Blueprint: Create Weather Archives
```yaml
FORMAT: 1A

# API para archivos
Una API simple para crear y ver datos del Archivo.

## Colección de archivos [/archive]

### Crear un nuevo archivo [POST]

Se espera que el cuerpo de la solicitud sea el archivo con las observaciones meteorologicas en formato CSV.

+ Request

    + Headers

            Content-Type: text/csv

+ Response 201 (application/json)

    + Body

            {
              "id": 3,
              "created": "2019-09-23T16:32:49Z",
              "archive_file": "archive/2019/09/23/4a4c2dc7-41e1-4d09-ae7b-49f2fd5c3468.csv",
              "status": "Pending"
            }
```
