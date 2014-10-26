# -*- coding: utf-8 -*- 
'''
Created on 5/10/2014

Ejercicio 8
Escriba un programa que pida los coeficientes de una ecuación de segundo grado (ax²+ b x + c = 0) 
y escriba la solución. Se recuerda que una ecuación de segundo grado
puede no tener solución, tener una solución única, tener dos soluciones o que todos
los números sean solución. Se recuerda que la fórmula de las soluciones cuando hay
dos soluciones es x = (-b ± √(b2-4ac) ) / (2a)

@author: Luismi
'''
from cmath import sqrt

print "(ax²+ b x + c = 0)" 
a = int(raw_input("Introduzca el coeficiente a: "))
b = int(raw_input("Introduzca el coeficiente b: "))
c = int(raw_input("Introduzca el coeficiente c: "))

''' El numero de soluciones de una ecuacion de segundo grado lo marca el discriminante

    D = b^2-4ac
    
    D > 0, entonces tenemos dos soluciones reales
    D = 0, entonces tenemos dos soluciones reales iguales, es decir, una solucion
    D < 0, entonces no existen soluciones reales.
    
'''

d = (b**2)-(4*a*c)

if (d < 0):
    print "No existen soluciones reales"
elif (d == 0):
    print "La solucion unica es: " (-b+sqrt(d))/(2*a)
else:
    print "La primera solucion es: ", (-b+sqrt(d))/(2*a)
    print "La segunda solucion es: ", (-b-sqrt(d))/(2*a)