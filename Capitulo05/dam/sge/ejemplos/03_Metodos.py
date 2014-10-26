# -*- coding: utf-8 -*- 
'''
Created on 19/10/2014

@author: Luismi
'''
class Antena(): 
    color = "" 
    longitud = "" 
 
class Pelo(): 
    color = "" 
    textura = "" 
 
class Ojo(): 
    forma = "" 
    color = "" 
    tamanio = ""

class Objeto(): 
    color = "verde" 
    tamanio = "grande" 
    aspecto = "feo" 
    antenas = Antena() 
    ojos = Ojo() 
    pelos = Pelo() 
 
    def flotar(self): 
        pass

