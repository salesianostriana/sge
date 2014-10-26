# -*- coding: utf-8 -*- 
'''
Created on 5/10/2014

Ejercicio 6
Calcular e imprimir la suma 1+2+3+4+5+...+50, usando funciones

@author: Luismi
'''
def add(x,y):
    return x+y

print reduce(add, range(1,51))