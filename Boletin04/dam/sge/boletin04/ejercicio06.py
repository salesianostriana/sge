# -*- coding: utf-8 -*- 
'''
Created on 12/10/2014

Ejercicio 6

Escriba un programa que permita crear una lista de palabras y que, a continuaci�n,
cree una segunda lista igual a la primera, pero al rev�s (no se trata de escribir la lista al
rev�s, sino de crear una lista distinta).


@author: Luismi
'''

from ejercicio02 import construir_lista_palabras
# Creamos la lista
lista = construir_lista_palabras()

# Instanciamos una lista, que será la que almacene los valores en orden inverso
lista_inversa = []

# Llenamos la lista con los valores de la original
lista_inversa.extend(lista)

# Modificamos el orden, invirtiendolo
lista_inversa.reverse()

# Imprimimos la lista invertida
print lista_inversa
