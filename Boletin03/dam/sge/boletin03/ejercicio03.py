# -*- coding: utf-8 -*- 
'''
Created on 12/10/2014

Ejercicio 3

Escriba un programa que pida un numero y escriba una lista de numeros consecutivos
del 0 al valor dado

@author: Luismi
'''

n = int(raw_input("Introduzca un numero entero: "))

if (n >= 0):
    print(list(range(n+1)))
else:
    print(list(range(0,n-1,-1)))
