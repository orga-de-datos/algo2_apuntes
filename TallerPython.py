# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.5.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Python

# + [markdown] slideshow={"slide_type": "slide"}
# ## Un poco de Historia

# + [markdown] slideshow={"slide_type": "subslide"}
# Python fue creado a finales de los años 80 por un programador holandés llamado **Guido van Rossum**,
# quien sigue siendo aún hoy el líder del desarrollo del lenguaje. (Edit julio 2018: [ya no más](https://www.mail-archive.com/python-committers@python.org/msg05628.html))

# + [markdown] slideshow={"slide_type": "subslide"}
# El nombre del lenguaje proviene de los humoristas británicos Monty Python.
#
# >*"I chose Python as a working title for the project, being in a slightly irreverent mood (and a big fan of Monty Python's Flying Circus)."*

# + [markdown] slideshow={"slide_type": "slide"}
# ## Diferencias entre C y Python
#
# **Lenguaje de programación C:**
# - Compilado
# - Tipado estático
# - Procedural
# - Bajo nivel
# - Permite acceso a memoria de bajo nivel mediante punteros
#
# **Python:**
# - Interpretado
# - Tipado dinamico
# - Multiparadigma
# - Alto nivel
# - Tiene un recolector de basura (no hay malloc, free, realloc, etc)
# -

# ## ¿Cómo empezar?
#
# * Al ser un lenguaje *interpretado*, se puede ir escribiendo a medida que se ejecuta, sin necesidad de compilar de antemano! Solamente hace falta escribir `python` o `python3` en una terminal para empezar
#   
# * También, permite escribir archivos y correrlos. Crear un archivo con extensión `.py` y luego correr `python miarchivo.py` en laterminal

# + [markdown] slideshow={"slide_type": "slide"}
# ## La filosofía de Python

# + slideshow={"slide_type": "slide"}
import this

# + [markdown] slideshow={"slide_type": "slide"}
# ## Conocimientos Básicos de Python: Variables y Tipos

# + slideshow={"slide_type": "slide"}
'''Este es un comentario''' # Triple comillas para comentarios. Numeral para comentarios en linea

print("Hello World!")

# + slideshow={"slide_type": "slide"}
# Declaración de variables

string = 'Hola'
print(string)
entero = 1
print(entero)
flotante = 1.0
print(flotante)
tupla = (entero,flotante)
print(tupla)
nupla = (entero,flotante,string)
print(nupla)
lista = [entero,flotante,string]
print(lista)
diccionario = {'1':tupla,50:nupla,'3':entero}
print(diccionario)
conjunto = set([1,2])
print(conjunto)
booleano = True
print(booleano)

# +
# Pueden cambiar de tipo

elemento = 1
print(elemento) 
print(type(elemento))
elemento = str(1)
print(elemento)
print(type(elemento))

# Pueden redefinirse
elemento = ['dos']

print(elemento)
print(type(elemento))


# + [markdown] slideshow={"slide_type": "slide"}
# ## Funciones en Python

# + slideshow={"slide_type": "slide"}
# Definir una función

def suma(a,b):
    return a+b

print(suma(1,2))
print(suma(1.0,2.0))
print(suma(1.0,2))
print(suma("hola ","como te va"))
print(suma([1,2,3],[4,5]))
print(suma("1",3)) # Falla


# +
# El valor por default de divisor es 1

def division(dividendo,divisor=1):
    return dividendo/divisor

print(division(4)) # Usa el valor por default
print(division(1,2)) # Parámetros por orden
print(division(dividendo=1,divisor=2)) # Parámetros por nombre
print(division(divisor=2,dividendo=1))

# +
# Funciones básicas ya en el lenguaje
# Hechas para funcionar para distintos tipos

string_ordenado = sorted('bca')
print(string_ordenado)

lista_ordenada = sorted([1,3,2])
print(lista_ordenada)

separadas = "hola, don, pepito".split(",")
print(separadas)
unidas = "".join(separadas)
print(unidas)

# + [markdown] slideshow={"slide_type": "slide"}
# ## Diferencia entre lista y tupla
# Las listas se caracterizan por ser mutables, es decir, se puede cambiar su contenido en tiempo de ejecución, mientras que las tuplas son inmutables ya que no es posible modificar el contenido una vez creada.

# + [markdown] slideshow={"slide_type": "slide"}
# ### Listas de Python

# + slideshow={"slide_type": "slide"}
# Como hacer una lista
lista = [] # A modo de ejemplo llamamos a la lista "lista", pero no deben llamar a las variables por su tipo

# Como agregar cosas a la lista
print(lista)
lista.append(1) # Inserto un 1 al final
lista.append("dos") # Inserto un "dos" al final
lista.append(3.0) # Inserto un 3.0 al final
lista.insert(2,10) # Inserto en posicion 2 un 10
print(lista)

# +
# Como iterar una lista elemento por elemento
print("Primera iteración")
for elemento in lista:
    print ("\t",elemento)

print("Segunda iteración")
for i, elemento in enumerate(lista):
    print("\tIndice:",i)
    print("\tValor:",elemento)
    
# Como hacer un ciclo for que recorra la lista
print("Tercera iteración")
for i in range(0,2):
    print("\t",lista[i])

# Como hacer un ciclo while que recorra la lista
print("Cuarta iteración")
i = 0
while i < len(lista):
    print("\t",lista[i])
    i += 1 # No se puede hacer i++ o ++i

# Como remover por elemento
lista.remove(1) # Elimina la primer aparición de 1
print(lista)

# Como remover por posicion
elemento = lista.pop(1) # Elimina el elemento en la posición pasada por parámetro
                        # si no se le pasa nada elimina el último
print(elemento)
print(lista)

# + [markdown] slideshow={"slide_type": "slide"}
# ### Tuplas de Python

# + slideshow={"slide_type": "slide"}
# Como hacer una tupla
tupla = (1,2)  # Las tuplas son inmutables. No se pueden crear e ir agregando cosas

print(tupla)
print(tupla[0])
print(tupla[1])

tupla[1] = 3 # Falla. No se puede mutar
# -

# ### Slices
#
# **Valen para listas, tuplas o strings (_segmentos_)**

# +
numeros = [0,1,2,3,4,5,6,7,8,9,10]

print(numeros)
print(numeros[2]) # Imprimo elemento en la posición 2
print(numeros[-1]) # # Imprimo elemento en la última posición

print(numeros[0:2]) # Imprimo de la pos 0 a la pos 2
print(numeros[-4:-2])
print(numeros[0:80]) 
print(numeros[:3])
print(numeros[3:])
print(numeros[::2])

numeros[7] = 'siete' # Las listas se pueden mutar
print(numeros)

numeros = numeros[::-1]
print(numeros)
# -

print(numeros[15]) # Falla. No se puede acceder a una posición inexistente

palabra = 'palabra'
print(palabra)
print(palabra[3])
print(palabra[:3])
print(palabra[3:])

# +
tupla = (0,1)

print(tupla)
print(tupla[0])
print(tupla[1])

tupla[3] = 2 # Falla. No se puede cambiar algo en una tupla. Es inmutable!


# -

# ## Condicionales (if...elif...else)
#
# ```
# if <condición_1>:
#     <hacer algo_1 si se da la condición_1>
# elif <condición_2>:
#     <hacer algo_2 si se da la condición_2>
# ...
# elif <condición_n>:
#     <hacer algo_n si se da la condición_n>
# else:
#     <hacer otra cosa si no dan las anteriores>
# ```
#
#

# + slideshow={"slide_type": "slide"}
def busqueda_binaria(lista, elemento):
    # not equivale a ! en C
    # True y False empiezan con mayúscula
    if not lista: return False
    elif len(lista) == 1: # len(lista) devuelve el largo de la lista
        return lista[0] == elemento
    mitad = len(lista)//2 # // es la operación división entera
    if lista[mitad] == elemento: return True
    if lista[mitad] > elemento:
        return busqueda_binaria(lista[:mitad],elemento)
    if lista[mitad] < elemento:
        return busqueda_binaria(lista[mitad:],elemento)
    
print(busqueda_binaria([1,2,3,4,5],4))
print(busqueda_binaria([1,4,6,7,9,10],2))

# + [markdown] slideshow={"slide_type": "slide"}
# ## Diccionarios de Python
#
# Son como hashmaps, las claves deben ser inmutables para que no pierda sentido el diccionario. Si se pudieran modificar, se podrían cambiar las claves y generaría conflictos.
#
# Tipos mutables:
# - Listas
# - Diccionarios
# - Sets
#
# Tipos inmutables:
# - Int
# - Float
# - String
# - Tuplas
#

# + slideshow={"slide_type": "slide"}
# Cómo hacer un diccionario
diccionario = {}

# Cómo agregar cosas al diccionario
diccionario['clave1'] = 'valor1'
diccionario[2] = 'valor2'
diccionario['clave3'] = 3
print(diccionario)

# {('clave1','valor1'),('clave2','valor2'),('clave3',3)}
print(diccionario.get('clave3',2))  # Equivalente a diccionario['clave3']
                                    # pero en caso de no tener la clave, devuelve
                                    # un elemento por default (en este caso 2)

print ('clave1' in diccionario) # Verifico si la clave está en el diccionario

# Cómo iterar un diccionario elemento por elemento
print("Primera iteración")
for clave,valor in diccionario.items(): # diccionario.items() va devolviendo tuplas con el formato (clave,valor)
                                        # con esta sintaxis se desempaquetan en clave y valor (similar a enumerate)
    print("\tClave: " + str(clave))
    print("\tValor: " + str(valor))
    
print("Segunda iteración: claves")
for clave in diccionario.keys():
    print("\t"+str(clave))
    
print("Tercera iteración: valores")
for valor in diccionario.values():
    print("\t"+str(valor))
# -

# ## Sets
#
# Son similares a los diccionarios (en eficiencia) pero se almacenan solo claves, y tienen algunas operaciones particulares.
#
# En particular, no pueden tener elementos iguales (pensar que son conjuntos)

help("set")

# Se definen como los diccionarios pero sin hacerlos 'clave:valor', solamente una seguidilla de elementos
{1,2,2,3}

# ## Módulos
#
# Para incluir alguna biblioteca de funciones se usa `import`. Pueden ser cosas ya predefinidas en Python (`math`, `random`, etc), nombres de archivos en nuestro directorio (por ejemplo, para `mimodulo.py` ponemos `import mimodulo`) o bibliotecas instaladas por el usuario

# +
import math
print(math.pi)

from math import pi
print(pi)
# -

# ## Manejo de excepciones
#
# Se pueden encapsular errores esperados en un bloque 'try/except' para evitar cortar el flujo del programa

division(1,0) # No se puede dividir por cero

try:
    division(1,0)
except ZeroDivisionError:
    print('No se puede dividir por cero, ojo!')

# + [markdown] slideshow={"slide_type": "slide"}
# ## Lectura y escritura de archivos

# + slideshow={"slide_type": "slide"}
import random
with open('archivo.csv','w') as archivo: # Al usar esta sintaxis no es necesario hacer close
    archivo.write("Alumno, nota\n")
    # Tambien de forma similar al fprintf se puede hacer:
    # print("Alumno, nota\n", file=archivo)
    for i in range(0,10):
        archivo.write(str(i) + "," + str(random.randrange(0,10))+"\n")

print(archivo)  # Comentario aclaratorio:
                # Las variables definidas en un determinado scope siguen existiendo por fuera del mismo.
                # Se debe tener cuidado con esto, ya que nada garantiza que por fuera el valor sea el esperado.

# + slideshow={"slide_type": "slide"}
with open('archivo.csv','r') as f:
    for linea in f:
        print(linea)
#        print(linea, end="") # Reemplaza "\n" por ""

# + [markdown] slideshow={"slide_type": "slide"}
# ### Archivos CSV

# + slideshow={"slide_type": "slide"}
import csv
with open('archivo.csv','r') as f:
    f_reader = csv.DictReader(f,delimiter=',')
    #f_reader = csv.reader(f,delimiter = ',') # Devuelve lista de elementos
    for row in f_reader:
        print(row)

# + slideshow={"slide_type": "slide"}
from csv import writer as writerPiola
with open('archivo.csv','w') as f:
    f_writer = writerPiola(f,delimiter=',')
    f_writer.writerow([1,2])
    f_writer.writerow([2,3])
    f_writer.writerow([4,5])


# + [markdown] slideshow={"slide_type": "slide"}
# ## Objetos
#
# Los objetos tienen metodos y atributos:
# - Atributos: equivalentes a variables.
# - Métodos: equivalentes a las primitivas.
#
# Se puede trazar una equivalencia entre los objetos y los structs de C, "ambas son estructuras en las que se le pueden guardar cosas".
#
# La clase de un objeto es el tipo.
#
# Por ejemplo:
#
# En C, para definir un nodo haciamos:

# + [markdown] slideshow={"slide_type": "slide"}
# ```C
# typedef struct nodo {
#     void* dato;
#     struct nodo* siguiente;
# } nodo_t;
# ```

# + [markdown] slideshow={"slide_type": "slide"}
# ### Cómo creo una clase

# + slideshow={"slide_type": "slide"}
class Nodo (object):
    
    def __init__(self,dato,siguiente = None):
        self.dato = dato
        self.siguiente = siguiente
            
    def obtener_dato(self):
        return self.dato;
    
    def proximo(self):
        return self.siguiente

    def __repr__(self):
        return str(self.dato)
    
    def __str__(self):
        return str(self.dato)


# + slideshow={"slide_type": "slide"}
nodo = Nodo("hola")
print(nodo)
nodo2 = Nodo("lala")
print([nodo,nodo2])
nodo3 = nodo.obtener_dato()
print(nodo3)


# + [markdown] slideshow={"slide_type": "slide"}
# ### Ejemplo: Lista Enlazada

# + slideshow={"slide_type": "slide"}
class Lista_Enlazada(object):
    
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.largo = 0
    
    def insertar_al_principio(self,dato):
        nodo = Nodo(dato, self.primero)
        self.primero = nodo
        self.largo += 1
        if self.largo == 1:
            self.ultimo = nodo
            
    def insertar_al_final(self,dato):
        if self.largo != 0:
            nodo = Nodo(dato)
            nodo_anterior = self.ultimo
            nodo_anterior.siguiente = nodo
            self.ultimo = nodo
            self.largo += 1
        else:
            self.insertar_al_principio(dato)

    def ver_primero(self):
        return self.primero.obtener_dato();
    
    def borrar_primero(self):
        dato = self.primero.obtener_dato()
        self.primero = self.primero.siguiente
        self.largo -= 1
        if self.largo == 0:
            self.ultimo = None
        return dato
            
    def __str__(self):
        cadena = ""
        nodo_actual = self.primero
        while nodo_actual is not None:
            cadena += str(nodo_actual.obtener_dato())
            cadena += " | "
            nodo_actual = nodo_actual.siguiente
        return cadena
        
        
lista = Lista_Enlazada()
lista.insertar_al_principio("Primer Dato")
lista.insertar_al_principio("Primer primer Dato")
elemento = lista.ver_primero()
print(elemento)
print(str(lista))

# + [markdown] slideshow={"slide_type": "slide"}
# ### Librería para Heaps

# + slideshow={"slide_type": "slide"}
import heapq

heap = [5,2,3,7,2,20,1]
heapq.heapify(heap)
print(heap)

heapq.heappush(heap,27)
print(heap)

menor = heapq.heappop(heap)
print(menor)
print(heap)

n_menores = heapq.nsmallest(3,heap)
print(n_menores)

# -

# ### Y como hacer un Max-Heap

class Nodo_heap(object):
    def __init__(self,dato):
        self.dato = dato
    
    def obtener_valor():
        return dato
    
    def __lt__(self, other):
        return self.dato>other.dato
    
    def __gt__(self, other):
        return self.dato<other.dato
    
    def __eq__(self, other):
        return self.dato==other.dato

    def __str__(self):
        return str(self.dato)
    
    def __repr__(self):
        return str(self.dato)


heap = [Nodo_heap(5),Nodo_heap(2),Nodo_heap(3),Nodo_heap(7),Nodo_heap(2),Nodo_heap(20),Nodo_heap(1)]
heapq.heapify(heap)
print(heap)

# ### Concepto de Cola
#
# El comportamiento de una cola se puede describir con la frase "Lo primero que se encoló es lo primero que se usa". Es decir, su estructura es **FIFO (First in, First out)**
#
# Suponiendo que implementamos una **cola** usando una **lista**. ¿Cómo se podría implementar? ¿Cuál sería el costo?
#
# **Opción 1:**
#    * enqueue encola al principio de la lista
#    * dequeue desencola del final de la lista
#     
# **Opción 2:**
#    * enqueue encola al final de la lista
#    * dequeue desencola del principio de la lista
#
#
# *Problema*: En el primer caso encolar y en el segundo caso desencolar del principio implica desplazar todo el contenido de la lista (en un sentido u otro). Esta operación es costosa, imaginense una lista muy grande!

# ### Deque como Cola
#
# **Deque**: diseñado para appends y pops eficientes en ambos extremos
#
#
# * Operación encolar: se usa la función ```append()```
# * Operacion dequeue (desencolar): se usa la función ```popleft()```

# +
from collections import deque

queue = deque(["a", "b", "c"])
print(queue)
queue.append("d")
print(queue)
queue.popleft()
print(queue)
print(type(queue))
# -

# ## Recursos
#
# * [Documentación de Python 3](https://docs.python.org/3/tutorial/)
#
# * [Apunte de Algoritmos y Programación I](https://algoritmos1rw.ddns.net/material)
#
# * [Automate the Boring Stuff with Python](http://automatetheboringstuff.com/)
#
# * [Curso Python](https://pythoncurso.github.io)
#
# * [Python Tutor](http://pythontutor.com/)
#
# * [Learn Python3 in Y minutes](https://learnxinyminutes.com/docs/python3/)
#
# * [Bibliografía de Algoritmos y Programación I](https://algoritmos1rw.ddns.net/bibliografia)
