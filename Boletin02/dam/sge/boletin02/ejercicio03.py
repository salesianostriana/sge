# -*- coding: utf-8 -*- 
'''
Created on 5/10/2014

@author: Luismi
'''

actual = int(raw_input("Introduzca el a�o actual: "))
otro = int(raw_input("Introduzca otro a�o: "))



if (actual > otro):
    print "Han pasado ", actual-otro, " a�os"
elif (actual < otro):
    print "Faltan por pasar ", otro-actual, " a�os"
else:
    print "No hay diferencias entre las dos fechas"