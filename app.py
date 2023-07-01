#

#Funcion para instalar una libreria
def instalar_libreria(nombre_libreria):
  import pip
  pip.main(['install', nombre_libreria])

#Funcion para escribir un archivo 
def escribir_archivo(file_path,text):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

#Funcion para leer un archivo
def leer_archivo(file_path):
  with open(file_path, 'r',encoding='utf-8') as file:
        return file.read()
  
#Funcion para obtener el texto de un articulo de wikipedia
def obtener_articulo_wikipedia_es( subject):
  import requests
  from bs4 import BeautifulSoup
  url = 'https://es.wikipedia.org/w/api.php'
  params = {
              'action': 'parse',
              'page': subject,
              'format': 'json',
              'prop':'text',
              'redirects':''
          }
  response = requests.get(url, params=params)
  data = response.json()
  raw_html = data['parse']['text']['*']
  soup = BeautifulSoup(raw_html,'html.parser')
  soup.find_all('p')
  text = ''
  for p in soup.find_all('p'):
      text += p.text
  return text

def guardar_articulo_wikipedia(file_path,articulo):
   text=obtener_articulo_wikipedia_es(articulo)
   escribir_archivo(file_path,text)


'''
                                                      Instalación de las Librerias necesarias
instalar_libreria('tensorflow')
instalar_libreria('transformers')
instalar_libreria('torch')
instalar_libreria('bs4')
'''
                                                      #Importamos las librerias obligariamente necesarias
import time
inicio_importacion=time.time()
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
from textwrap import wrap
fin_importacion=time.time()
duracion_impotacion=fin_importacion-inicio_importacion  
print('Tiempo de Importacion de Librerias:',duracion_impotacion)

                                                      #Cargamos el modelo
inicio_creacion_modelo=time.time()
the_model = 'mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es'
tokenizer = AutoTokenizer.from_pretrained(the_model, do_lower_case=True)
model = AutoModelForQuestionAnswering.from_pretrained(the_model)
nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
fin_creacion_modelo=time.time()
duracion_creacion_modelo=fin_creacion_modelo-inicio_creacion_modelo
print('Tiempo de Creación del modelo:',duracion_creacion_modelo)

def preguntas_y_respuestas(model, contexto, nlp):
  '''
  Pone a prueba el modelo de pregunta-respuesta haciendo una serie de preguntas
  al modelo y mostrando las respuestas proporcionadas, así como la posición en
  el texto donde empieza y termina la respuesta. El bucle de preguntas se detiene
  cuando se presiona Enter sin escribir una pregunta."""
  '''
                                                      #Imprime el contexto
  print('Contexto:')
  print('-----------------')
  print('\n'.join(wrap(contexto)))

                                                      #Bucle preguntas-respuestas:
  continuar = True
  while continuar:
    print('\nPregunta:')
    print('-----------------')
    pregunta = str(input())
    inicio_respuesta=time.time()
    continuar = pregunta!=''
    if continuar:
      salida = nlp({'question':pregunta, 'context':contexto})
      print('\nRespuesta:')
      print('-----------------')
      fin_respuesta=time.time()
      duracion_respuesta=fin_respuesta-inicio_respuesta
      print(salida['answer'])
      print(salida)
      print('Tiempo de Respuesta:',duracion_respuesta)

#                                                     Carga del contexto
#Ruta del archivo de texto con el contexto
inicio_carga_contexto=time.time()
file_path = "context.txt"
'''                                                   Obtención de datos desde Wikipedia
Obtenemos un articulo de la wikipedia en español y lo guardamos en un archivo de texto
En el caso de no contar con el contexto cargado en el archivo correspondiente descomentar la siguiente sentencia
tema='Universidad Tecnologica Nacional'
guardar_articulo_wikipedia(file_path,tema)'''
#cargamos el contexto desde el archivo de texto
contexto=leer_archivo(file_path)
fin_carga_contexto=time.time()
duracion_carga_contexto=fin_carga_contexto-inicio_carga_contexto
print('Tiempo de Carga del contexto:',duracion_carga_contexto)
#                                                   Inicio del bucle de preguntas y respuestas
preguntas_y_respuestas(model, contexto, nlp)
