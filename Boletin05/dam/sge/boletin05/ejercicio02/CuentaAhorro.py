# -*- coding: utf-8 -*- 
'''
Created on 28/10/2014

@author: Luismi
'''

from Cuenta import *

class CuentaAhorro(Cuenta):
    
    def __avisar(self):
        if (self.leer_saldo(3210) < 0):
            print "Numeros rojos!!!"
            
    def retirar(self, retirada):
        #return Cuenta.retirar(self, retirada)
        if (self.leer_saldo(3210) < 0):
            print "No tiene credito!!!"
            return self.leer_saldo(3210)
        else:
            saldo = Cuenta.retirar(self, retirada)
            if (saldo < 0):
                self.__avisar()
            return saldo