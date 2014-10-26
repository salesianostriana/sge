# -*- coding: utf-8 -*- 
'''
Created on 23/10/2014

@author: Luismi
'''


class CuentaCorriente(object):
    
    def __init__(self, saldo):
        self.__saldo = saldo
        
    def get_saldo(self):
        return self.__saldo
    
    def aumentar_saldo(self,cantidad):
        self.__saldo += cantidad
        
    def decrementar_saldo(self, cantidad):
        self.__saldo -= cantidad
        
    def set_saldo(self, cantidad):
        self.__saldo = cantidad
        
    def __lt__(self,otro):
        return (self.__saldo < otro.get_saldo())
      
    def __add__ (self,otro):
        self.__saldo += otro.get_saldo()
        otro.set_saldo(0)  
        
    
if __name__ == '__main__':
    c1 = CuentaCorriente(1000)
    c2 = CuentaCorriente(2000)

    if (c1 < c2):
        print 'La cuenta c1 es menor que la c2'
    else:
        print 'La cuenta c2 es menor o igual que la c1'
    
    print c1.get_saldo()
    c1+c2
    print c1.get_saldo()
        