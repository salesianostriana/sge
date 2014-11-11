# -*- coding: utf-8 -*- 
'''
Created on 9/11/2014

@author: Luismi
'''

fichero = open('../datos_ficheros.txt','r')
lineas = fichero.readlines()

acumulador = 1

for n in lineas[len(lineas)-1].split("   "):
    acumulador *= int(n)
    
print acumulador

fichero.close()