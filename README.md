# C-43

![TEO-BOT](/logos/teo.jpg)
## Chat Bot - TEO - Desarrolladores
* Joseph Jahir Delgado Corella 
* Jean Carlos Rodríguez Quintero
* Raúl Omar Gutierrez Becerra

 
## Funcionalidades: 

- TEO-BOT es un bot para atención al cliente para la empresa [Ralix Autos](https://jeanrodriguezq.github.io/index.html).
- Permite realizar recomendaciones a los usuarios en base a su selección. 
- Ya sea por medio de una busqueda directa en la bodega o una recomendación que mejor se aproxime a las características que desea el usuario - Beta -. 
- Además, en estado Beta se encuentra el procesamiento de una url de referencia para realizar recomendaciones realizando reconocimiento de imágenes y devolver un auto del mismo tipo en la bodega.

## Interacciones: 
Además de las recomendaciones, TEO-BOT proporciona un enlace con la página web de Ralix Autos donde se termina de concretar el pedido y la cita. 

## Contenido de Carpetas 

### Driver :
Controlador usado en Microsoft Edge Versión 109.0.1518.55 

### Gestión de Bodega:
gestionar_bodega.py se encarga de agregar elemento a la bodega del local 

### Main 
Aquí se encuentan los archivos principales del chatbot.Contiene el modelo de respuestas del chatbot y el controlador de sesiones. 

### Modelo de reconocimiento de imágenes:
Contiene el modelo entrenado para el reconocimiento de imágenes mediante una URL 

### Procesamiento de Características y Recomendaciones 
Contiene los archivos que procesan los datos que da el usuario a través de la librería spaCy y la bodega del local. 

### Zip: 
Contiene los elementos de entrenamiento del modelo de reconocimiento de imágenes.