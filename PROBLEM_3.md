# Problem 3 - API Archivos de recolleción de observaciones

Agregue un nuevo recurso a su servicio web basado en el Blueprint definido en [Appendix B](#appendix-b---api-blueprint-weather-archives). La API debe agregar la siguiente funcionalidad:
  - ver un único archivo (por ejemplo, Vista detallada)
  - ver una lista de archivos (por ejemplo, vista de lista). La vista de lista debe incluir un parámetro 'Límite' que limita el número de Archivos devueltos (Valor predeterminado: 20).


## Appendix B - API Blueprint: Archivos de recolleción de observaciones

(API Blueprint basado en https://apiblueprint.org)


```yaml
FORMAT: 1A

# API Archivos de recolleción de observaciones 
Una API simple para ver los datos del archivo meteorológico.

## Archivo [/archive/{id}]
Un objeto de archivo que tiene la informaicón de este:

+ id - A unique integer id
+ created - Una fecha en formato ISO8601 the cuando fue creada.
+ archive_file - La url para descargar el archivo.
+ status - El estado del archivo. Uno de ["Pending", "Running", "Complete", "Failure"].

+ Parametros
    + id: 1 (required, number) - Identificador unico del archivo.

### Vista de detalle del archivo [GET]

+ Response 200 (application/json)

    + Body

            {
              "id": 1,
              "created": "2019-09-23T16:21:27Z",
              "archive_file": "archive/2019/09/23/0ae02dd3-6212-46c2-9068-7fdcc74fff00.csv",
              "status": "Complete"
            }

## Colección de archivos [/archive{?limit}]

+ Parameters
    + limit (number, optional) - El numero maximo de archivos a importar.
        + Default: `20`

### Listar todos los archivos [GET]

+ Response 200 (application/json)

    + Body

            [
              {
                "id": 1,
                "created": "2019-09-23T16:21:27Z",
                "archive_file": "archive/2019/09/23/0ae02dd3-6212-46c2-9068-7fdcc74fff00.csv",
                "status": "Complete"
              },
              {
                "id": 2,
                "created": "2019-09-23T16:27:16Z",
                "archive_file": "archive/2019/09/23/42f74e19-bfe5-47ae-8cde-a03853fbb18c.csv",
                "status": "Running"
              },
              {
                "id": 3,
                "created": "2019-09-23T16:32:49Z",
                "archive_file": "archive/2019/09/23/4a4c2dc7-41e1-4d09-ae7b-49f2fd5c3468.csv",
                "status": "Pending"
              }
            ]
```
