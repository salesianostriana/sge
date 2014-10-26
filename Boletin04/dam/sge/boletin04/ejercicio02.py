# -*- coding: utf-8 -*- 
'''
Created on 12/10/2014

Ejercicio 2

Escriba un programa que permita crear una lista de palabras y que, a continuaci�n,
pida una palabra y diga cu�ntas veces aparece esa palabra en la lista.

@author: Luismi
'''

# Copiamos y pegamos el ejercicio anterior en una funcion, 
# para poder construir la lista de palabras


def construir_lista_palabras():
    lista = []
    n = int(raw_input("Introduzca el numero de palabras que va a insertar: "))
    while (n <= 0):
        print "El numero debe ser positivo"
        n = int(raw_input("Introduzca el numero de palabras que va a insertar: "))
    for i in range(n):
        palabra = raw_input("Introduzca una palabra: ")
        lista.append(palabra)
    return lista

# Esto nos sirve para que solo se ejecute si invocamos el módulo directamente,
# no si lo invocamos a través de una importación
if __name__=='__main__': 
    # Obtenemos la lista de palabras introducidas por el usuario
    lista = construir_lista_palabras()
    
    # Le solicitamos la palabra a buscar
    palabra = raw_input("Introduzca la palabra a buscar en la lista: ")
    
    # Realizamos una búsqueda exhaustiva de la palabra
    cuantas = 0
    for p in lista:
        if p == palabra:
            cuantas += 1
            
    print "La palabra ", palabra, " se ha encontrado ", cuantas, " veces"
    
'''
Todo esto se podría sustituir por la siguiente linea
    
    print "La palabra ", palabra", se ha encontrado ", lista.count(palabra), " veces"
    
'''

