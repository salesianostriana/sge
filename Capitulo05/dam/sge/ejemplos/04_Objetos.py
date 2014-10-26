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
        print 12
  
et = Objeto() 
print et.color 
print et.tamanio 
print et.aspecto 
et.color = "rosa" 
print et.color  
et.flotar()
