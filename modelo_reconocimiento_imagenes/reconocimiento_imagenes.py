
from tensorflow.keras.models import load_model
import tensorflow_hub as hub
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import cv2


def cargar_modelo():
    # Recrea exactamente el mismo modelo solo desde el archivo 
    modelo = load_model(r'C:\Users\HP-LAPTOP\Documents\GitHub\C-43\modelo_reconocimiento_imagenes\IA_hackton.h5',custom_objects={'KerasLayer': hub.KerasLayer})
    return modelo

def categorizar(url):
    modelo = cargar_modelo()
    respuesta = requests.get(url)
    img = Image.open(BytesIO(respuesta.content))
    img = np.array(img).astype(float)/255

    img = cv2.resize(img, (224,224))
    prediccion = modelo.predict(img.reshape(-1, 224, 224, 3))

    ERROR_THRESHOLD = 0.60
    
    for i in prediccion[0]:
        if i >ERROR_THRESHOLD:
          return np.argmax(prediccion[0], axis=-1)

def hacer_prediccion(url):
    prediccion = categorizar(url)
  
    if prediccion == 0 : 
        prediccion = 'camioneta'
    elif prediccion == 1 : 
        prediccion = 'coupe'
    elif prediccion == 2 : 
        prediccion = 'deportivo'
    elif prediccion == 3 : 
        prediccion = 'pickup'
    elif prediccion == 0 : 
        prediccion = 'sedan'
    else:
        prediccion = "Ingrese una foto de un auto, por favor"

    print(prediccion)
    return prediccion

