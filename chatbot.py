'''-----------------------CHATBOT - TEO ------------------------ '''
# LIBRERÍAS
import nltk, json , pickle
import numpy as np
import random
from nltk.stem import SnowballStemmer
from tensorflow.keras.models import load_model
import sys

# sys.path.append(directorio pendiente)
# import gestinar_recomendacion as gestor

tipo_marca = []
features_user = []

stemmer = SnowballStemmer('spanish')

model = load_model("./chatbot_model_hackton.h5")
#intents = json.loads(open(!!!pendientes).read())
#words = pickle.load(open(pendiente,'rb'))
#classes = pickle.load(open(pendiente,'rb'))

#def clean_up
