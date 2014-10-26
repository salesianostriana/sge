# -*- coding: utf-8 -*- 

'''
Created on 21/10/2014

@author: Luismi
'''

class B(object):
    '''
    classdocs
    '''
    def __init__(self, val1):
        '''
        Constructor
        '''
        #print val1
        
        
class C(object):
    def __init__(self):
        '''
        Constructor
        '''
        #print "El valor es", val1
        print "constructor!!!"
        

class D(C, B):
    pass


d = D()
        