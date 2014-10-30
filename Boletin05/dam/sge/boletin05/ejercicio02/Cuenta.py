# -*- coding: utf-8 -*- 
'''
Created on 28/10/2014

@author: Luismi
'''
class Cuenta:
    
    #saldo = 0
    
    def __init__(self, sald = 0):
        self.__saldo = sald
        self.__pin = 3210
    
    def ingresar(self, ingreso):
        self.__saldo += ingreso
        return self.__saldo

    def retirar(self, retirada):
        self.__saldo -= retirada
        return self.__saldo
    
    def leer_saldo(self, pin):
        if (pin == self.__pin):
            return self.__saldo
        else:
            return "El pin es incorrecto"
