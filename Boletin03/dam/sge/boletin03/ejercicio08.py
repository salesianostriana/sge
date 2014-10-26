# -*- coding: utf-8 -*- 
'''
Created on 12/10/2014

Ejercicio 8

Escriba un programa que pida dos n�meros enteros y escriba la 
lista de n�meros pares
que hay entre ellos (incluidos ellos mismos si son pares)

@author: Luismi
'''

# Devuelve verdadero si un numero es par
def es_par(n):
    return (n % 2 == 0)

# Devuelve -1 si el signo del numero es negativo, y 1 en caso de que sea 0 o positivo
def sign(n):
    return 1 if (n >= 0) else -1

# Inicio del programa
n = int(raw_input("Introduzca el primer numero entero: "))
m = int(raw_input("Introduzca el segundo numero entero: "))
'''
La siguiente sentencia equivale a esta estructura de decision
if (n < m):
    inc = 2
else:
    inc = -2
'''
inc = 2 if n < m else -2

# El inicio de nuestra lista sera el primer numero, n
# si es par. Si no, es el siguiente, n+1
inicio = n if es_par(n) else n+(sign(inc)*1)
# El final de nuestra lista es m, pero como usaremos la funcion
# range, usamos m+1; pero solo si es par; si no lo fuese, el final
# de la lista es m-1,  pero como usamos range, usamos m.
#fin = m+1 if es_par(m+2) else m
fin = m+(sign(inc)*1)

print(list(range(inicio, fin, inc)))