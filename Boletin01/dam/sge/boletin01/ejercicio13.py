# -*- coding: utf-8 -*- 
'''
Created on 5/10/2014

Ejercicio 13
Imprimir y contar los n�meros m�ltiplos de 3 que hay entre 1 y 100.

@author: Luismi
'''

cuantos = 0

for i in range(1,101):    
    if (i % 3 == 0):
        print i
        cuantos += 1

print "Hay ", cuantos, " numeros multiplos de 3 entre 1 y 100 (ambos inclusive)"
