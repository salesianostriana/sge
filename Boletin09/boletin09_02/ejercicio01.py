# -*- coding: utf-8 -*- 
'''
Created on 9/11/2014

@author: Luismi
'''


fichero = open('../datos_ficheros.txt','r')
lineas = fichero.readlines()

cont = 0

for l in lineas:
    if l.startswith("#"):
        cont += 1
        
        
print str(len(lineas) - cont)

fichero.close()