# -*- coding: utf-8 -*- 
'''
Created on 5/10/2014

Ejercicio 7
Escriba un programa que pida los coeficientes de una ecuaci�n de primer grado (a x + b = 0) y 
escriba la soluci�n. Se recuerda que una ecuaci�n de primer grado puede no
tener soluci�n, tener una soluci�n �nica, o que todos los n�meros sean soluci�n. Se
recuerda que la f�rmula de las soluciones es x = -b / a.

@author: Luismi
'''

print "ax+b=0"
a = int(raw_input("Introduzca el coeficiente a: "))
b = int(raw_input("Introduzca el coeficiente b: "))

if (a == 0):
    print "La ecuacion no tiene solución"
elif (b == 0):
    print "Todos los numeros son solucion de la ecuacion"
else:
    print "La solucion es: ", (-b/a)