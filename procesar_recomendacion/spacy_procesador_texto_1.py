#!/usr/bin/env python
# coding: utf-8

########################## LIBRERÍAS #########################################3
import spacy
from spacy.matcher import Matcher
import es_core_news_sm
import statistics as stats
import sklearn
from sklearn.neighbors import NearestNeighbors
import pandas as pd

'''--------------------- PROCESAMIENTO DE DATOS ---------------------'''
def get_year(df):
    dato = df.loc["año"][0]
    nlp = spacy.load('es_core_news_sm')
    doc = nlp(dato)
    print(doc)
    pattern2 = [{"LIKE_NUM":True}]
    
    matcher =  Matcher(nlp.vocab)
    matcher.add("dato", [pattern2])
    matches =  matcher(doc)
    print(matches)
    
    for match_id, start, end in matches:
        #obten el span resultante
        matched_span= doc[start:end]
        year = matched_span.text
        return int(year)
    
def get_potencia(df):
    dato = df.loc["potencia"][0]
    
    nlp = spacy.load('es_core_news_sm')
    doc = nlp(dato)
    print(doc)
    pattern2 = [{"LIKE_NUM":True}]
    
    matcher =  Matcher(nlp.vocab)
    matcher.add("dato", [pattern2])
    matches =  matcher(doc)
    print(matches)

    for match_id, start, end in matches:
        #obten el span resultante
        matched_span= doc[start:end]
        potencia = matched_span.text
        return int(potencia)
    
def get_precio_promedio(df):
    dato = df.loc["rango_precio"][0]
    
    nlp = spacy.load('es_core_news_sm')
    doc = nlp(dato)
    print(doc)
    pattern2 = [{"LIKE_NUM":True}]
    matcher =  Matcher(nlp.vocab)
    matcher.add("dato", [pattern2])
    matches =  matcher(doc)
    print(matches)

    for match_id, start, end in matches:
        #obten el span resultante
        matched_span= doc[start:end]
        precio_promedio = matched_span.text
        return float(precio_promedio)
    
def get_consumo(df):
    dato = df.loc["consumo"][0]
    
    nlp = spacy.load('es_core_news_sm')
    doc = nlp(dato)
    print(doc)
    pattern2 = [{"LIKE_NUM":True}]
    matcher =  Matcher(nlp.vocab)
    matcher.add("dato", [pattern2])
    matches =  matcher(doc)
    print(matches)

    for match_id, start, end in matches:
        #obten el span resultante
        matched_span= doc[start:end]
        consumo = matched_span.text
        return int(consumo)


def combustible_value(tipo):
    casos = ["gasolina","diesel","eléctrico","híbrido"]
    value = [0,1,2,3]
    
    if tipo in casos[o]:
        return value[0]
    elif tipo in casos[1]:
        return value[1]
    elif tipo in casos[2]:
        return value[2]
    elif tipo in casos[3]:
        return value[3]
    
def get_combustible(df):
    dato = df.loc["combustible"][0]
    nlp = spacy.load('es_core_news_sm')
    doc = nlp(dato)
    print(doc)
    pattern1 = [{'LOWER': {'IN':["gasolina","diesel","eléctrico","electrico","hibrido","híbrido"]}}]
    matcher =  Matcher(nlp.vocab)
    matcher.add("dato", [pattern1])
    matches =  matcher(doc)
    print(matches)
    
    for match_id, start, end in matches:
        #obten el span resultante
        matched_span= doc[start:end]
        combustible = matched_span.text
        df_value = combustible_value(combustible)
        return int(df_value)


def get_asientos(df):
    dato = df.loc["plazas"][0]
    nlp = spacy.load('es_core_news_sm')
    doc = nlp(dato)
    print(doc)
    pattern2 = [{"LIKE_NUM":True}]
    matcher =  Matcher(nlp.vocab)
    matcher.add("dato", [pattern2])
    matches =  matcher(doc)
    print(matches)
    for match_id, start, end in matches:
        #obten el span resultante
        matched_span= doc[start:end]
        asientos = matched_span.text
        return int(asientos)
    

def get_transmision_value(tipo):
    casos = ["manual","automática","automatica"]
    value = [0,1,1]
    
    if tipo in casos[0]:
        return value[0]
    elif tipo in casos[1]:
        return value[1]
    elif tipo in casos[2]:
        return value[2]
    

    
def get_transmision(df):
    dato = df.loc["transmisión"][0]
    
    nlp = spacy.load('es_core_news_sm')
    doc = nlp(dato)
    print(doc)
    pattern1 = [{'LOWER':{'IN':["manual", "automatica","automática"]}}]
    
    matcher =  Matcher(nlp.vocab)
    matcher.add("dato", [pattern1])
    matches =  matcher(doc)
    print(matches)
    for match_id, start, end in matches:
        #obten el span resultante
        matched_span= doc[start:end]
        tipo = matched_span.text
        transmision = get_transmision_value(tipo)
        return int(transmision)
    

######################Metodos principales###########

def get_df_raw(raw_text):
    df= pd.DataFrame(raw_text,columns=['text'], index=['año','potencia','rango_precio','consumo','combustible','plazas','transmisión'])
    return df

def get_data_user(df):
    
    lista_features = [get_year(df), get_potencia(df), get_precio_promedio(df),
                     get_consumo(df),get_combustible(df),get_asientos(df),
                     get_transmision(df)]
    print(f"Datos de recomendacion:{lista_features}")
    return lista_features


def ajustar_df(bodega_raw):
    print(bodega_raw)
    df_bodega = bodega_raw.copy()
    df_bodega["tipo"].replace(["gasolina","diesel","electrico","hibrido"],[0,1,2,3],inplace=True)
    df_bodega["transmision"].replace(["automatico","manual"],[0,1],inplace=True)
    promedio=[]
    for rango in df_bodega["rango_de_precio"]:
        prom = stats.mean(rango)
        promedio.append(prom)
    df_bodega.drop(["rango_de_precio"],axis=1,inplace=True)
    df_bodega.insert(3,"promedio_precio",promedio)
    return df_bodega


def recomendar_busqueda_df(m:list,df):
    datos_recomendar = df.iloc[:,[1,2,3,4,5,6,7]].values
    print(datos_recomendar)
    nn = NearestNeighbors(n_neighbors=1).fit(datos_recomendar)
    y = nn.kneighbors([m])
    auto = y[1][0][0]
    recomend = pd.DataFrame(df.iloc[auto])
    return recomend

    
    

###############  Main   ####################



def recomendacion_caracteristicas(entrada,bodega):
    df_datos = get_df_raw(entrada)
    ajuste_bodega =  ajustar_df(bodega)
    features = get_data_user(df_datos)
    
    resultado = recomendar_busqueda_df(features, ajuste_bodega)
    return resultado

#----------------------------------------------------------------------------------------------------
# Pendiente de Ajustar
'''if __name__ == '__chatbot__':
    
    recomendacion = recomendacion_caracteristicas(entrada,bodega):'''





