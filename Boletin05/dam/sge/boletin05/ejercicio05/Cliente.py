# -*- coding: utf-8 -*- 
'''
Created on 30/10/2014

@author: Luismi
'''
from dam.sge.boletin05.ejercicio02.CuentaAhorro import CuentaAhorro
from dam.sge.boletin05.ejercicio04.Persona import Persona

class Cliente(Persona, CuentaAhorro):
    
    def __init__(self, persona, cuenta_ahorro, credito=1000):
        #self.set_direccion(persona.get_direccion())
        #self.set_dni(persona.get_dni())
        #self.set_nombre(persona.get_nombre())
        Persona.__init__(self, persona.get_nombre(), persona.get_dni(), persona.get_direccion(), persona.get_telefono(),persona.get_email())
        CuentaAhorro.__init__(self, cuenta_ahorro.leer_saldo(3210))
        self.__credit = credito

    def mostrar(self):
        print "Nombre ", self.get_direccion()
        print "DNI ", self.get_dni()
        print "Direccion ", self.get_direccion()
        print "Saldo", self.leer_saldo(3210)
        print "Credito ", self.__credit
        
    