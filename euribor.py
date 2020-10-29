# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests as rq
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
 
req = rq.get('https://www.idealista.com/news/euribor/historico-diario/')
soup = BeautifulSoup(req.text,"lxml")

i=0
anio=''
mes=''
valor=''
indice=''

def switch_mes(argument):
    switcher = {
        'Enero': '01',
    	'Febrero': '02',
    	'Marzo': '03',
    	'Abril': '04',
    	'Mayo': '05',
    	'Junio': '06',
    	'Julio': '07',
        'Agosto': '08',
        'Septiembre': '09',
        'Octubre': '10',
        'Noviembre': '11',
        'Diciembre': '12'
    }
    return switcher.get(argument, "Invalid month")

euribor={}

for sub_heading in soup.find_all('td'):
    i=(i+1)%3
    if i==1: 
        anio=sub_heading.text
    elif i==2:            
        mes=sub_heading.text
        indice=anio+switch_mes(mes)       
    elif i==0: 
        valor=sub_heading.text
        euribor[indice]=(anio,mes,valor)
eur=pd.DataFrame(euribor).transpose()
eur=eur.rename(columns={0:'Año',1:'Mes',2:'Valor'})
eur.to_csv('prueba.csv')

#eur.plot(x='Index', y='Valor')





