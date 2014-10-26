# -*- coding: utf-8 -*- 
'''
Created on 5/10/2014

Ejercicio 2
Escriba un programa que pida dos n�meros y que conteste cu�l es el menor y cu�l el mayor o que escriba que son iguales.

@author: Luismi
'''

a = int(raw_input("Introduzca el primer numero: "))
b = int(raw_input("Introduzca el segundo numero: "))

if (a < b):
    print a, " es menor que ", b
elif (a > b):
    print a, " es mayor que ", b
else:
    print a, " y ", b, " son iguales"