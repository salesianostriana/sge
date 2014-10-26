# -*- coding: utf-8 -*- 
'''
Created on 24/10/2014

@author: Luismi
'''

class Padre(object):
    
    def __init__(self):
        self.__num = 7
        
    def get_num(self):
        return self.__num
    
    def my_print(self):
        print 'Hello desde Padre'
        

class Hija(Padre):
    
    def print_hija(self):
        self.my_print()
        print 'Y desde hija también'
        print self.get_num()
        
        
        
h = Hija()
h.print_hija()