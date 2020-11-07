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
import time
from zipfile import ZipFile
from selenium import webdriver

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


controlmesactual = True

# Creamos listas donde guardaremos los días y los valores
dias = []
valores = []
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
        sleep_secs = random.randrange(2, 4)
        time.sleep(sleep_secs)

        # Descargamos el sitio web de interés
        html = requests.get(url, headers=headers)

        soup = bsoup(html.content)

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


# Función para extraer los precios medios por m2 de una Ciudad.
# Se trata de un contenido dinámico.
# Utilizando la libreria Selenium, podremos acceder al marco donde se encuentra la tabla que se genera de forma
# dinámica

def precios_ciudad(dias, ciudad):
    ciudad_url_dict = {
        'Barcelona': 'https://www.idealista.com/sala-de-prensa/informes-precio-vivienda/venta/cataluna/barcelona-provincia/barcelona/historico/',
        'Bilbao': 'https://www.idealista.com/sala-de-prensa/informes-precio-vivienda/venta/euskadi/vizcaya/bilbao/historico/',
        'Madrid': 'https://www.idealista.com/sala-de-prensa/informes-precio-vivienda/venta/madrid-comunidad/madrid-provincia/madrid/historico/',
        'Sevilla': 'https://www.idealista.com/sala-de-prensa/informes-precio-vivienda/venta/andalucia/sevilla-provincia/sevilla/historico/',
        'Valencia': 'https://www.idealista.com/sala-de-prensa/informes-precio-vivienda/venta/comunitat-valenciana/valencia-valencia/valencia/historico/'}

    url_ciudad = ciudad_url_dict[ciudad]

    # Opciones para el driver de Selenium
    options = webdriver.ChromeOptions()

    # Headless impide que el navegador Crhrome controlado por python se muestre en pantalla
    # options.add_argument('headless')

    # Ignoramos posibles errores
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')

    # Elegimos el user-agent del pool de user-agents userAgents
    options.add_argument('user-agent=%s' % (random.choice(userAgents)))

    # Creamos objeto webdriver (selenium), que es el que realiza la petición con las opciones anteriormente establecidas
    try:
        web_driver = webdriver.Chrome(options=options)
    except:
        # Si no podemos crear el objeto webdriver es porque no tenemos el driver Chrome.
        # Lo descargamos y descomprimimos.
        print("Descargamos y descomprimimos driver Chrome")
        driver = requests.get('http://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_win32.zip')

        with open('chrome_driver.zip', 'wb') as d:
            d.write(driver.content)

        with ZipFile('chrome_driver.zip', 'r') as zfile:
            try:
                zfile.extractall()
            except:
                print("Something else went wrong")
        # Una vez descargado y descomprimido el driver Chrome, creamos objeto webdriver (selenium), que es el que
        # realiza la petición con las opciones anteriormente establecidas.
        web_driver = webdriver.Chrome(options=options)

    # Espaciado entre peticiones (de 10 a 15 segundos)
    sleep_secs = random.randrange(10, 16)
    time.sleep(sleep_secs)

    # Tiempo de espera del driver para asegurarse de que carga la página en su totalidad, 5 segundos
    seconds = 5
    web_driver.implicitly_wait(seconds)
    # Se abre una nueva petición a la página deseada
    web_driver.get(url_ciudad)

    # Buscamos el elemento 'iframe' que es el marco donde se encuentra la tabla dinámica que queremos obtener.
    frame = web_driver.find_element_by_tag_name('iframe')
    # Cambiamos al marco
    web_driver.switch_to.frame
    # Obtenemos el marco
    web_driver.page_source

    soup_tabla_precios = bsoup(web_driver.page_source, "lxml")

    anyomes = []
    precio_m2 = []
    contador = 0
    for dato_tabla_precios in soup_tabla_precios.body.tbody.find_all('td'):
        contador += 1
        if contador % 5 == 1:
            a = dato_tabla_precios.string.split()
            for i in range(1, 13):
                if calendar.month_name[i] == a[0].lower():
                    anyomes.append("%s%s" % (a[1], '{:02d}'.format(i)))
        elif contador % 5 == 2:
            b = dato_tabla_precios.string.split()
            if b[0] == 'n.d.':
                precio_m2.append(np.NaN)
            else:
                precio = b[0].replace(".", "")
            precio_m2.append(precio)

    diccionario = dict(zip(anyomes, precio_m2))

    precio_m2_2 = []
    for i in range(len(dias)):
        try:
            precio_m2_2.append(diccionario[dias[i][0:6]])
        except:
            precio_m2_2.append(np.NaN)

    # Cerramos driver
    web_driver.close()

    return precio_m2_2


ciudades = ['Barcelona', 'Bilbao', 'Madrid', 'Sevilla', 'Valencia']

# Creamos diccionario de listas con las listas días, valores, precios_m2_Barcelona, precios_m2_Bilbao,
# precios_m2_Madrid, precios_m2_Sevilla, precios_m2_Valencia
euribor_dict = {'Dia': dias[::-1], 'Valor': valores[::-1],
                'precio_m2_' + ciudades[0]: precios_ciudad(dias, ciudades[0])[::-1],
                'precio_m2_' + ciudades[1]: precios_ciudad(dias, ciudades[1])[::-1],
                'precio_m2_' + ciudades[2]: precios_ciudad(dias, ciudades[2])[::-1],
                'precio_m2_' + ciudades[3]: precios_ciudad(dias, ciudades[3])[::-1],
                'precio_m2_' + ciudades[4]: precios_ciudad(dias, ciudades[4])[::-1]}

# Creamos un DataFrame para almacenar el diccionario de listas
euribor_df = pd.DataFrame(euribor_dict)

# Almacenamos los resultados de nuestro dataset en un csv
euribor_df.to_csv('euribordiario.csv')

# Representamos gráficamente la evolución temporal del Euribor
print(euribor_df)

f, ax = plt.subplots()
ax.plot(euribor_df.index, euribor_df.Valor)
ax.set(xlabel='Fecha (AñoMesDia)', ylabel='tasa de interés del Euribor (%)',
       title='Evolución diaria del Euribor desde 1999')
plt.xticks(np.arange(euribor_df.shape[0])[::150], euribor_df.Dia[::150], rotation=90)

plt.show()

# Almacenamos la gráfica
f.savefig("euribor.png")

