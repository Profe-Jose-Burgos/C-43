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
intents = json.loads(open('./intents.json').read())
words = pickle.load(open('./words.pkl','rb'))
classes = pickle.load(open('./classes.pkl','rb'))

def clean_up_sentences(sentence):
    # Tokenizamos la entrada
    sentence_words = nltk.word_tokenize(sentence) # Tokens de la oración
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words] # Lematización
    return sentence_words

# Lazos entre la entrada del usuario y la referencia
def bow(sentence,words,show_details = True):
    sentence_words = clean_up_sentences(sentence)
    bag=[0]*len(words)
    for i in sentence_words:
        for j,w in enumerate(words):
            if w == i:
                bag[j]=1 # True si la palabra verificada está en la posición del vocabulario generado
                print("Encontrado en Bolsa:",w)
    return(np.array(bag))
'''----------------- PREDICCIONES CON MODELO ENTRENADO -----------------------'''
def predict_class(sentence, model):
    # Procesamiento (p)
    p = bow(sentence, words, show_details = False)
    print(p)

    #Busca en la bolsa

    res = model.predict(np.array([p]))[0]
    print(res)
    # Se busca la eficacia del modelo (probabilidad de que la palabra corresponda a una etiqueta)
    # res es la eficacia según el modelo entrenado.
    # [0] retorna la palabra
    # [1] retorna la etiqueta

    ERROR_THRESHOLD = 0.35 # UMBRAL DE COINCIDENCIAS

    # Results recibe una lista [1,0,0,1] desde el modelo
    results = [[i,r] for i,r in enumerate(res) if r > ERROR_THRESHOLD]
    # Si la probabilidad de la etiqueta es > que 35%, se determinará como válida

    # r[0] = Tag
    # r[1] = probabilidad de ese tag

    # Ordenar por pesos de probabilidad
    results.sort(key = lambda x: x[1], reverse = True)

    return_list = []

    for r in results:
        return_list.append({'intent':classes[r[0]], 'probability' : str(r[1])})

    print("Lista de retorno:", return_list)

    return return_list

'''----------------  RESPUESTAS PARA EL USUARIO BASADAS EN LAS ETIQUETAS  -----------------'''

def get_response(ints, intents_json,text):
    # Respuestas basadas en los intents (ejemplares) proporcionados al modelo.
    # Además guarda la informaión para realizar la busqueda en bodega.

    global tipo_marca
    global features_user
    # Datos para organizar las entradas del usuario
    user_data = ["anho_del_auto", "caballos_de_fuerza", "precio_esperado",  
               "consumo_combustible", "tipo_de_combustible", "número_de_asientos",  
               "tipo_de_transmisión" 
                 ]
    # Obtención del tag de la entrada proporcionada por el usuario ints[0]
    tag = ints[0]['intent']
    # Lista de ejemplares de referencia
    list_of_intents =  intents_json["intents"]

    for i in list_of_intents:
        if(i["tag"]==tag):
            result = random.choice(i["responses"]) # respuesta aleatoria del grupo posible
            if(tag == "tipo" or tag == "marca"):
                tipo_marca.append(text)     # BETA # Guarda la información dada por el usuario
            if(len(tipo_marca)>1): # Condición provisional
                print("Buscando en bodega")
                result = gest.busqueda_directa(tipo_marca) # Llama la función busqueda_directa
            if(tag in user_data):
                features_user.append(text)
            if(tag == "recomendar ahora"):
                print(f"Preparando recomendación de {features_user}")
                result = gest.busqueda_caracteristicas(features_user)
            if (tag == "url"):
                print("Realizando busqueda por imagen")
                result = gest.busqueda_url(text)
            else:
                break
    return result
    
''' ---------------- ENVÍO DE RESPUESTA DEL CHATBOT ------------------ '''
def chatbot_response(text):
    ints = predict_class(text,model)
    print(ints) # Ejemplar de la entrada del usuario

    res = get_response(ints,intents,text) # Procesamiento de la respuesta
    return res

########################## PRUEBAS EN CONSOLA ##########################################

def start_bot():
    text_us = ""
    print("Bienvenido.\n Para salir, escriba Salir:")

    while text_us != "Salir":
        text_us = input()
        res = chatbot_response(text_us)
        print(res)

############################## CHAT BOT - TEO ##########################################
# Función principal ejecutora
def bot(text_us):
    res = chatbot_response(text_us)
    return res

############################## MAIN - CHAT BOT - TEO #####################################
if __name__ == '__main__':
    # Consola
    start_bot()

    # Integración Whatsapp
    answer = bot(texto_us)
