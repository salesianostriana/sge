# -*- coding: utf-8 -*- 
'''
Created on 12/10/2014

Ejercicio 8

Escriba un programa que permita crear dos listas de palabras y que, a continuaci�n,
escriba las siguientes listas (en las que no debe haber repeticiones):

- Lista de palabras que aparecen en las dos listas.
- Lista de palabras que aparecen en la primera lista, pero no en la segunda.
- Lista de palabras que aparecen en la segunda lista, pero no en la primera.
- Lista de palabras que aparecen en ambas listas.

@author: Luismi
'''

from ejercicio02 import construir_lista_palabras

def elimina_repetidos(l):
    lista = []
    for palabra in l:
        if (lista.count(palabra) == 0):
            lista.append(palabra)
    return lista



lista1 = construir_lista_palabras()
lista2 = construir_lista_palabras()

# Resultado 1
lista_res_1 = []

for palabra in lista1:
    if (lista2.count(palabra) > 0):
        lista_res_1.append(palabra)

lista_res_1 = elimina_repetidos(lista_res_1)        

print lista_res_1

# Resultado 2
lista_res_2 = []

for palabra in lista1:
    if (lista2.count(palabra) == 0):
        lista_res_2.append(palabra)

lista_res_2 = elimina_repetidos(lista_res_2)        

print lista_res_2

# Resultado 3
lista_res_3 = []

for palabra in lista2:
    if (lista1.count(palabra) == 0):
        lista_res_3.append(palabra)

lista_res_3 = elimina_repetidos(lista_res_3)        

print lista_res_3

# Resultado 4
lista_res_4 = lista1 + lista2

lista_res_4 = elimina_repetidos(lista_res_4)        


print lista_res_4