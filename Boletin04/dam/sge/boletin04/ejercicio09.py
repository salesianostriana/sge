# -*- coding: utf-8 -*- 
'''
Created on 12/10/2014

Ejercicio 9

Escriba un programa que permita crear una lista de palabras y que, a continuaci�n,
ordene la lista por orden alfab�tico.

@author: Luismi
'''

from ejercicio02 import construir_lista_palabras
# Creamos la lista
lista = construir_lista_palabras()

lista.sort()

print lista