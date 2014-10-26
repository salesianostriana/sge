# -*- coding: utf-8 -*- 
'''
Created on 12/10/2014

Ejercicio 5

Escriba un programa que permita crear dos listas de palabras y que, a continuaci�n,
elimine de la primera lista los nombres de la segunda lista.

NOTA: Se introduce, a modo de ejemplo, el manejo de excepciones, para hacer el 
      ejercicio más fácil.

@author: Luismi
'''


from ejercicio02 import construir_lista_palabras

lista1 = construir_lista_palabras()
lista2 = construir_lista_palabras()

for palabra in lista2:
    try: 
        lista1.remove(palabra)
    except ValueError:
        print palabra, " no se encuentra en la primera lista"

print lista1

