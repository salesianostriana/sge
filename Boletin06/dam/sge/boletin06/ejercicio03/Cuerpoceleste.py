# -*- coding: utf-8 -*- 
'''
Created on 30/10/2014

@author: Luismi
'''

class CuerpoCeleste(object):
    
    def __init__(self, nombre, radio, masa, rotacion, traslacion):
        self.__nombre = nombre
        self.__radio = radio
        self.__masa = masa
        self.__rotacion = rotacion
        self.__traslacion = traslacion

    def __str__(self, *args, **kwargs):
        return object.__str__(self, *args, **kwargs)
    


class Planeta(CuerpoCeleste):
    pass

class Satelite(CuerpoCeleste):
    pass

class Estrella(CuerpoCeleste):
    pass


