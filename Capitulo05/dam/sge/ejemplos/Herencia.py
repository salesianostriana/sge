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
        
    def metodo1(self):
        print "Metodo 1 de la clase madre"
        
    def metodo2(self):
        print "Metodo 2 de la clase madre"
        
    def getValor1(self):
        return self.__val1
    
    def getValor2(self):
        return self.__val2
    
class Hija(Madre):
    
    def metodo1(self):
        print "Metodo 1 de la clase hija"
        
    def getValoresSumados(self):
        return self.getValor1()+self.getValor2()
    
    
h = Hija(3,4)
h.metodo1()
h.metodo2()
print h.getValor1()
print h.getValor2()
print h.getValoresSumados()
    
