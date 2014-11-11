# -*- coding: utf-8 -*- 
'''
Created on 9/11/2014

@author: Luismi
'''

fichero = open('../datos_ficheros.txt','r')
linea = fichero.readline()
print len(linea.split("   "))
fichero.close()