
#24_ Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de 
#su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
#necesarias para resolver las siguientes actividades:

#a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
#b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
#c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

from Operaciones_Pilas import Pila

pila=Pila()

personaje=[{'nombre':'Capitan America','peliculas':11},
            {'nombre':'Iron Man','peliculas':9},
            {'nombre':'Thor','peliculas':9},
            {'nombre':'Black Widow','peliculas':9},
            {'nombre':'Drax','peliculas':4},
            {'nombre':'Rocket Raccoon','peliculas':4},
            {'nombre':'Groot','peliculas':4},
            {'nombre':'Nebula','peliculas':4},
            {'nombre':'Gamora','peliculas':4},
            {'nombre':'Star-Lord','peliculas':4},]

for persona in personaje:
    pila.push(persona)

tamanio=pila.size()
while pila.size()>0:
    elemento=pila.pop()
    if (elemento['nombre']=='Rocket Raccoon') or (elemento['nombre']=='Groot'):
        print(elemento['nombre'],' esta en la posicion: ',pila.size()+1)   
    if (elemento['peliculas']>5):
        print(elemento['nombre'],' aparece en mas de 5 peliculas, con un total de',elemento['peliculas'])
    if (elemento['nombre']=='Black Widow'):
        print('Black Widow participo en un total de', elemento['peliculas'],' peliculas')
    if (elemento['nombre'][0] in ['C','D','G']):
        print(elemento['nombre'], 'Empieza por ',elemento['nombre'][0] )

