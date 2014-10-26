# -*- coding: utf-8 -*- 
'''
Created on 5/10/2014

Ejercicio 7
Calcular e imprimir el producto 1*2*3*4*5*...*20

@author: Luismi
'''
i= 1
for j in range(1,20):
    i*=j
    
print i

def producto(x,y):
    return x*y

print reduce(producto,range(1,20)) 
