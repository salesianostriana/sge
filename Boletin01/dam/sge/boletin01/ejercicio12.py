# -*- coding: utf-8 -*- 
'''
Created on 5/10/2014

Ejercicio 13
Introducir dos numeros por teclado. Imprimir los numeros que hay entre ellos comenzando por 
el m�s peque�o. Contar cuantos hay y cu�ntos de ellos son pares. Calcular la suma de los pares
.

@author: Luismi
'''
a = int(raw_input("Introduzca el primer numero: "))
b = int(raw_input("Introduzca el segundo numero: "))

peque = min(a,b)
grande = max(a,b)

cuantos = pares = sumapares = 0

for i in range(peque,grande+1):
    print i
    cuantos += 1
    if (i % 2 == 0):
        pares += 1
        sumapares += i

print "Entre ", peque, " y ", grande, " hay ", cuantos, " numeros (ambos inclusive), donde ", pares, " son pares, y su suma es ", sumapares
