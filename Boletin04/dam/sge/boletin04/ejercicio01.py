# -*- coding: utf-8 -*- 
'''
Created on 12/10/2014

Ejercicio 1

Escriba un programa que permita crear una lista de palabras. Para ello, el programa
tiene que pedir un n�mero y luego solicitar ese n�mero de palabras para crear la lista.
Por �ltimo, el programa tiene que escribir la lista.



@author: Luismi
'''

lista = []

n = int(raw_input("Introduzca el numero de palabras que va a insertar: "))

while (n <= 0):
    print "El numero debe ser positivo"
    n = int(raw_input("Introduzca el numero de palabras que va a insertar: "))
    
for i in range(n):
    palabra = raw_input("Introduzca una palabra: ")
    lista.append(palabra)
    
print lista


    