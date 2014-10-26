# -*- coding: utf-8 -*- 
'''
Created on 12/10/2014

Ejercicio 2

Escriba un programa que pida un numero entero mayor que cero y escriba varias
listas de numeros consecutivos, como indican los ejemplos siguientes:

Escriba un numero mayor que 0: 0
¡Le he pedido un numero entero mayor que 0!

Escriba un numero mayor que 0: 5
[0, 1, 2, 3, 4, 5]
[5, 4, 3, 2, 1, 0]
[1, 2, 3, 4]
[4, 3, 2, 1]
[0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]

...


@author: Luismi
'''

# Pedimos el número entero.
# Lo hacemos mediante un bucle while con lectura anticipada
n = int(raw_input("Introduzca un numero entero mayor que 0: "))

while (n <= 0):
    print "¡Le he pedido un numero entero mayor que 0"
    n = int(raw_input("Introduzca un numero entero mayor que 0: "))
    

print(list(range(n+1)))
print(list(range(n,-1,-1)))
print(list(range(1,n)))
print(list(range(n-1,0,-1)))
print(list(range(n)+range(n,-1,-1)))