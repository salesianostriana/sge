# -*- coding: utf-8 -*- 
'''
Created on 12/10/2014

Ejercicio 10

Escriba un programa que pida un número y a continuación escriba la lista de todos los
divisores del número (incluidos el uno y él mismo).

@author: Luismi
'''


n = int(raw_input("Introduzca un numero: "))

lista = []

for i in range(1,n+1):
    if (n % i == 0):
        lista.append(i)

print lista