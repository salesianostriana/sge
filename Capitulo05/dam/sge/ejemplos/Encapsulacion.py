# -*- coding: utf-8 -*- 
'''
Created on 20/10/2014

@author: Luismi
'''

class Mamifero(object):
    '''
    classdocs
    '''
    def __init__(self, num_extremidades, tiempo_gestacion):
        '''
        Constructor
        '''
        self.__numero_extremidades = num_extremidades
        self.__tiempo_gestacion = tiempo_gestacion
        
    
    def get_numero_extremidades(self):
        return self.__numero_extremidades
    
    def get_tiempo_gestacion(self):
        return self.__tiempo_gestacion
    

humano = Mamifero(4,9)
# print dir(humano)
# print humano.numero_extremidades
# print humano.get_numero_extremidades()
# print humano.__numero_extremidades
print humano._Mamifero__numero_extremidades


    
    