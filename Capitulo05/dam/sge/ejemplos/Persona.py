# -*- coding: utf-8 -*- 
'''
Created on 23/10/2014

@author: Luismi
'''

class Persona(object):
    '''
    classdocs
    '''
    def __init__(self, nombre, apellidos):
        '''
        Constructor
        '''
        self.__nombre = nombre
        self.__apellidos = apellidos

    def get_datos(self):
        return self.__nombre, self.__apellidos
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos
        
    def get_nombre(self):
        return self.__nombre
    
    def get_apellidos(self):
        return self.__apellidos
# Fin de la clase

separador = ''
if (True):
    separador = '/'
else:
    separador = '\\'


if __name__=='__main__':     
    p = Persona('Jose Ignacio', 'Barragan')
    print p.get_nombre(), p.get_apellidos()    
   

 
