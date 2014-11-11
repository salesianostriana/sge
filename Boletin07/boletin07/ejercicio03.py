# -*- coding: utf-8 -*- 
'''
Created on 7/11/2014

@author: Luismi
'''

from ejercicio01 import *
from ejercicio02 import *


user = raw_input("Introduzca un nombre de usuario: ")
password = raw_input("Introduzca una contraseña válida: ")


if (not validar_user(user) or not validar_pass(password)):
    print "El nombre de usuario o contraseña no son validos"
else:
    print "Usuario y contraseña válidos"