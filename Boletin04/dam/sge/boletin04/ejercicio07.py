# -*- coding: utf-8 -*- 
'''
Created on 12/10/2014

Ejercicio 7

Escriba un programa que permita crear una lista de palabras y 
que, a continuaci�n,
elimine los elementos repetidos (dejando �nicamente el 
primero de los elementos
repetidos).


@author: Luismi
'''

from ejercicio02 import construir_lista_palabras
# Creamos la lista
lista = construir_lista_palabras()

lista_sin_repetidos = []

for palabra in lista:
    if (lista_sin_repetidos.count(palabra) == 0):
        lista_sin_repetidos.append(palabra)


print lista_sin_repetidos