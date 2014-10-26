# -*- coding: utf-8 -*- 
'''
Created on 12/10/2014

Ejercicio 4

Escriba un programa que permita crear una lista de palabras y que, a continuaci�n,
pida una palabra y elimine esa palabra de la lista.


@author: Luismi
'''


from ejercicio02 import construir_lista_palabras

lista = construir_lista_palabras()

a_buscar = raw_input("Introduzca la palabra a buscar en la lista para ser eliminada: ")

lista.remove(a_buscar)

print lista
