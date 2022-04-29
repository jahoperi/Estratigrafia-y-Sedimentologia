# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 14:27:33 2022

@author: jahop_fz60h0
"""

import streamlit as st
from streamlit_option_menu import option_menu
#from streamlit_lottie import st_lottie  # pip install streamlit-lottie
import streamlit.components.v1 as components
import requests  # pip install requests
import plotly.express as px

import pandas as pd
#import numpy as np

#import plotly.graph_objects as go 


from PIL import Image

image = Image.open('pemex.png')
st.image(image)


    
st.title("Estratigrafía y Sedimentología")
page_names = ['Aarón Antonio Nájera Aldape', 'Adriana Guadalupe Gómez Alejandro', 'Alan Leal Saucedo', 'Alejandra Cristina de la Rosa Illescas', 'Alejandra Eliane Valladares Hernández', 'Alejandro Ortega Nieto ', 'Ana Ferreira Silva', 'Ave Lucía Ochoa Bocanegra', 'Candelaria Hernández Mimiaga', 'Carlos Alberto Santiago Guillén', 'Carlos Arturo Rojas Reyna', 'Dalia Ivania Rivero Torres', 'Daniel González Rivera', 'David Octavio Loya Villanueva', 'Edgar Guadalupe Angulo Custodio', 'Edgar Jair Galicia González', 'Edson Giovanni Martínez Sánchez', 'Elisa Guadalupe Galvan Mares', 'Emmanuel Martínez González', 'Erick Neftali Tovar Candelaria', 'Fabiola María Hernández del Ángel', 'Fabiola Sarahi Lona Hernández', 'Gabriel Hernández Díaz', 'Gabriela Santos Martínez', 'Geovanni González Gallegos', 'Gustavo Silva Escamilla', 'Ivonne Edith Avila García', 'Jaime Enrique Pezzina Quintanilla', 'Javier Alejandro Castellanos Estevez', 'Javivi Rizo Ramírez', 'José Juan González López', 'Juan Alberto Treviño García', 'Juan Antonio Balleza Correa', 'Juan Carlos Olvera Saldaña', 'Juan José Ramos Villarreal', 'Juana Guadalupe Petrikowski Sandoval', 'Karina Remigio Morales', 'Kenia Esmeralda Díaz Hernández', 'Laura Patricia Bautista Garcilazo', 'Lucia Sánchez Ramírez', 'Lucy Salazar Castillo', 'Luis Alfonso Mares Martínez', 'Luis Daniel Sánchez Guzmán', 'Marcos Ramón Beltrán López', 'Maria del Sol Díaz Vera', 'María Jazmin González Romo', 'María Nohemí López Herrera', 'Maricruz Rocio Mendoza Hernández', 'Marlene Olivares Cruz', 'Nayeli Barrera Maceda', 'Olga Ithzel Hernández Sandoval', 'Orquidia Sarahi López Puente', 'Siboney Treviño Garcia', 'Victor Miguel Padilla Hernández', 'Vindia Itzel Herrera Garduza', 'Abraham Rodríguez Pérez', 'Carlos Alejandro Villalobos Dominguez', 'Carlos Erick García Flores', 'Ismael Romero Landaverde', 'José Alfredo Castillo Cabrera', 'José Alfredo Guerrero Mar', 'José Manuel López Infante', 'Juan Domingo Ruiz Nápoles', 'Juan Manuel Zamora Rangel', 'Leonardo Jiménez Velázquez', 'Leonora Patricia Bautista Garcilazo', 'María Manuela Méndez Díaz', 'María Yadira González Romo', 'Miguel Angel Ubilla Escamilla', 'Sixto Alberto Pérez González', 'Vanessa del Carmen Farias Couoh', 'Unión de los gráficos']

page = st.radio('Navegación', page_names, index = 0)
#st.write("**La variable 'page' returns:**", page)

data = pd.read_csv("NDR.csv")
data = data.set_index('PROFESIONISTAS')

#col1, col2, col3 = st.columns(3)

col1, col2 = st.columns([100, 100])

col1.subheader("DATOS")
col1.write(data)


#1 vertical menu

#selected = option_menu(
#    menu_title = "Geología Estructural", #required
#    options = ["Ariel Ramírez Díaz", "Arnulfo Zarate Santiago", "Daniel Gómez Ochoa", "Gustavo Gutiérrez Rodríguez", "Jesica Aguirre Olguin", "Jesús Alejandro García Cantú", "José Luis Landa Mondragon", "María Elena Arenas Martínez", "Marybeth Garrido Hernández", "Mónica Rodríguez Otero", "Nestor Daniel Ortíz Najera", "Oscar Emmanuel Guadalupe Vences Estudillo", "Raúl Arturo Palacios Zamora", "Rosalía Molina Mandujano", "Uriel Román Manjarrez Juárez", "Uzziel Saldaña Hernández", "Verónica Iveth Ramírez Soria", "Yessica Guerrero Amador"], #required
#    #icons = ["house", "envelope", "envelope",  "envelope",  "envelope",  "envelope",  "envelope",  "envelope",  "envelope",  "envelope",  "envelope",  "envelope", "envelope", "envelope", "envelope", "envelope", "envelope", "envelope", "envelope",], #optional
#    #icons = ["house"],
#    menu_icon = "cast", #optional
#    default_index = 0, #optional
    
#    ) 
 

################################################################################################################################################################  
#1                 
if page == 'Aarón Antonio Nájera Aldape':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,2,2,1,2,2,3,2,2,2,1,1,2,2,1,2,1,1])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Aarón Antonio Nájera Aldape', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")
   
#2
if page == 'Adriana Guadalupe Gómez Alejandro':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,2,2,1,2,2,2,2,2,2,1,2,1,1,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Adriana Guadalupe Gómez Alejandro', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   

#3
if page == 'Alan Leal Saucedo':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,1,1,2,1,2,2,2,1,2,1,1,1,1,1,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Alan Leal Saucedo', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#4
if page == 'Alejandra Cristina de la Rosa Illescas':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,2,3,1,3,1,3,2,3,1,2,3,1,1,1,1,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Alejandra Cristina de la Rosa Illescas', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#5
if page == 'Alejandra Eliane Valladares Hernández':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,3,2,2,3,3,3,3,2,2,1,2,1,3,3,3,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Alejandra Eliane Valladares Hernández', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#6
if page == 'Alejandro Ortega Nieto ':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,2,2,2,2,2,2,3,2,2,2,2,1,1,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Alejandro Ortega Nieto', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#7
if page == 'Ana Ferreira Silva':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,1,2,1,2,2,2,1,2,1,1,1,1,1,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Ana Ferreira Silva', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#8
if page == 'Ave Lucía Ochoa Bocanegra':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,1,1,1,1,1,1,2,2,1,2,1,1,1,1,1,1,2,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Ave Lucía Ochoa Bocanegra', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#9
if page == 'Candelaria Hernández Mimiaga':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,2,2,2,1,3,2,1,1,2,2,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Candelaria Hernández Mimiaga', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#10
if page == 'Carlos Alberto Santiago Guillén':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,3,2,3,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Carlos Alberto Santiago Guillén', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
############### 10 ############################################################################################################################################

#11
if page == 'Carlos Arturo Rojas Reyna':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,2,2,2,2,1,2,1,1,1,2,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Carlos Arturo Rojas Reyna', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

#12
if page == 'Dalia Ivania Rivero Torres':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,2,3,3,3,2,3,2,3,2,2,3,1,1,2,1,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Dalia Ivania Rivero Torres', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

#13
if page == 'Daniel González Rivera':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,3,3,3,3,2,2,2,2,1,2,1,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Daniel González Rivera', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

#14
if page == 'David Octavio Loya Villanueva':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,1,2,2,2,3,2,2,1,2,2,1,2,1,1,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='David Octavio Loya Villanueva', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

#15
if page == 'Edgar Guadalupe Angulo Custodio':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,1,2,2,2,2,3,2,3,1,1,2,1,2,1,2,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Edgar Guadalupe Angulo Custodio', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

#16
if page == 'Edgar Jair Galicia González':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,2,3,3,2,3,4,3,2,3,2,2,2,2,3,2,2,2,5])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Edgar Jair Galicia González', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

#17
if page == 'Edson Giovanni Martínez Sánchez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,2,2,2,2,1,2,2,1,2,2,2,1])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Edson Giovanni Martínez Sánchez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

#18
if page == 'Elisa Guadalupe Galvan Mares':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,2,2,1,2,2,2,1,2,1,1,1,1,1,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Elisa Guadalupe Galvan Mares', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

#19
if page == 'Emmanuel Martínez González':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,2,2,2,2,3,3,2,3,2,2,1,1,2,2,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Emmanuel Martínez González', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

#20
if page == 'Erick Neftali Tovar Candelaria':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,3,3,2,3,3,3,2,2,2,2,2,2,2,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Erick Neftali Tovar Candelaria', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 

############   20  ############################################################################################################################################

#21
if page == 'Fabiola María Hernández del Ángel':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,2,2,3,3,3,3,2,2,2,1,2,1,1,1,1,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Fabiola María Hernández del Ángel', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("") 
   
#22
if page == 'Fabiola Sarahi Lona Hernández':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,1,3,3,2,3,3,3,2,2,2,2,3,2,1,1,1,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Fabiola Sarahi Lona Hernández', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#23
if page == 'Gabriel Hernández Díaz':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,3,3,2,2,2,2,1,1,2,1,2,1,1,1,1,1,1])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Gabriel Hernández Díaz', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#24
if page == 'Gabriela Santos Martínez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,3,3,3,3,3,3,3,2,3,2,1,2,1,1,1,2,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Gabriela Santos Martínez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#25
if page == 'Geovanni González Gallegos':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,2,1,2,2,1,2,2,2,1,2,2,1,1,1,3,1,2,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Geovanni González Gallegos', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#26
if page == 'Gustavo Silva Escamilla':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,1,3,3,2,3,2,2,2,1,1,1,2,2,2,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Gustavo Silva Escamilla', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#27
if page == 'Ivonne Edith Avila García':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,3,2,2,3,3,3,3,3,1,3,2,3,3,2,1,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Ivonne Edith Avila García', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#28
if page == 'Jaime Enrique Pezzina Quintanilla':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,3,2,2,2,1,1,1,1,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Jaime Enrique Pezzina Quintanilla', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#29
if page == 'Javier Alejandro Castellanos Estevez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,3,3,3,3,3,3,2,3,3,3,2,2,3,3,3,2,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Javier Alejandro Castellanos Estevez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#30
if page == 'Javivi Rizo Ramírez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,2,1,1,2,2,2,1,2,2,1,2,1,1,1,1,1,1])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Javivi Rizo Ramírez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#########  30   ###############################################################################################################################################   
   
#31
if page == 'José Juan González López':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,2,2,1,3,2,3,2,3,2,1,1,1,1,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='José Juan González López', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#32
if page == 'Juan Alberto Treviño García':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Juan Alberto Treviño García', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#33
if page == 'Juan Antonio Balleza Correa':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,2,3,3,2,3,3,3,3,3,2,2,2,2,2,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Juan Antonio Balleza Correa', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#34
if page == 'Juan Carlos Olvera Saldaña':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,3,2,2,2,1,1,1,1,2,1,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Juan Carlos Olvera Saldaña', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#35
if page == 'Juan José Ramos Villarreal':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,3,3,3,3,3,3,2,2,2,1,3,1,1,1,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Juan José Ramos Villarreal', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#36
if page == 'Juana Guadalupe Petrikowski Sandoval':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,3,4,2,3,3,3,2,3,2,3,3,2,2,2,2,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Juana Guadalupe Petrikowski Sandoval', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#37
if page == 'Karina Remigio Morales':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,3,3,3,2,3,3,3,2,2,2,1,2,2,2,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Karina Remigio Morales', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#38
if page == 'Kenia Esmeralda Díaz Hernández':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,1,3,1,3,2,2,2,2,1,2,3,2,1,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Kenia Esmeralda Díaz Hernández', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#39
if page == 'Laura Patricia Bautista Garcilazo':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,3,3,2,2,2,3,1,1,2,2,2,1,1,2,1,3,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Laura Patricia Bautista Garcilazo', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#40
if page == 'Lucia Sánchez Ramírez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,3,2,2,2,2,3,2,2,2,1,2,2,2,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Lucia Sánchez Ramírez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
##########  40   ############################################################################################################################################   
   
#41
if page == 'Lucy Salazar Castillo':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Lucy Salazar Castillo', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#42
if page == 'Luis Alfonso Mares Martínez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,1,1,1,1,1,2,2,1,1,2,2,1,1,1,1,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Luis Alfonso Mares Martínez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#43
if page == 'Luis Daniel Sánchez Guzmán':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,3,3,3,3,2,3,1,2,2,2,2,2,2,2,2,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Luis Daniel Sánchez Guzmán', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#44
if page == 'Marcos Ramón Beltrán López':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,1,2,2,2,2,1,2,2,2,1,1,1,1,1,1])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Marcos Ramón Beltrán López', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#45
if page == 'Maria del Sol Díaz Vera':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,3,2,2,2,2,2,2,2,2,1,1,1,1,1,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Maria del Sol Díaz Vera', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#46
if page == 'María Jazmin González Romo':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,3,2,2,2,3,2,1,3,1,2,2,1,1,1,1,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='María Jazmin González Romo', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#47
if page == 'María Nohemí López Herrera':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,3,3,3,2,3,2,2,2,2,2,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='María Nohemí López Herrera', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#48
if page == 'Maricruz Rocio Mendoza Hernández':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,3,3,2,3,2,3,2,3,2,2,2,2,1,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Maricruz Rocio Mendoza Hernández', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#49
if page == 'Marlene Olivares Cruz':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,3,2,2,2,2,2,1,1,1,1,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Marlene Olivares Cruz', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
#50
if page == 'Nayeli Barrera Maceda':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,2,1,2,2,1,3,2,3,1,2,1,1,2,1,1,1,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Nayeli Barrera Maceda', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")   
   
########  50   ###############################################################################################################################################   
   
#51
if page == 'Olga Ithzel Hernández Sandoval':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,1,2,2,2,1,3,2,2,2,3,2,1,1,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Olga Ithzel Hernández Sandoval', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#52
if page == 'Orquidia Sarahi López Puente':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,1,1,2,2,1,2,1,2,1,2,1,1,2,1,1,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Orquidia Sarahi López Puente', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#53
if page == 'Siboney Treviño Garcia':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,2,3,3,1,3,1,3,2,3,2,2,2,1,1,2,2,3,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Siboney Treviño Garcia', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#54
if page == 'Victor Miguel Padilla Hernández':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,2,2,1,2,1,2,1,1,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Victor Miguel Padilla Hernández', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#55
if page == 'Vindia Itzel Herrera Garduza':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,3,3,1,2,2,2,1,1,1,2,1,1,1,1,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Vindia Itzel Herrera Garduza', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#56
if page == 'Abraham Rodríguez Pérez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,2,2,2,2,2,2,3,2,2,2,1,1,2,2,2,2,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Abraham Rodríguez Pérez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#57
if page == 'Carlos Alejandro Villalobos Dominguez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,1,2,2,1,1,2,2,2,2,1,1,1,1,2,1,2,1,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Carlos Alejandro Villalobos Dominguez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#58
if page == 'Carlos Erick García Flores':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,3,2,2,2,2,2,1,1,1,2,2,3,2,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Carlos Erick García Flores', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#59
if page == 'Ismael Romero Landaverde':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,2,2,2,3,2,2,1,2,1,1,1,2,1,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Ismael Romero Landaverde', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#60
if page == 'José Alfredo Castillo Cabrera':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,1,2,1,2,1,1,1,1,1,2,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='José Alfredo Castillo Cabrera', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")     
   
#####  60  #####################################################################################################################################################   
   
#61
if page == 'José Alfredo Guerrero Mar':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,2,2,1,2,2,1,2,2,1,1,1,1,3,2,3,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='José Alfredo Guerrero Mar', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#62
if page == 'José Manuel López Infante':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,3,2,1,2,1,1,1,1,2,2,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='José Manuel López Infante', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    

#63
if page == 'Juan Domingo Ruiz Nápoles':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Juan Domingo Ruiz Nápoles', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#64
if page == 'Juan Manuel Zamora Rangel':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,2,2,2,2,2,3,2,2,2,2,1,1,1,1,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Juan Manuel Zamora Rangel', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#65
if page == 'Leonardo Jiménez Velázquez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,1,2,2,2,2,2,2,1,1,2,2,2,2,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Leonardo Jiménez Velázquez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#66
if page == 'Leonora Patricia Bautista Garcilazo':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,2,2,2,2,2,2,2,2,2,2,1,2,1,1,2,2,2,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Leonora Patricia Bautista Garcilazo', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
   
#67
if page == 'María Manuela Méndez Díaz':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,1,2,2,1,2,2,1,1,1,2,3,2,3,1,1])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='María Manuela Méndez Díaz', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
#68
if page == 'María Yadira González Romo':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,2,3,2,1,2,3,2,2,3,2,1,2,1,1,2,2,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='María Yadira González Romo', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
   
#69
if page == 'Miguel Angel Ubilla Escamilla':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,1,1,1,1,2,1,1,2,1,1,1,1,3,2,3,1,1])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Miguel Angel Ubilla Escamilla', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")    
   
   
#70
if page == 'Sixto Alberto Pérez González':
    #st.title(f"Has seleccionado {selected}")
    fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
    fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Sixto Alberto Pérez González', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
    fig.update_yaxes(range = [0,5])
    st.plotly_chart(fig)
    #fig.show()
else:   
    st.subheader("")
    st.write("")   
   
#71
if page == 'Vanessa del Carmen Farias Couoh':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,1,2,2,2,2,2,2,2,2,1,1,1,1,2,2,1,1])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Vanessa del Carmen Farias Couoh', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()Vanessa del Carmen Farias Couoh
else:   
   st.subheader("")
   st.write("")    
   
#############   71   ###################################################################################################################################   
   
   
   
###############################################################################################################################################################
    
if page == 'Unión de los gráficos':
     fig = px.line(x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,2,2,1,2,2,3,2,2,2,1,1,2,2,1,2,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias',  autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#1
     fig.add_scatter(name = 'Aarón Antonio Nájera Aldape',x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,2,2,1,2,2,3,2,2,2,1,1,2,2,1,2,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#2
     fig.add_scatter(name = 'Adriana Guadalupe Gómez Alejandro', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,2,2,1,2,2,2,2,2,2,1,2,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#3
     fig.add_scatter(name = 'Alan Leal Saucedo', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,1,1,2,1,2,2,2,1,2,1,1,1,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#4
     fig.add_scatter(name = 'Alejandra Cristina de la Rosa Illescas', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,2,3,1,3,1,3,2,3,1,2,3,1,1,1,1,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#5
     fig.add_scatter(name = 'Alejandra Eliane Valladares Hernández', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,3,2,2,3,3,3,3,2,2,1,2,1,3,3,3,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#6
     fig.add_scatter(name = 'Alejandro Ortega Nieto ', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,2,2,2,2,2,2,3,2,2,2,2,1,1,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#7
     fig.add_scatter(name = 'Ana Ferreira Silva', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,1,2,1,2,2,2,1,2,1,1,1,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#8
     fig.add_scatter(name = 'Ave Lucía Ochoa Bocanegra', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,1,1,1,1,1,1,2,2,1,2,1,1,1,1,1,1,2,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#9
     fig.add_scatter(name = 'Candelaria Hernández Mimiaga', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,2,2,2,1,3,2,1,1,2,2,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#10
     fig.add_scatter(name = 'Carlos Alberto Santiago Guillén', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,3,2,3,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#11
     fig.add_scatter(name = 'Carlos Arturo Rojas Reyna', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,2,2,2,2,1,2,1,1,1,2,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#12
     fig.add_scatter(name = 'Dalia Ivania Rivero Torres', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,3,2,3,3,3,2,3,2,3,2,2,3,1,1,2,1,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#13
     fig.add_scatter(name = 'Daniel González Rivera', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,3,3,3,3,2,2,2,2,1,2,1,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#14
     fig.add_scatter(name = 'David Octavio Loya Villanueva', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,1,2,2,2,3,2,2,1,2,2,1,2,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#15
     fig.add_scatter(name = 'Edgar Guadalupe Angulo Custodio', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,1,2,2,2,2,3,2,3,1,1,2,1,2,1,2,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#16
     fig.add_scatter(name = 'Edgar Jair Galicia González', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,2,3,3,2,3,4,3,2,3,2,2,2,2,3,2,2,2,5])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#17
     fig.add_scatter(name = 'Edson Giovanni Martínez Sánchez', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,2,2,2,2,1,2,2,1,2,2,2,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#18
     fig.add_scatter(name = 'Elisa Guadalupe Galvan Mares', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,2,2,1,2,2,2,1,2,1,1,1,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#19
     fig.add_scatter(name = 'Emmanuel Martínez González', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,2,2,2,2,3,3,2,3,2,2,1,1,2,2,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#20
     fig.add_scatter(name = 'Erick Neftali Tovar Candelaria', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,3,3,2,3,3,3,2,2,2,2,2,2,2,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#21
     fig.add_scatter(name = 'Fabiola María Hernández del Ángel', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,2,2,3,3,3,3,2,2,2,1,2,1,1,1,1,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#22
     fig.add_scatter(name = 'Fabiola Sarahi Lona Hernández', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,1,3,3,2,3,3,3,2,2,2,2,3,2,1,1,1,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#23
     fig.add_scatter(name = 'Gabriel Hernández Díaz', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,3,3,2,2,2,2,1,1,2,1,2,1,1,1,1,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#24
     fig.add_scatter(name = 'Gabriela Santos Martínez', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,3,3,3,3,3,3,3,2,3,2,1,2,1,1,1,2,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#25
     fig.add_scatter(name = 'Geovanni González Gallegos', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,2,1,2,2,1,2,2,2,1,2,2,1,1,1,3,1,2,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#26
     fig.add_scatter(name = 'Gustavo Silva Escamilla', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,1,3,3,2,3,2,2,2,1,1,1,2,2,2,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#27
     fig.add_scatter(name = 'Ivonne Edith Avila García', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,3,2,2,3,3,3,3,3,1,3,2,3,3,2,1,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#28
     fig.add_scatter(name = 'Jaime Enrique Pezzina Quintanilla', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,3,2,2,2,1,1,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])   

#29
     fig.add_scatter(name = 'Javier Alejandro Castellanos Estevez', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,3,3,3,3,3,3,2,3,3,3,2,2,3,3,3,2,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#30
     fig.add_scatter(name = 'Javivi Rizo Ramírez', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,2,1,1,2,2,2,1,2,2,1,2,1,1,1,1,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#31
     fig.add_scatter(name = 'José Juan González López', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,2,2,1,3,2,3,2,3,2,1,1,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])   

#32
     fig.add_scatter(name = 'Juan Alberto Treviño García', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])   

#33
     fig.add_scatter(name = 'Juan Antonio Balleza Correa', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,2,3,3,2,3,3,3,3,3,2,2,2,2,2,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#34
     fig.add_scatter(name = 'Juan Carlos Olvera Saldaña', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,3,2,2,2,1,1,1,1,2,1,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#35
     fig.add_scatter(name = 'Juan José Ramos Villarreal', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,3,3,3,3,3,3,2,2,2,1,3,1,1,1,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#36
     fig.add_scatter(name = 'Juana Guadalupe Petrikowski Sandoval', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,3,4,2,3,3,3,2,3,2,3,3,2,2,2,2,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#37
     fig.add_scatter(name = 'Karina Remigio Morales', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,3,3,3,2,3,3,3,2,2,2,1,2,2,2,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#38
     fig.add_scatter(name = 'Kenia Esmeralda Díaz Hernández', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,1,3,1,3,2,2,2,2,1,2,3,2,1,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#39 
     fig.add_scatter(name = 'Laura Patricia Bautista Garcilazo', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,3,3,2,2,2,3,1,1,2,2,2,1,1,2,1,3,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#40
     fig.add_scatter(name = 'Lucia Sánchez Ramírez', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,3,2,2,2,2,3,2,2,2,1,2,2,2,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#41
     fig.add_scatter(name = 'Lucy Salazar Castillo', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#42
     fig.add_scatter(name = 'Luis Alfonso Mares Martínez', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,1,1,1,1,1,2,2,1,1,2,2,1,1,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#43
     fig.add_scatter(name = 'Luis Daniel Sánchez Guzmán', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,3,3,3,3,2,3,1,2,2,2,2,2,2,2,2,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#44
     fig.add_scatter(name = 'Marcos Ramón Beltrán López', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,1,2,2,2,2,1,2,2,2,1,1,1,1,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#45
     fig.add_scatter(name = 'Maria del Sol Díaz Vera', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,3,2,2,2,2,2,2,2,2,1,1,1,1,1,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#46
     fig.add_scatter(name = 'María Jazmin González Romo', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,3,2,2,2,3,2,1,3,1,2,2,1,1,1,1,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#47
     fig.add_scatter(name = 'María Nohemí López Herrera', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,3,3,3,2,3,2,2,2,2,2,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#48
     fig.add_scatter(name = 'Maricruz Rocio Mendoza Hernández', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,3,3,2,3,2,3,2,3,2,2,2,2,1,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#49
     fig.add_scatter(name = 'Marlene Olivares Cruz', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,3,2,2,2,2,2,1,1,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#50
     fig.add_scatter(name = 'Nayeli Barrera Maceda', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,2,1,2,2,1,3,2,3,1,2,1,1,2,1,1,1,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#51
     fig.add_scatter(name = 'Olga Ithzel Hernández Sandoval', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,1,2,2,2,1,3,2,2,2,3,2,1,1,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#52
     fig.add_scatter(name = 'Orquidia Sarahi López Puente', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,1,1,2,2,1,2,1,2,1,2,1,1,2,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#53
     fig.add_scatter(name = 'Siboney Treviño Garcia', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,2,3,3,1,3,1,3,2,3,2,2,2,1,1,2,2,3,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#54
     fig.add_scatter(name = 'Victor Miguel Padilla Hernández', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,2,2,1,2,1,2,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#55
     fig.add_scatter(name = 'Vindia Itzel Herrera Garduza', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,1,3,3,1,2,2,2,1,1,1,2,1,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#56
     fig.add_scatter(name = 'Abraham Rodríguez Pérez', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,2,2,2,2,2,2,3,2,2,2,1,1,2,2,2,2,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])


#57
     fig.add_scatter(name = 'Carlos Alejandro Villalobos Dominguez', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,1,2,2,1,1,2,2,2,2,1,1,1,1,2,1,2,1,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#58
     fig.add_scatter(name = 'Carlos Erick García Flores', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,3,2,2,2,2,2,1,1,1,2,2,3,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#59
     fig.add_scatter(name = 'Ismael Romero Landaverde', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,2,2,2,3,2,2,1,2,1,1,1,2,1,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#60
     fig.add_scatter(name = 'José Alfredo Castillo Cabrera', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,1,2,1,2,1,1,1,1,1,2,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#61
     fig.add_scatter(name = 'José Alfredo Guerrero Mar', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,2,2,2,2,1,2,2,1,2,2,1,1,1,1,3,2,3,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#62
     fig.add_scatter(name = 'José Manuel López Infante', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,3,2,1,2,1,1,1,1,2,2,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#63
     fig.add_scatter(name = 'Juan Domingo Ruiz Nápoles', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#64
     fig.add_scatter(name = 'Juan Manuel Zamora Rangel', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,3,2,2,2,2,2,3,2,2,2,2,1,1,1,1,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#65
     fig.add_scatter(name = 'Leonardo Jiménez Velázquez', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,1,2,2,2,2,2,2,1,1,2,2,2,2,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#66
     fig.add_scatter(name = 'Leonora Patricia Bautista Garcilazo', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,2,2,2,2,2,2,2,2,2,2,1,2,1,1,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#67
     fig.add_scatter(name = 'María Manuela Méndez Díaz', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,2,2,1,2,2,1,2,2,1,1,1,2,3,2,3,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#68
     fig.add_scatter(name = 'María Yadira González Romo', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[3,3,2,3,2,1,2,3,2,2,3,2,1,2,1,1,2,2,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#69
     fig.add_scatter(name = 'Miguel Angel Ubilla Escamilla', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,1,1,1,1,2,1,1,2,1,1,1,1,3,2,3,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#70
     fig.add_scatter(name = 'Sixto Alberto Pérez González', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])

#71
     fig.add_scatter(name = 'Vanessa del Carmen Farias Couoh', x=["Calidad de roca almacén",	"Bioestratigrafía", "Diagénesis", "Estratigrafía de Secuencias de sistemas carbonatados", "Estratigrafía de Secuencias de sistemas clásticos", "Sedimentología, diagénesis y distribución de facies en lutitas orgánicas", "Sedimentología y análisis de facies de clásticos", "Sedimentología y análisis de facies de rocas carbonatadas", "Mapeo, correlaciones estratigráficas y estructurales", "Petrografía y descripción de núcleos", "Exploración y análisis de plays", "Reconstrucción estructural, paleogeografía y tectónica", "Análisis de atributos", "Estratigrafía sísmica", "Análisis de petrofísica de clásticos y de baja resistividad", "Análisis petrofísico de carbonatos", "Análisis especial y rutinario de núcleos", "Principios de petrofísica y evaluación de formaciones", "Análisis de riesgo geológico", "Integración de geociencias"], y=[2,2,2,1,2,2,2,2,2,2,2,2,1,1,1,1,2,2,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     st.plotly_chart(fig)
     
else:
    st.subheader("")
    
    
