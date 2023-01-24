''' ---------------------------- Conexión con Whatsapp Web ------------------------------ '''
#Navegador:  Microsoft Edge
#Version de Edge: 109.0.1518.61
# Enlace para driver: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

#---------------- LIBRERÍAS -------------------
# Librería Selenium - Versión:4.7.2
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

#--------------- DEFINIR SESIÓN ---------------
driver = webdriver.Edge("./Driver/msedgedriver.exe")
# Revisar DeprecationWarning: executable_path has been deprecated, please pass in a Service object

executor_url = driver.command_executor._url
session_id = driver.session_id
driver.get("https://web.whatsapp.com/")

print("Session ID:"+session_id)
print("Executor URL:"+executor_url)

# Almacenar en un archivo text el Id y el Local Host de la sesión
with open("./whatsapp_session.txt","w") as text_file:
    text_file.write(f"{executor_url}\n")
    text_file.write(session_id)

# Verifica si la sesión es nueva
def new_command_execute(self,command,params=None):
    if command == "newSession":
        return {'success':0, 'value': None, 'sessionId': session_id}
    else:
        return org_command_execute(self,command,params)

# Genera el controlador 
def crear_driver_session(session_id,executor_url):
    org_command_execute = RemoteWebDriver.execute
    RemoteWebDriver.execute = new_command_execute

    new_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    new_driver.session_id = session_id

    RemoteWebDriver.execute = org_command_execute

    return new_driver

# Inicializador del administrador de sesión
def iniciar_mantener_sesion():
    driver2 = crear_driver_session(session_id,executor_url)
    print(f"Driver 2 URL : {driver2.current_url}")

#-------------------------------- MAIN ------------------------------------
    
if __name__ == '__main__':
    iniciar_mantener_sesion()
