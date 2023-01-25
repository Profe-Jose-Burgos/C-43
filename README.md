# C-43

## Chat Bot - Teo
Jean Carlos Rodríguez Quintero -Joseph Jahir Delgado Corella -Raúl Omar Gutierrez Becerra

 
##Funcionalidades: 

Teo-Bot permite realizar recomendaciones a los usuarios en base a su selección. 
Ya sea por medio de una busqueda directa en la bodega o una recomendación que mejor se aproxime a las características que desea el usuario. 
Además, en estado Beta se encuentra el procesamiento de una url de referencia para realizar recomendaciones realizando reconocimiento de imágenes.

Interacciones: 
Además de las recomendaciones,Teo-Bot puede incluir información referente a horarios de atención y ubicación del local a los clientes.  

Contenido de Carpetas 

Driver :
Controlador usado en Microsoft Edge Versión 109.0.1518.55 

Gestión de Bodega:
gestionar_bodega.py se encarga de agregar elemento a la bodega del local 

Main 
Aquí se encuentan los archivos principales del chatbot.Contiene el modelo de respuestas del chatbot y el controlador de sesiones. 

Modelo de reconocimiento de imágenes:
Contiene el modelo entrenado para el reconocimiento de imágenes mediante una URL 

Procesamiento de Características y Recomendaciones 
Contiene los archivos que procesan los datos que da el usuario a través de la librería spaCy y la bodega del local. 

Zip: 
Contiene los elementos de entrenamiento del modelo de reconocimiento de imágenes.