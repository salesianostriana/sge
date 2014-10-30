# -*- coding: utf-8 -*- 
'''
Created on 30/10/2014

@author: Luismi
'''
from dam.sge.boletin05.ejercicio02.CuentaAhorro import CuentaAhorro
from dam.sge.boletin05.ejercicio04.Persona import Persona
from dam.sge.boletin05.ejercicio05.Cliente import Cliente


p = Persona("Luismi","12345678A","C/Rue del percebe 13","600000000")
c = CuentaAhorro(5)

cliente = Cliente(p,c)

cliente.mostrar()