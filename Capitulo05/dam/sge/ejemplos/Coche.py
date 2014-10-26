# -*- coding: utf-8 -*- 
'''
Created on 19/10/2014

@author: Luismi
'''

class Coche(object):
    '''
    classdocs
    '''
    def __init__(self, marca, modelo, motorizacion, color, numero_puertas, tipo_combustible="diesel"):
        '''
        Constructor
        '''
        # Estas propiedades las inicializamos con valores del "constructor"
        self.marca = marca
        self.modelo = modelo
        self.motorizacion = motorizacion
        self.color = color
        self.numero_puertas = numero_puertas
        self.tipo_combustible = tipo_combustible
        
        # Estas otras las inicializamos con valores literales
        self.cantidad_combustible = 10
        self.aceleracion = 0
        self.arrancado = False
        
    def desc(self):
        print self.marca, " ", self.modelo, " ", self.motorizacion 
        print "Color", self.color, ", ", self.numero_puertas, " puertas, ", self.tipo_combustible
        print "Cantidad de combustible disponible: ", self.cantidad_combustible
        print "Estado de aceleracion: ", self.aceleracion
        if (self.arrancado):
            print "El coche esta arrancado"
        else:
            print "El coche no esta arrancado"
        
    def arrancar(self):
        if (not self.arrancado):
            self.arrancado = True
        
    def acelerar(self):
        if (not self.arrancado):
            print "Debes arrancar antes de acelerar"
        else:
            if (self.cantidad_combustible <= 0):
                print "Debes pasar antes por la gasolinera!!"
                self.arrancado = False
                self.aceleracion = 0
            else:
                self.aceleracion += 1
                self.cantidad_combustible -= self.aceleracion
                if (self.cantidad_combustible < 0):
                    self.cantidad_combustible = 0
                    print "Se acabo el combustible, debes pasar por la gasolinera"
            
    def frenar(self):
        if (self.arrancado):
            if (self.aceleracion == 0):
                print "El coche esta en ralenti, no se puede frenar mas"
            else:
                self.aceleracion -= 1
                
    def apagar(self):
        if (self.arrancado):
            self.arrancado = False
            self.aceleracion = 0
    
    def repostar(self):
        print "Lleno, por favor"
        self.cantidad_combustible = 10
        
c = Coche("Mercedes Benz","Clase CLA","350 CDI","Rojo", "5", "Diesel")
c.desc()
c.arrancar()
c.acelerar()
c.acelerar()
c.acelerar()
c.desc()
c.acelerar()
c.acelerar()
c.desc()
c.repostar()
c.arrancar()
c.desc()
c.acelerar()
c.frenar()
c.apagar()
c.desc()

