# webScrappingUOC

## Práctica 1: Web scraping

## Descripción

### Contexto, justificación y finalidad
Desarrollo de la práctica 1 de la asignatura Tipología y ciclo de vida de los datos del Máster Universitario en Ciencia de Datos de la Universitat Oberta de Catalunya.

En el momento actual, dentro de la mayor pandemia del siglo, hay una incertidumbre creciente en todos los aspectos financieros, de los que no queda exento el mercado inmobiliario.

Mediante esta recolección de datos se pretende obtener una herramienta que permita analizar la tendencia del principal índice inmobiliario en Europa, el Euribor, para poder realizar tanto análisis como predicciones.

La finalidad del proyecto es educativa y de investigación, no comercial.

### Datos obtenidos
Creación de un dataset en formato csv  con los valores diarios del índice del Euribor y   os precios de venta medios de la vivienda/m2  desde 2006 hasta el día actual y de las cotizaciones del Ibex35, con fines educativos. Se obtienen las cotizaciones con un programa en python mediante técnicas de webscraping contra el portal inmobiliario www.idealista.com y contra www.infobolsa.com

Idealista es uno de los portales inmobiliarios de referencia en el contexto estatal y probablemente uno de los mayores portales de compra venta en España.

Infobolsa.com es el portal de informción financiera de BME, Bolsas y Mercados Españoles.



## Miembros del equipo

Sergio Fernández Bertolin

Enrique Javier Andrés Orera


## Uso de técnicas avanzadas

Uso de 'pool' de user agents

Uso de retardos en las peticiones

Uso de Selenium para poder acceder al contenido de las tablas que se generan de forma dinámica y que de otra forma serían inaccesibles

Se gestionan usuarios y contraseñas


## Descripción de los ficheros


### Ficheros del código fuente
La extracción de datos se realiza mediante un script en código Python, escrito para funcionar con Python3: 

__euribordiario.py__  

Este código fuente genera un DataFrame de salida que se almacena en un fichero csv y una gráfica en formato PNG que permite interpretar los datos
El DataFrame generado tiene el siguiente formato:

| Index   |      Dia      | Euribor | precio_m2_Barcelona | precio_m2_Bilbao | precio_m2_Madrid | precio_m2_Sevilla | precio_m2_Valencia |  IBEX35  |
|---------|:-------------:|--------:|--------------------:|-----------------:|-----------------:|------------------:|-------------------:|---------:|
| 2473    | 20160104      | 0.058   | 3313                | 2814             | 2743             | 1778              | 1342               | 9313.200 |
| 2474    | 20160105      | 0.059   | 3313                | 2814             | 2743             | 1778              | 1342               | 9335.200 |

Donde __Index__ es un valor entero auto incremental, empezando en cero

__Dia__ es el dia en el que se ha registrado el valor, con el formato AAAAMMDD, donde las cuatro primeras cifras son el año, las dos siguientes el mes en formato numérico y las dos últimas el día del mes

__Euribor__ es el valor del índice del Euribor registrado ese día, en formato decimal

__precio_m2_Barcelona__ es el precio de venta medio por metro cuadrado en la ciudad de Barcelona

__precio_m2_Bilbao__ es el precio de venta medio por metro cuadrado en la ciudad de Bilbao

__precio_m2_Madrid__ es el precio de venta medio por metro cuadrado en la ciudad de Madrid

__precio_m2_Sevilla__ es el precio de venta medio por metro cuadrado en la ciudad de Sevilla

__precio_m2_Valencia__ es el precio de venta medio por metro cuadrado en la ciudad de Valencia

__IBEX35__ es la cotización del indice Ibex 35



### Fichero CSV
El DataFrame se almacena en un fichero csv, con el siguiente nombre:

__euribordiario.csv__

En el repositorio hay un fichero de ejemplo generado el 30 de octubre de 2020. 

### Fichero PNG
El código de Python también genera una gráfica con la representación de la evolución diaria del índice, llamada:  

__euribor.png__

En el repositorio hay una gráfica de ejemplo generada el 30 de octubre de 2020.

### Otros ficheros
PDF que contiene el documento de respuestas solicitado en la práctica_

__PDF/Práctica 1.pdf__ 

## Licencia
CC BY-NC-SA 4.0 License

Está licencia tiene los siguientes términos:

Atribución : debe otorgar el crédito correspondiente , proporcionar un enlace a la licencia e indicar si se realizaron cambios . Puede hacerlo de cualquier manera razonable, pero no de ninguna manera que sugiera que el licenciante lo respalda a usted o su uso.

No comercial: no puede utilizar el material con fines comerciales .

ShareAlike : si remezcla, transforma o construye sobre el material, debe distribuir sus contribuciones bajo la misma licencia que el original.

Terminos extraídos de https://creativecommons.org/licenses/by-nc-sa/4.0/
