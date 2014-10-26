# -*- coding: utf-8 -*- 
'''
Created on 12/10/2014

Ejercicio 12

Escriba un programa que calcule términos de una sucesión del tipo Un+1 = a Un + b. El
programa tiene que pedir el valor de a, de b y del término U0 y el número de términos
a calcular.

@author: Luismi
'''

a = int(raw_input("Introduzca el valor del coeficiente a: "))
b = int(raw_input("Introduzca el valor del coeficiente b: "))
inicial = int(raw_input("Introduzca el valor del termino U0: "))
n = int(raw_input("Introduzca el numero de terminos a calcular: "))


lista = []
termino = inicial
for i in range(n):
    lista.append(termino)
    termino = (a*termino)+b

print lista
