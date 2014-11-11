# -*- coding: utf-8 -*- 
'''
Created on 9/11/2014

@author: Luismi
'''

fichero = open('../datos_ficheros.txt','r')
lineas = fichero.readlines()

acumulador = 0

for l in lineas:
    datos = l.split("   ")
    for d in datos:
        if (int(d) % 2 == 1):
            acumulador += int(d)
    
print acumulador

fichero.close()