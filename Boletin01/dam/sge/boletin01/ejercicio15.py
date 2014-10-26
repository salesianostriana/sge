# -*- coding: utf-8 -*- 
'''
Created on 5/10/2014

Ejercicio 15
Introducir dos valores A y B: Si A>=B, calcular e imprimir la suma 10+14+18+...+50 ; si
A/B<=30, calcular e imprimir el valor de (A^2+B^2)

@author: Luismi
'''

a = int(raw_input("Introduzca el primer numero"))
b = int(raw_input("Introduzca el segundo numero"))

if (a >= b):
    suma = 0
    for i in range(10,51,4):
        suma += i
    print "Resultado de la suma 10+14+18+...+50: ", suma
elif (a / b <= 30):
    print "Resultado de (A^2+B^2): ", (a*a)+(b*b)
    