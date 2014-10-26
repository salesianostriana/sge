# -*- coding: utf-8 -*- 
'''
Created on 12/10/2014

Ejercicio 11

Escriba un programa que pida un n�mero y a continuaci�n escriba la lista de todos los
n�meros primos hasta �l
.

@author: Luismi
'''

from math import sqrt

def es_primo(n):
    divisor_encontrado = False
    divisor = 2
    tope = sqrt(n)
    while ((not divisor_encontrado) and (divisor <= tope)):
        if (n % divisor == 0):
            divisor_encontrado = True
        else:
            divisor += 1
    return (not divisor_encontrado)


n = int(raw_input("Introduzca un numero: "))

lista_primos = []

for i in range(1,n+1):
    if (es_primo(i)):
        lista_primos.append(i)
        
print lista_primos