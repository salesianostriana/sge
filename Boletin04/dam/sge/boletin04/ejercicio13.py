# -*- coding: utf-8 -*- 
'''
Created on 12/10/2014

Ejercicio 13

Escriba un programa que calcule t�rminos de la sucesi�n Un+1 = 3 Un + 1 si Un es impar y
Un+1 = Un / 2 si Un es par. El programa tiene que pedir el t�rmino U0 y el n�mero de
t�rminos a calcular.

@author: Luismi
'''

inicial = int(raw_input("Introduzca el valor del termino U0: "))
n = int(raw_input("Introduzca el numero de terminos a calcular: "))


lista = []

termino = inicial
for i in range(n):
    lista.append(termino)
    if (termino % 2 == 0):
        termino = termino / 2
    else:
        termino = (3*termino)+1

print lista