#!/usr/bin/env python
# coding: utf-8
'''                     GESTION DE RECOMENDACIONES PARA EL USUARIO                      '''
''' ------------------------------- LIBRERÍAS -------------------------'''
import pandas as pd
from datetime import datetime as d_t
import pytz as tz
import json
import os
import matplotlib.pyplot as plt
import numpy as np
import sys

'''---------------------- LLAMAR UN PATH EXTERNO A LA CARPETA-------------------'''
#  Se llama el path de las carpetas con los scripts necesarios
sys.path.append(r'C:\Users\HP-LAPTOP\Documents\GitHub\C-43\procesar_recomendacion')
#sys.path.append(r'C:\Users\HP-LAPTOP\Documents\GitHub\C-43\modelo_reconocimiento_imagenes')

# Ruta donde se guardan la bodega de autos
path = r'C:\Users\HP-LAPTOP\Documents\GitHub\C-43\gestion_bodega\bodega_autos.json'

# Llamo los scripts desde las rutas agregadas
#import spacy_procesador_texto as spt
#import predictor_de_tipo as pdt

# Hora y fecha en Panamá: Se asigano zona horaria y retorna Hora de panamá
def time_in_pty():
    time_zone = "America/Panama"
    pty = tz.timezone(time_zone)
    date_pty = d_t.now(pty)
    f_date_pty = date_pty.strftime("%m_%d__%H_%M")
    return f_date_pty
# Abre el JSON
def abrir_json(ruta:str):
    data_file= open(ruta).read()
    intents=json.loads(data_file)
    return intents

# Convierte el JSON en un DF Multi-index
def json_to_multidf(dataframe):
    multi_df = pd.concat({k:pd.DataFrame(v).T for k, v in dataframe.items()}, axis=0)
    return multi_df

# Se crea la imagen que se envirá como recomendación al usuario. Se basa en la busqueda en la bodega.
def df_to_image(df,tipo):
    title_text = 'Consulta en Bodega'
    fecha= time_in_pty()
    fig_background_color = 'skyblue'
    fig_border = 'steelblue'
    data= df
    archivo= f'C:/Users/HP-LAPTOP/Documents/GitHub/C-43/consultas_realizadas/Consulta_{tipo}_{fecha}.png'
    
    column_headers = data.columns
    row_headers = [x for x in data.index]
    
    cell_text=[]
    for row in data.values:
        cell_text.append(row)
        
    rcolors = plt.cm.BuPu(np.full(len(row_headers),0.1))
    ccolors = plt.cm.BuPu(np.full(len(column_headers),0.1))
    
    plt.figure(linewidth=2,
              edgecolor=fig_border,
              facecolor=fig_background_color,
              tight_layout={'pad':1},
              #figsize=(5,3)
              )
    the_table = plt.table(cellText=cell_text,
                         rowLabels=row_headers,
                         rowColours=rcolors,
                         rowLoc='right',
                         colColours=ccolors,
                         colLabels=column_headers,
                         loc='center')
    the_table.scale(1,1.5)
    
    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.box(on=None)
    
    plt.suptitle(title_text)
    
    plt.figtext(0.95, 0.05, fecha, horizontalalignment='right', size=6, weight='light')
    
    plt.draw()
    
    fig=plt.gcf()
    plt.savefig(archivo,
               edgecolor=fig.get_edgecolor(),
               facecolor=fig.get_facecolor(),
               dpi=150
               )
    
    return archivo


'''' ------------------------- Busqueda directa en bodega -------------------------------- '''
#Buscará en el DF generado de la bodega
def buscar_bodega(datos, df):
    car_serie= pd.DataFrame(df.loc[datos[0]].loc[datos[1]])
    return car_serie

# Preparar respuesta de busqueda
# Genera un DF del auto encontrado en la Bodega
def preparar_respuesta_busqueda(df):
    df.index=['Modelo', 'Año','Potencia', 'Rango de presio(US Dolar)', 'Consumo de combustible',
             'Tipo de Combustible', 'Plazas', 'Transmisión']
    df.columns= [df.columns[0].title()]
    df.replace()
    return df


''' ---------------------------------- Main ------------------------------------ '''

bodega_json =  abrir_json(path)


df_bodega =  json_to_multidf(bodega_json)


################## Funcion Busqueda Directa #################
# Se integran las funciones anteriores
def busqueda_directa(texto:list):
    auto = buscar_bodega(texto,df_bodega)
    datos = preparar_respuesta_busqueda(auto)
    resultado = df_to_image(datos, "direct")
    print(f'Salida:{resultado}')
    return resultado # Retorna la ruta del archivo png creado

##################### Funcion Busqueda Caracteristicas ###########
# Se conecta al path para llamar la función recomendacion_caracteristicas desde spt
def busqueda_caracteristicas(entrada):
    auto=spt.recomendacion_caracteristicas(entrada, df_bodega)
    resultado=df_to_image(auto,"recomend")
    print(f'Salida:{resultados}')
    return resultado # Retorna la ruta del archivo png creado

############# Funcion de busqueda Url ##########
# Recibe la predición del modelo de reconocimiento de imágenes para retornar al usuario
def referencia_url(entrada:int,df):
    tipo=entrada
    nt=[]
    if tipo == 4:
        nt.append("sedán")
    elif tipo == 3:
        nt.append('pickup')
    elif tipo == 2:
        nt.append('deportivo')
    elif tipo == 0:
        nt.append('camioneta')
    elif tipo == 1:
        nt.append('coupe')
    print(nt)
    
    df.columns = ['Modelo', 'Año','Potencia(HP)', 'Rango de Precios', 'Consumo de combustible', 'N° Asientos', 'Transmision' ]
    
    df_result=pd.DataFrame(df.loc[nt[0]])
    return df_resultado 

# Llama al modelo de reconocimiento de imágenes para relizar una predicción 
def busqueda_url(url):
    entrada = pdt.hacer_prediccion(url)
    auto = referencia_url(entrada,df_bodega)
    resultado = df_to_image(auto,"url")
    print(f'Salida:{resultados}')
    return resultado # Retorna la ruta del archivo png creado

# Prueba
usuario=['sedán','nissan']
busqueda_directa(usuario)
'''
try_it = ['año del auto: 2019','235 caballos de fuerza',  27900 dolares,'40 millas por galon', 'gasolina ', '4 asientos', 'automatica']
busqueda_caracteristicas(try_it, df_bodega)'''

#busqueda_url("https://www.nissan-cdn.net/content/dam/Nissan/mexico/vehicles/NP300/my21/vlp/np300-2021_blanca-exterior-piloto.jpg.ximg.l_full_h.smart.jpg")








    
    

