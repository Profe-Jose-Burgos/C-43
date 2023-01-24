''' CREADOR DEL MODELO DE IA - TEO BOT '''

''' LIBRERÍAS'''
import json
import pickle as pkl
import numpy as np
import nltk
import keras
from nltk.stem import WordNetLemmatizer
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense,Dropout
from tensorflow.keras.optimizers import SGD

# Palabras que se ignorarán
ignore_words = ["?","¿","!","¡"]
# Cargar ejemplos de interacción
data_file = open('intents.json').read()
intents  = json.loads(data_file)

# Tokenizador
def tokenizer():
    words  = []
    classes  = []
    documents  = []
    for intent in intents["intents"]:
      for pattern in intent["patterns"]:
        w = nltk.word_tokenize(pattern) # tokeniza
        words.extend(w)
        documents.append((w,intent["tag"]))
        if intent["tag"] not in classes :
            classes.append(intent["tag"])
    return words , classes, documents
# Lematizador

def lematizer(words,classes,documents):
    words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
    words3 = words
    print("Palabras luego de lematizar:", len(words))
    pkl.dump(words,open('words.pkl',"wb"))
    pkl.dump(classes,open('classes.pkl',"wb"))

    return words3

#Datos de entrenamiento
def trainig_sets(words,classes, documents):
    traning = []
    output_empty = [0]*len(classes)
    for doc in documents:
      bag = []
      patterns_words = doc[0]
      patterns_words = [stemmer.stem(words.lower()) for words in patterns_words if w not in ignore_words]
      for palabra in words:
        bag.append(1) if palabra in patterns_words else bag.append(0)
      output_row = list(output_empty)
      output_row[classes.index(doc[1])] = 1
      traning.append([bag,output_row])
      
    traning = np.array(traning,dtype=object)
    x_train = list(traning[:,0])
    y_train = list(traning[:,1])

    return x_train, y_train

def model_builder_TEO():
    model = Sequential()
    model.add(Dense(128, input_shape=(len(x_train[0]),), activation='relu')) 
    model.add(Dropout(0.5))

    model.add(Dense(64,activation='relu'))
    model.add(Dropout(0.5))

    model.add(Dense(len(y_train[0]),activation='softmax'))

    sgd = SGD(learning_rate = 0.01,decay = 1e-6,momentum = 0.9,nesterov = True)
     
    model.compile(loss="categorical_crossentropy",optimizer=sgd,metrics=["accuracy"])

    historial = model.fit(np.array(x_train),np.array(y_train),epochs= 300,batch_size=5,verbose=1)
    model.save("chatbot_model_TEO.h5",historial)
    print("Modelo creado con éxito")

def start_model():
    words, classes, documents = tokenizer()
    words3 = lematizer(words, classes, documents)
    x_train, y_train = trainig_sets(words3, classes, documents)
    model_builder_TEO(x_train, y_train)

###################### MAIN ##############################

from intents_reference import start_intents

# Controlador
if __name__ == '__main__':
    start_intents()
    start_model()
