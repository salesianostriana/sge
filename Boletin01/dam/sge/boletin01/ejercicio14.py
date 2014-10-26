# -*- coding: utf-8 -*- 
'''
Created on 5/10/2014

Ejercicio 14
Imprimir, sumar y contar los n�meros que son a la vez m�ltiplos de 2 y de 3, que hay
entre la unidad y un determinado n�mero introducido por el teclado.

@author: Luismi
'''


tope = int(raw_input("Introduzca el numero tope"))

suma = cuantos = 0

for i in range(1, tope+1):
    if ((i % 2 == 0) and (i % 3 == 0)):
        print i
        suma += i
        cuantos += 1
        
print "Hay ", cuantos, " numeros multiplos de 2 y 3 entre 1 y ", tope, " y su suma da como resultado ", suma