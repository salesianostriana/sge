# -*- coding: utf-8 -*- 
'''
Created on 5/10/2014

Ejercicio 16
Introducir los valores A, B y C: Si A/B>30, calcular e imprimir A/C * B^3
; si A/B<=30, calcular e imprimir 2^2+4^2+6^2+...+30^2

@author: Luismi
'''

a = int(raw_input("Introduzca el primer numero: "))
b = int(raw_input("Introduzca el segundo numero: "))
c = int(raw_input("Introduzca el tercer numero: "))

if (a / b > 30):
    print "El resultado es: ", a / (c * (c**3))
else:
    acumulador = 0
    for i in range (2,31,2):
        acumulador+= i**2
    print "El resultado es: ", acumulador