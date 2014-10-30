# -*- coding: utf-8 -*- 
'''
Created on 28/10/2014

@author: Luismi
'''
from Cuenta import *

dineroCaja = int(raw_input("Introduzca el dinero que usted tiene en la caja de ahorro:\n"))

dinero = Cuenta(dineroCaja)

# pin = int(raw_input("Introduzca el pin para consultar el saldo"))

# print dinero.leer_saldo(pin)

print dinero._Cuenta__saldo
