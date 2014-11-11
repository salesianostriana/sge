# -*- coding: utf-8 -*- 
'''
Created on 9/11/2014

@author: Luismi
'''
fichero = open('../datos_ficheros.txt','r')
lineas = fichero.readlines()
print len(lineas)
fichero.close()