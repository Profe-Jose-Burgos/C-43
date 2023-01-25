#!/usr/bin/env python
# coding: utf-8
'''-------------------- GESTIÓN DE BODEGA ------------------------'''

def guardar_json(datos):
    import json
    archivo=open('bodega_autos.json','w+')
    json.dump(datos,archivo,indent=4)

def start_bodega():
    bodega = {"sedan":{
            "nissan":{
              "modelo":"sentra",
              "year":2022,
              "potencia_HP":149,
              "rango_de_precio":[19950,22700],
              "consumo_MPG": 39,
              "tipo" : "gasolina",
              "plazas" : 5,
              "transmision": "automatico",
              },
            "honda":{
              "modelo":"accord",
              "year":2011,
              "potencia_HP":192,            
              "rango_de_precio":[26520,38450],
              "consumo_MPG": 47,
              "tipo": "hibrido",
              "plazas": 5,
              "transmision": "automatico"
              },
            "toyota":{
              "modelo":"corolla", 
              "year":2016,
              "potencia_HP":122,
              
              "rango_de_precio":[26520,38450],
              "consumo_MPG": 47,
              "tipo": "hibrido",
              "plazas": 5,
              "transmision": "automatico"
              },
            },
            
          "pickup":{
            "toyota":{
              "modelo":"hilux",
              "year":2017,
              "potencia_HP":122,
              
              "rango_de_precio":[45300,48000],
              "consumo_MPG": 26.72,
              "tipo": "diesel",
              "plazas": 2,
              "transmision": "automatico"
                    
                },
            "ford":{
              "modelo":"ranger",
              "year":2018,
              "potencia_HP":122,
              
              "rango_de_precio":[45300,48000],
              "consumo_MPG": 24.24,
              "tipo": "diesel",
              "plazas": 5,
              "transmision": "manual"
                    
                },
            "isuzu":{
              "modelo":"Dmax",
              "year":2019,
              "potencia_HP":122,
              
              "rango_de_precio":[71000],
              "consumo_MPG": 14.9,
              "tipo": "diesel",
              "plazas": 5,
              "transmision": "manual"      
                }


            },
          "camioneta":{
            "honda":{
              "modelo":"HR-V",
              "year":2016,
              "potencia_HP":119,
              
              "rango_de_precio":[26990,30990],
              "consumo_MPG": 46.1,
              "tipo": "gasolina",
              "plazas": 5,
              "transmision": "manual"
                    
                },
            "toyota":{
              "modelo":"highlander",
              "year":2017,
              "potencia_HP":122,
              
              "rango_de_precio":[36420,46075],
              "consumo_MPG":24.1,
              "tipo": "gasolina",
              "plazas": 5,
              "transmision": "automatico"
                    
                },
            "nissan":{
              "modelo":"X-Trail",
              "year":2014,
              "potencia_HP":163,
              
              "rango_de_precio":[42160,56510],
              "consumo_MPG": 44.3,
              "tipo": "hibrido",
              "plazas": 5,
              "transmision": "automatico"
              }
              },
          "coupé":{

            "bmw":{
              "modelo":"serie 8",
              "year":2014,
              "potencia_HP":350,
              
              "rango_de_precio":[103306,198481],
              "consumo_MPG": 22,
              "tipo": "electrico",                                                                                                                                                                         
      
              "plazas": "4",
              "transmision": "automatico"
                    
                },
            "subaru":{
              "modelo":"BRZ",
              "year":2017,
              "potencia_HP":163,
              
              "rango_de_precio":[42160,56510],
              "consumo_MPG": 44.3,
              "tipo": "hibrido",
              "plazas": 5,
              "transmision": "automatico"
              },
                    


            },
          "deportivo":{
            "nissan":{
              "modelo":"gtr nismo",
              "year":2017,
              "potencia_HP":592,
              
              "rango_de_precio":[106050,146.000],
              "consumo_MPG": 19.9,
              "tipo": "gasolina",
              "plazas": 4,
              "transmision": "automatico"
                    
                },
            "toyota":{
              "modelo":"gr supra",
              "year":2023,
              "potencia_HP":368,
              "rango_de_precio":[103306,198481],
              "consumo_MPG": 29.0,
              "tipo": "electrico",
              "plazas": "4",
              "transmision": "automatico"
                    
                },
            "corvette":{
              "modelo":"stingray",
              "year":2019,
              "potencia_HP":495,
              
              "rango_de_precio":[139999,159999],
              "consumo_MPG": 15,
              "tipo": "gasolina",
              "plazas": 2,
              "transmision": "automatico"      


              }
            }
  }
    guardar_json(bodega)
    
#________________________Main________________________

#Driver program

if __name__=='__main__':
    start_bodega()






