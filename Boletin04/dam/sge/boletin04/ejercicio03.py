# -*- coding: utf-8 -*- 
'''
Created on 12/10/2014

Ejercicio 3

Escriba un progra ma que permita crear una lista de palabras y que, a continuaci�n,
pida dos palabras y sustituya la primera por la segunda en la lista.


@author: Luismi
'''


from ejercicio02 import construir_lista_palabras

lista = construir_lista_palabras()

sustituida = raw_input("Introduzca la palabra a buscar en la lista: ")
sustituta = raw_input("Introduzca la palabra con la que sustituiremos en la lista: ")

for i in range(len(lista)):
    if (lista[i] == sustituida):
        lista[i] = sustituta
        
print lista    