'''19_ Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de es-
treno, desarrollar las funciones necesarias para resolver las siguientes actividades:

a. mostrar los nombre películas estrenadas en el año 2014;

b. indicar cuántas películas se estrenaron en el año 2018;

c. mostrar las películas de Marvel Studios estrenadas en el año 2016.
'''
from Operaciones_Pilas import Pila

pila=Pila()
Peliculas=[
{'Titulo':'Toy Stoy 3', 'Año':2010,'Estudio':'Pixar Animation Studios'},
{'Titulo':'Los Vengadores','Año':2012,'Estudio':'Marvel Studios'},
{'Titulo':'El sorprendente Hombre Araña','Año':2012,'Estudio':'Columbia Pictures'},
{'Titulo':'El hombre de acero','Año':2013,'Estudio':'DC Studios'},
{'Titulo':'Tortugas Ninja','Año':2014,'Estudio':'Nickelodeon Movies'},
{'Titulo':'El Hobbit: La batalla de los cinco ejércitos ','Año':2014,'Estudio':'New Line Cinema'},
{'Titulo':'Los juegos del hambre: Sinsajo - Parte 2','Año':2015,'Estudio':'Color Force'},
{'Titulo':'Deadpool','Año':2016,'Estudio':'Marvel Studios'},
{'Titulo':'Doctor Strange','Año':2016,'Estudio':'Marvel Studios'},
{'Titulo':'Escuadrón Suicida','Año':2016,'Estudio':'DC Studios'},
{'Titulo':'Avengers: Infinity War','Año':2018,'Estudio':'Marvel Studios'},
{'Titulo':'Venom','Año':2018,'Estudio':'Marvel Studios'},
{'Titulo':'El robo perfecto','Año':2018,'Estudio':'Diamond Film Productions'},
{'Titulo':'Guasón','Año':2019,'Estudio':'DC Studios'},
]

for film in Peliculas:
    pila.push(film)

contador=0
while (pila.size()>0):
    elemento=pila.pop()
    if (elemento["Año"]==2014):
        print('Pelicula estrenada en el 2014: ',elemento["Titulo"])
    elif (elemento["Año"]==2018):
        contador += 1
    elif (elemento["Año"]==2016 and elemento['Estudio']=='Marvel Studios'):
        print('Pelicula marvel del 2016: ',elemento["Titulo"])

print(f'En el 2018 se estrenaron {contador} peliculas')