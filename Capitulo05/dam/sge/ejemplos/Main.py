# -*- coding: utf-8 -*- 
'''
Created on 23/10/2014

@author: Luismi
'''


from Persona import *
#from dam.sge.ejemplos.Persona import separador

p = Persona('Luis Miguel','Lopez Maga�a MAMA')
print p.get_nombre(), p.get_apellidos()

p2 = Persona('Miguel', 'Campos Rivera PAPA')

lista_personas = []

lista_personas.append(p)
lista_personas.append(p2)

for perso in lista_personas:
    print perso.get_apellidos()
    
print separador