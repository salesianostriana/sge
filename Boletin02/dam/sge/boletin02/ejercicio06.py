# -*- coding: utf-8 -*- 
'''
Created on 5/10/2014

Ejercicio 6
Escriba un programa que pida un año y que escriba si es bisiesto o no. Se recuerda que
los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los
múltiplos de 400 sí. Estos son algunos ejemplos de posibles respuestas: 2012 es
bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.

@author: Luismi
'''

def bisiesto(anio):
    return ((anio % 400 == 0) or ((anio % 4 == 0) and (anio % 100 != 0)))


anio = int(raw_input("Introduzca un año: "))

if (bisiesto(anio)):
    print "El año es bisiesto"
else:
    print "El año no es bisiesto"