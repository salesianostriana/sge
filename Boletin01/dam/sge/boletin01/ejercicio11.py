# -*- coding: utf-8 -*- 
'''
Created on 5/10/2014

Ejercicio 11
Imprimir los n�meros del 1 al 100 y calcular la suma de todos los n�meros pares por un lado, y por otro, la de los impares.

@author: Luismi
'''

par = 0;
impar = 0;

for i in range(1,101):
    if (i % 2 == 0):
        par+= i
    else:
        impar+=i
    print i

print "Suma de los numeros pares: ", par
print "Suma de los numeros impares: ", impar

