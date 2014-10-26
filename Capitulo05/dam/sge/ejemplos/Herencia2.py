# -*- coding: utf-8 -*- 

'''
Created on 21/10/2014

@author: Luismi
'''

class Madre(object):
    '''
    classdocs
    '''
    def __init__(self, valor1, valor2):
        '''
        Constructor
        '''
        self.__val1 = valor1
        self.__val2 = valor2
        
    
class Hija(Madre):
    
    def __init__(self, valor1, valor2, valor3):
        super(Hija, self).__init__(valor1, valor2)
        self.__val3 = valor3
    


h = Hija(1,2,3)
print h._Hija__val3
m = Madre(1,2)
print m._Madre__val2