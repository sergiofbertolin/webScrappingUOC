# webScrappingUOC

## Práctica 1: Web scraping

## Descripción

### Contexto, justificación y finalidad
Desarrollo de la práctica 1 de la asignatura Tipología y ciclo de vida de los datos del Máster Universitario en Ciencia de Datos de la Universitat Oberta de Catalunya.

En el momento actual, dentro de la mayor pandemia del siglo, hay una incertidumbre creciente en todos los aspectos financieros, de los que no queda exento el mercado inmobiliario.

Mediante esta recolección de datos se pretende obtener una herramienta que permita analizar la tendencia del principal índice inmobiliario en Europa, el Euribor, para poder realizar tanto análisis como predicciones.

La finalidad del proyecto es educativa y de investigación, no comercial.

### Datos obtenidos
Creación de un dataset en formato csv con los valores diarios del euribor desde 1999 hasta el día actual con fines educativos. Se obtienen las cotizaciones con un programa en python mediante técnicas de webscraping contra el portal inmobiliario www.idealista.com
Idealista es uno de los portales inmobialiarios de referencia en el contexto estatal y probablemente uno de los mayores portales de compra venta en España.

Incluir citas de estudios con datos de Idealista (TODO)

## Miembros del equipo

Sergio Fernández Bertolin

Enrique Javier Andrés Orera


## Descripción de los ficheros


### Ficheros del código fuente
La extracción de datos se realiza mediante un script en código Python, escrito para funcionar con Python3 
__euribordiario.py__
Este código fuente genera un DataFrame de salida que se almacena en un fichero csv y una gráfica en formato PNG que permite interpretar los datos
El DataFrame generado tiene el siguiente formato:

| Index   |      Dia      |  Valor |
|---------|:-------------:|-------:|
| 0       |  19990104     | 0.345  |
| 1       |  19990105     | 0.367  |

Donde __Index__ es un valor entero auto incremental, empezando en cero
__Dia__ es el dia en el que se ha registrado el valor, con el formato AAAAMMDD, donde las cuatro primeras cifras son el año, las dos siguientes el mes en formato numérico y las dos últimas el día
__Valor__ es el valor del índice del Euribor registrado ese día, en formato decimal


### Fichero CSV
El DataFrame se almacena en un fichero csv, con el siguiente nombre:
 __euribordiario.csv__
En el repositorio hay un fichero de ejemplo generado el 30 de octubre de 2020. 

### Fichero PNG
El código de Python también genera una gráfica con la representación de la evolución diaria del índice, llamada:
 __euribordiario.png__
En el repositorio hay una gráfica de ejemplo generada el 30 de octubre de 2020.

### Otros ficheros
pdf/Práctica 1.pdf: contiene el documento de respuestas (TO DO)

## Licencia


Práctica 1 de la asignatura Tipología y Ciclo de Vida de los Datos del Master de Ciencia de Datos de la UOC

1. Contexto. Explicar en qué contexto se ha recolectado la información. Explique
por qué el sitio web elegido proporciona dicha información.
2. Definir un título para el dataset. Elegir un título que sea descriptivo.
3. Descripción del dataset. Desarrollar una descripción breve del conjunto de datos
que se ha extraído (es necesario que esta descripción tenga sentido con el título
elegido).
4. Representación gráfica. Presentar una imagen o esquema que identifique el
dataset visualmente
5. Contenido. Explicar los campos que incluye el dataset, el periodo de tiempo de
los datos y cómo se ha recogido.
6. Agradecimientos. Presentar al propietario del conjunto de datos. Es necesario
incluir citas de investigación o análisis anteriores (si los hay).
7. Inspiración. Explique por qué es interesante este conjunto de datos y qué
preguntas se pretenden responder.
8. Licencia. Seleccione una de estas licencias para su dataset y explique el motivo
de su selección:
○ Released Under CC0: Public Domain License
○ Released Under CC BY-NC-SA 4.0 License
○ Released Under CC BY-SA 4.0 License
○ Database released under Open Database License, individual contents
under Database Contents License
○ Other (specified above)
○ Unknown License
9. Código. Adjuntar el código con el que se ha generado el dataset, preferiblemente
en Python o, alternativamente, en R.
10. Dataset. Publicación del dataset en formato CSV en Zenodo (obtención del DOI)
con una breve descripción.
