# -*- coding: utf-8 -*-
"""Chatbot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e_TkFeZDzFgeTdg46U0tNmn4A5d__JAl
"""

pip install nltk

import nltk
from nltk.chat.util import Chat, reflections

reflections={ 
   
}

pairs =[
[ 'hola', 
 ['Ingresa la palabra servicios para el menú de opciones']],

 
['(.*)numero|telefono|linea de atencion|whatsapp(.*)', 
 ['Linea de atención al usuario: 01800853245 \nLinea de whatsapp: 3004752698\n']],

['(.*)direccion|ubicacion(.*)', 
 ['Cl. 67 ##53-108, Medellín, Antioquia\n']],

['(.*)servicios(.*)', 
 ['Por el momento solo prestamos servicios de: \n1.Hospitaliación\n2.Consulta externa\n3.Farmacia\n4.Sedes\n5.Incapacidades\n']],

['4', 
 ['Actualmente la EPS Vida Alegre solo cuanta con una sede, la cual esta ubicada en Cl. 67 ##53-108, Medellín, Antioquia \n']],

['3', 
 ['Para el servicio de farmacia, debes trasladarte a nuestra sede principal, en el horaria de 8am a 12pm\n']],

['5', 
 ['Para el servicio de incapacidades le pedimos trasladarse a nuestra sede principal\n']],

['1', 
 ['Para el servicio de hospitalización le pedimos trasladarse a nuestra sede principal\n']],

['2', 
 ['Para el servicio de consulta externa no tenemos agneda disponible en el momento\n']]

]

def chatty():
  print("hola, soy Chatty y estoy para ayudarte :) \nPor favor, escribe hola para iniciar una conversación y recuerda que es en español y en minúsculas.\n Escribe salir para terminar\n")
  chat = Chat(pairs, reflections)
  chat.converse()

if __name__=="__main__":
  chatty()

chatty()