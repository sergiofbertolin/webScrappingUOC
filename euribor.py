# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests as rq
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import locale
import calendar

# Necesario para calendar
locale.setlocale(locale.LC_ALL, 'es_ES.utf8')

req = rq.get('https://www.idealista.com/news/euribor/historico-diario/')
soup = BeautifulSoup(req.text,"lxml")

i=0
anio=''
mes=''
valor=''
indice=''

# He quitado el método porque se puede hacer lo mismo utilizando el módulo calendar
# que viene con python

euribor={}

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
eur=pd.DataFrame(euribor).transpose()
eur=eur.rename(columns={0:'Año',1:'Mes',2:'Valor'})
eur.to_csv('prueba.csv')

#eur.plot(x='Index', y='Valor')

# Perfecto, así sacamos el valor del euribor a fin de mes

# Echale un vistazo a la implementación que he hecho para sacar el valor todos los días
# euribordiario.py
