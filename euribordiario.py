# -*- coding: utf-8 -*-
"""
Script para extraer el euribor diario de la página web de Idealista
Allí hay almacenados los datos del Euribor desde Enero de 1999 hasta 
el mes anterior a la extracción
"""

# Importación de librerías necesarias

import locale
import datetime
import random
from bs4 import BeautifulSoup as bsoup
import requests
import calendar
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import time

# Necesario para calendar (configuración local a hora española)
locale.setlocale(locale.LC_ALL, 'es_ES.utf8')

# Lista de user agents

userAgents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]

# Fecha actual
now = datetime.datetime.now()

anyo = int(now.strftime("%Y"))
mes = int(now.strftime("%m"))
dia = int(now.strftime("%d"))

controlmesactual = True

# Creamos listas donde guardaremos los días y los valores
dias= []
valores =[]
# Para cada año
while anyo >= 1999:
    # Para cada mes
    while mes > 0:
        if controlmesactual:
            url = "https://www.idealista.com/news/euribor/mensual/mes-actual/"
            controlmesactual = False
        else:
            url = "https://www.idealista.com/news/euribor/mensual/%s-%d/" % (calendar.month_name[int(mes)], anyo)

        # Seleccionamos user agent aleatoriamente
        userAgent = random.choice(userAgents)

        # Cargamos cabeceras por defecto
        headers = requests.utils.default_headers()

        # Actualizamos cabeceras con el User-Agent aleatorio
        headers.update({'User-Agent': userAgent})
        
        # Espaciado entre peticiones (2 ó 3 segundos)
        sleep_secs = randrange(2,3)
        time.sleep(sleep_secs)

        # Descargamos el sitio web de interés
        html = requests.get(url, headers=headers)

        soup = bsoup(html.content)

        # Se crea una lista vacía y mediante un bucle for, guardamos los títulos de la tabla que se quiere almacenar

        tablehead = []

        for header in soup.body.thead.tr.children:
            tablehead.append(header.text)

        contador = 0

        for dato in soup.body.tbody.find_all('td'):
            contador = contador + 1
            if contador % 2 == 1:
                # fecha
                fecha = "%d%s%s" % (anyo, '{:02d}'.format(mes), '{:02d}'.format(int(dato.string)))
                # Añadimos la fecha a la lista
                dias.append(fecha)
                print(fecha)
            else:
                # euribor
                euribor = dato.string[:-1].replace(",", ".")
                # Añadimos el euribor a la lista
                valores.append(float(euribor))
                print(float(euribor))

        mes = mes - 1

    anyo = anyo - 1
    mes = 12

# Creamos un DataFrame para almacenar los pares de conjuntos días, valores
euribordf = pd.DataFrame(list(zip(dias[::-1], valores[::-1])), columns=['Dia', 'Valor'])

# Almacenamos los resultados de nuestro dataset en un csv
euribordf.to_csv('euribordiario.csv')

# Representamos gráficamente la evolución temporal del Euribor
print(euribordf)

f, ax = plt.subplots()
ax.plot(euribordf.index, euribordf.Valor)
ax.set(xlabel='Fecha (AñoMesDia)', ylabel='tasa de interés del Euribor (%)', title='Evolución diaria del Euribor desde 1999')
plt.xticks(np.arange(euribordf.shape[0])[::150], euribordf.Dia[::150], rotation=90)

plt.show()

# Almacenamos la gráfica
f.savefig("euribor.png")

