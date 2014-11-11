# -*- coding: utf-8 -*- 
'''
Created on 9/11/2014

@author: Luismi
'''

fichero = open('../datos_ficheros_copy.txt','a')
for n in range(1,11):
    fichero.write(str(n)+"   ")
fichero.close()