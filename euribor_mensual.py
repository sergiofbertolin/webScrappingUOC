# -*- coding: utf-8 -*-
"""
Spyder Editor

Script para extraer el euribor mensual de la página web de Idealista
Allí hay almacenados los datos del Euribor desde Enero de 1999 hasta 
el mes anterior a la extracción
"""

# Importación de librerías necesarias
import requests as rq
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import locale
import calendar

# Necesario para calendar (configuración local a hora española)
locale.setlocale(locale.LC_ALL, 'es_ES.utf8')

# Creamos el request de la html
req = rq.get('https://www.idealista.com/news/euribor/historico-diario/')

# Generamos el objeto de tipo BeautifulSoup y extraemos los datos del texto HTML
# del requestd e idealistas con él
soup = BeautifulSoup(req.text,"lxml")

# Inicializo todas las variables
i=0
anio=''
mes=''
valor=''
indice=''
euribor={}

# Itero dentro del texto extraído para almacenar los valores siguientes:
# Año, mes y valor del índice del Euribor
# Se almacenan los resultados en el diccionario euribor cuya llave
# es una combinación del año y el mes en formato numérico
for sub_heading in soup.find_all('td'):
    i=(i+1)%3
    if i==1: 
        anio=sub_heading.text
    elif i==2:            
        mes=sub_heading.text
        # obtenemos el número del mes apartir del nombre utilizando calendar
        numeroMes= '{:02d}'.format(list(calendar.month_name).index(mes.lower()))
        indice=anio+numeroMes       
    elif i==0: 
        valor=sub_heading.text
        euribor[indice]=(anio,mes,valor)

# Almacenamos los valores como DataFrame         
eur=pd.DataFrame(euribor).transpose()
eur=eur.rename(columns={0:'Año',1:'Mes',2:'Valor'})

# Generamos un csv con los datos mensuales
eur.to_csv('euribor_mensual.csv')

#eur.plot(x='Index', y='Valor')


