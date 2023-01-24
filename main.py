''' ------------------------- MAIN  - TEO --------------------------'''
#Versiones Librerías

# -------------------- LIBRERÍAS ----------------------------
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
import re # Expresiones regulares
from unicodedata import normalize # Normalizar caracteres del idioma Español
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#-------------------------------------------------------------
import os
import autoit

##############################################################
#------------------------ADMINISTRAR SESIÓN----------------------------

ruta_archivo = "./whatsapp_session.txt"
driver = webdriver

def crear_driver_session():
    # Abrir el archivo de Sesión guardado
    with open(ruta_archivo) as fp:
        for numb , line in enumerate(fp):
            if numb == 0:
                executor_url = line
            if numb == 1:
                session_id = line
    def new_command_execute(self,command,params=None):
        if command == "newSession":
            return {'success':0, 'value': None, 'sessionId': session_id}
        else:
            return org_command_execute(self,command,params)

    org_command_execute = RemoteWebDriver.execute
    RemoteWebDriver.execute = new_command_execute

    new_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    new_driver.session_id = session_id

    RemoteWebDriver.execute = org_command_execute

    return new_driver


'''------------------------- SELECCIÓN Y PREPARACIÓN DEL MENSAJE ----------------------------'''
def normalizar(mensaje:str):
    mensaje = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",
                     normalize( "NFD", mensaje), 0, re.I)
    return normalize('NFC', mensaje) # Elimina tildes y normaliza el texto para evitar errores



'''------------------------- BUSQUEDA DE MENSAJES EN UN CHAT ----------------------------'''
# Requiere actualización constante debido a cambios en la web oficial
def identificar_mensajes():
    # Busca la lista de mensajes recibidos en el chat abierto
    element_box_message = driver.find_elements(By.CLASS_NAME,"_27K43")
    # Obtiene la posición del último msj de la lista de chats recibidos
    posicion = len(element_box_message)-1
    # Obtiene el elemento del último msj recibido
    element_message = element_box_message[posicion].find_elements(By.CLASS_NAME,"_21Ahp")
    # Obtiene el texto del último msj recibido y lo ajusta a minúsculas
    mensaje = element_message[0].text.lower().strip()
    print('MENSAJE ENTRANTE:', mensaje)

    return normalizar(mensaje)
def verificar_mensajes_pendientes(chat):
    # Verificar si existen mensajes pendientes.
    try:
        # Compara el elemento de la página web que tiene la clase para un mensaje nuevo.
        icono_mensajes = chat.find_elements(By.CLASS_NAME,"_1pJ9J").text
        msj_leer = re.findall('\d+',icono_mensajes)
        # Verifica la clase del círculo de mensajes. Si corresponde y no regresa decimales, retorna pendiente = Verdadero
        if len(msj_leer) != 0:
            pendiente = True
        # Verifica la clase del círculo de mensajes. Si NO corresponde y regresa decimales, retorna pendiente = False
        else:
            pendiente = False

    except:
        pendiente = False

    return pendiente



'''------------------------- BUSQUEDA E INTERACCION CON GRUPOS DE CHATS ----------------------------'''
def buscar_chats():
    print("Buscando Chats")
    sleep(5)

    # Test

    if len(driver.find_elements(By.CLASS_NAME,"zaKsw")) == 0:
    # Cuando ningun chat está abieto
        print("Conversación Abierta")
        mensaje = identificar_mensajes()
        if mensaje != None:
            return True
    else:
        chats = driver.find_elements(By.CLASS_NAME,"_1Oe6M")
        # Primer mensaje de la lista de mensajes a la izquierda
        print("Chats en cola:", len(chats))

        for chat in chats:
            print("Detectando Mensajes sin Leer ahora")
            # Busca el círculo de chat recibido
            chat_mensajes = chat.find_elements(By.CLASS_NAME,'_1pJ9J')

            if len(chat_mensajes) == 0:
                print('Chats Atendidos') # Si el chat ya fue abierto, continua al siguiente chat
                continue
            else:
                chat.click() # Abre el chat si no estaba abierto
                return True

            pendiente_respuesta = verificar_mensajes_pendientes(chat)
            # Verifica si exiten msj por leer con la función "verificar_mensajes_pendientes"

            if pendiente_respuesta:
                chat.click()
                sleep(2)
                return True
            else:
                print("Chats atendidos")
                continue
        return False

def preparar_respuesta(mensaje:str):
    print("Preparando la respuesta")
    # Se encarga de generar una respuesta. Aquí se integra el bot en el funcionamiento final.
    # Test --------------------------
    if mensaje.__contains__("hola"):
        respuesta = "Hola\nSoy un Bot"
    elif mensaje.__contains__("gracias"):
        respuesta = "Estamos para servirle"
    else:
         respuesta = "Patrón no detectado"

    # Final --------------------------

    #respuesta = bot(mensaje)

    return respuesta

def procesar_mensaje(mensaje:str):
    # Busqueda de la caja de input para los mensajes de salida
    chat_box = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')

    respuesta = preparar_respuesta(mensaje) # Se refiere a la función anterior

    chat_box.send_keys(respuesta, Keys.ENTER) # Envía la respuesta del Bot tras procesarla
    sleep(2)
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    print("Respuesta:", respuesta)
        
def whatsapp_bot_init():
    global driver
    driver = crear_driver_session()
    espera = 1

    while espera == 1:
        espera = len(driver.find_elements(By.CLASS_NAME, "_3S2GF"))
        sleep(8) # Espera para Login
        print("Inicio de sesion:", espera)

    while True:
        if not buscar_chats():
            sleep(5)
            continue
        
        msj_recibido = identificar_mensajes()

        if msj_recibido == None:
            continue
        else:
            procesar_mensaje(msj_recibido)


#--------------------------------------- MAIN --------------------------------------------
from admin_sesion import iniciar_mantener_sesion
#from chatbot import bot

#if __name__ == '__main__':
iniciar_mantener_sesion()
sleep(4) # Se debe considerar la rapidez del sistema en la computadora ejecutora. Sino, retorna un error.
whatsapp_bot_init()

    
        
    
    
