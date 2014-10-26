# -*- coding: utf-8 -*- 
'''
Created on 5/10/2014

@author: Luismi
'''

actual = int(raw_input("Introduzca el año actual: "))
otro = int(raw_input("Introduzca otro año: "))



if (actual > otro):
    print "Han pasado ", actual-otro, " años"
elif (actual < otro):
    print "Faltan por pasar ", otro-actual, " años"
else:
    print "No hay diferencias entre las dos fechas"