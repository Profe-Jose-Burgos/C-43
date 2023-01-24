import json

def guardar_json():
    archivo = open("intents.json","w")
    json.dump(datos, archivo, indent=4)

def start_intents():

    biblioteca = {
        "intents": [
            {
                "tag": "saludos",
                "patterns": [
                    "hola",
                    "buenos dias",
                    "buenas tardes",
                    "buenas noches",
                    "como estas",
                    "hay alguien ahi?",
                    "hey",
                    "saludos",
                    "que tal"
                ],
                "responses": [
                    "Hola soy Teo , tu asesor de compras para tu futuro autom.\n ¿En qué puedo ayudarte? "
                    "Qué tal, soy Teo, tu asesor de compras de tu futuro auto.\n ¿En qué puedo ayudarte? "
                ],
                "context": [
                    ""
                ]
            },
            {
                "tag": "compras",
                "patterns": [
                    "consultar precios",
                    "comprar un auto",
                    "averiguar precio",
                    "busco un coche",
                    "informacion",
                    "necesito ayuda con",
                    "me puede colaborar",
                    "busco un auto",
                    "que carros tienen"
                ],
                "responses": [
                    "Perfecto, ¿Quieres probar una busqueda directa, una recomendacion basada en características?"
                ],
                "context": [
                    ""
                ]
            },
            {
                "tag": "busqueda_directa",
                "patterns": [
                    "busqueda directa",
                    "directo",
                    "de inmediato",
                    "busqueda inmediata"
                ],
                "responses": [
                    "¿Qué tipo de vehículo te gustaría. Por ejemplo: sedán, pickup, camioneta..."
                ],
                "context": [
                    ""
                ]
            },
            {
                "tag": "tipo",
                "patterns": [
                    "sedan",
                    "pickup",
                    "camioneta",
                    "coupe",
                    "deportivos"
                ],
                "responses": [
                    "¿Alguna marca en particular?",
                    "¿Tiene alguna marca en mente?",
                    "¿Qué marca le gustaría?"
                ],
                "context": [
                    ""
                ]
            },
            {
                "tag": "marca",
                "patterns": [
                    "nissan",
                    "honda",
                    "toyota",
                    "ford",
                    "isuzu",
                    "audi",
                    "bmw",
                    "subaru",
                    "mitsubihi",
                    "corvette"
                ],
                "responses": [
                    "Listo, Te recomiendo este vehículo."
                ],
                "context": [
                    ""
                ]
            },
            {
                "tag": "recomendacion",
                "patterns": [
                    "recomendación",
                    "recomiendes algo",
                    "necesito recomendación",
                    "que me recomiendas",
                    "necesito algunas especificaciones"
                ],
                "responses": [
                    "Buena elección. por favor siga estas instrucciones: \n Revisaremos las caracter\u00edstica una a una. Por ejemplo, a\u00f1o del auto: 2020 . Si necesitas ayuda con alg\u00fan concepto, escribe la palabra asistencia."
                ],
                "context": [
                    ""
                ]
            },
            {
                "tag": "anho_del_auto",
                "patterns": [
                    "año",
                    "año:",
                    "del año"
                ],
                "responses": [
                    "¿Con cuantos caballos de fuerza?"
                ],
                "context": [
                    ""
                ]
            },
            {
                "tag": "caballos_de_fuerza",
                "patterns": [
                    "120 caballos de fuerza",
                    "caballos de fuerza:",
                    "potencia de:"
                ],
                "responses": [
                    "¿Qué precio tiene en mente?"
                ],
                "context": [
                    ""
                ]
            },
            {
                "tag": "precio_esperado",
                "patterns": [
                    "12 000 dólares",
                    "precio: 30000",
                    "costo: 25000"
                ],
                "responses": [
                    "¿Cuál quiere que sea el rendimiento de combustible?"
                ],
                "context": [
                    ""
                ]
            },
            {
                "tag": "consumo_combustible",
                "patterns": [
                    "cosumo:",
                    "consumo",
                    "50 kilómetros por galón"
                ],
                "responses": [
                    "¿Cuál quiere que sea el tipo de combustible? \n Gasolina, Diesel o Eléctrico."
                ],
                "context": [
                    ""
                ]
            },
            {
                "tag": "tipo_de_combustible",
                "patterns": [
                    "combustible:",
                    "gasolina",
                    "diesel",
                    "eléctrico"
                ],
                "responses": [
                    "¿Cuántas plazas (asientos) aproximadamente necesita?"
                ],
                "context": [
                    ""
                ]
            },
            {
                "tag": "número_de_asientos",
                "patterns": [
                    "asientos:",
                    "plazas:",
                    "2 asientos"
                ],
                "responses": [
                    "¿Transmisión manual o automática?."
                ],
                "context": [
                    ""
                ]
            },
            {
                "tag": "tipo_de_transmisión",
                "patterns": [
                    "transmisión manual",
                    "transmisión automática",
                    "manual",
                    "automática",
                    "automatica"
                ],
                "responses": [
                    "Listo.\n Escribe 'recomendar ahora' para continuar."
                ],
                "context": [
                    ""
                ]
            },
            {
                "tag": "recomendar_ahora",
                "patterns": [
                    "recomendar ahora"
                ],
                "responses": [
                    "Creo que este auto te podría interesar"
                ],
                "context": [
                    ""
                ]
            },
            {
                "tag": "url",
                "patterns": [
                    "https://",
                    "http://"
                ],
                "responses": [
                    "Ok, Basado en esa imagen, ¿tal vez buscas algo como esto?"
                ],
                "context": [
                    ""
                ]
            },
            {
                "tag": "despedidas",
                "patterns": [
                    "chao",
                    "adios",
                    "hasta luego",
                    "nos vemos",
                    "bye",
                    "hasta pronto",
                    "hasta la proxima"
                ],
                "responses": [
                    "Hasta luego, tenga un buen dia"
                    "Hasta luego, un placer ayudarle"
                ],
                "context": [
                    ""
                ]
            },
            {
                "tag": "agradecimientos",
                "patterns": [
                    "gracias",
                    "muchas gracias",
                    "mil gracias",
                    "muy amable",
                    "se lo agradezco",
                    "fue de ayuda",
                    "gracias por la ayuda",
                    "muy agradecido",
                    "gracias por su tiempo",
                    "ty"
                ],
                "responses": [
                    "De nada",
                    "Feliz por ayudarlo",
                    "Gracias a usted",
                    "Estamos para servirle",
                    "Fue un placer"
                ],
                "context": [
                    ""
                ]
            },
            {
                "tag": "norespuesta",
                "patterns": [
                    ""
                ],
                "responses": [
                    "Podrías repetir de nuevo la información, por favor",
                    "Podrías reformular tu mensaje por favor",
                    "Disculpe, no he podido procesar su solicitud.\ Podría repetirla.",
                    "Disculpe, podría verificar que la información proporcionada esté bien escrita, por favor."
                ],
                "context": [
                    ""
                ]
            }
        ]
    }    
########################## MAIN ##################################

if __name__ = '__main__':
    start_intents()
