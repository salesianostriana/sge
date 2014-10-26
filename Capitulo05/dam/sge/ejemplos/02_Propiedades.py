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
 
class Objeto(object): 
    color = "" 
    tamanio = "" 
    aspecto = "" 
    antenas = Antena() # propiedad compuesta por el objeto objeto Antena
    ojos = Ojo()       # propiedad compuesta por el objeto objeto Ojo
    pelos = Pelo()     # propiedad compuesta por el objeto objeto Pelo

