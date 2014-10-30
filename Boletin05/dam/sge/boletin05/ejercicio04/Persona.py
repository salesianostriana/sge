# -*- coding: utf-8 -*- 
'''
Created on 28/10/2014

@author: Luismi
'''

class Persona(object):
    
    def __init__(self, nombre, DNI, direccion, telefono, email=''):
        self.__nombre = nombre
        self.__dni = DNI
        self.__direccion = direccion
        self.__telefono = telefono
        self.__email = email
    
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def set_dni(self, dni):
        self.__dni = dni
    
    def set_direccion(self, direccion):
        self.__direccion = direccion
        
    def set_telefono(self, telefono):
        self.__telefono = telefono
        
    def set_email(self, email):
        self.__email = email
        
    def get_nombre(self):
        return self.__nombre
    
    def get_dni(self):
        return self.__dni
    
    def get_direccion(self):
        return self.__direccion
    
    def get_telefono(self):
        return self.__telefono
    
    def get_email(self):
        return self.__email
    
    
    def mostar(self):
        print self.__nombre, "(", self.__dni, ")", "\n", self.__direccion, "\n", 
    
    
if (__name__ == '__main__'):
    
    p = Persona("Pesky","12345678A", "Triana", "600000000", "pesky@delospeskydetriana.com")
    p2 = Persona("Luismi", "234567890A", "Mairena", "600696969", "erluismimolamazo@molamazo.com")
    
    lista = []
    
    lista.append(p)
    lista.append(p2)
    
    for perso in lista:
        perso.mostar()
    
    