# -*- coding: utf-8 -*- 
'''
Created on 12/10/2014

Ejercicio 10

Escriba un programa que pida un n�mero y a continuaci�n escriba la lista de todos los
divisores del n�mero (incluidos el uno y �l mismo).

@author: Luismi
'''


n = int(raw_input("Introduzca un numero: "))

lista = []

for i in range(1,n+1):
    if (n % i == 0):
        lista.append(i)

print lista