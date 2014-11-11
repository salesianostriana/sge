# -*- coding: utf-8 -*- 
'''
Created on 9/11/2014

@author: Luismi
'''
fichero_lectura = open('../datos_ficheros.txt','r')
fichero_escritura = open('../datos_ficheros2.txt','w')

linea = fichero_lectura.readline()
numeros = linea.split("   ")

acumulador = 0

for n in numeros:
    acumulador+= int(n)
    print n
    
fichero_escritura.write(str(acumulador))

print "El resultado de la suma es", acumulador

fichero_lectura.close()
fichero_escritura.close()