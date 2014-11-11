# -*- coding: utf-8 -*- 
'''
Created on 9/11/2014

@author: Luismi
'''

class Contacto():
    
    def __init__(self, nombre, numero=''):
        self.__nombre = nombre
        self.__numero = numero
        

    def get_nombre(self):
        return self.__nombre
    
    def get_numero(self):
        return self.__numero
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def set_numero(self, numero):
        self.__numero = numero
        
    def __srt__(self):
        return '['+self.__nombre+', '+str(self.__numero)+']'
    


class Agenda():
    
    def __init__(self):
        self.__contactos = {}
        
    def insertar_contacto(self, contacto):
        if (not self.__contactos.has_key(contacto.get_nombre())):
            self.__contactos.setdefault(contacto.get_nombre(), contacto.get_numero())
        else:
            print "Ya existe un contacto con ese nombre"
            
    def borrar_contacto(self, contacto):
        if (self.__contactos.has_key(contacto.get_nombre())):
            del self.__contactos[contacto.get_nombre()]
    
    def listar_contactos(self):
        for key, value in self.__contactos.items():
            print key, value
            
 
 
def menu():
    print "\n-- Samsung Galaxy S534 Menu\n"
    print "1. Insertar un nuevo contacto\n"
    print "2. Borrar un contacto\n"
    print "3. Listar todos los contactos\n"
    print "4. Salir\n"


if __name__ == '__main__':
    
    a = Agenda()
    menu()
    opcion = int(raw_input("Introduzca una opción"))
    while(opcion != 4):
        if(opcion == 1):
           nombre = raw_input("Introduzca el nombre del contacto: ")
           numero = raw_input("Introduzca el numero del contacto: ")
           a.insertar_contacto(Contacto(nombre, numero))
        elif(opcion == 2):
           nombre = raw_input("Introduzca el nombre del contacto: ")
           opcion2 = raw_input("¿Seguro que quiere eliminarlo? (S/N)")
           if (opcion2 == 'S'):
               a.borrar_contacto(Contacto(nombre))
           else: 
               print "El contacto no ha sido borrado"
        elif (opcion == 3):
            a.listar_contactos()
            
        menu()
        opcion = int(raw_input("Introduzca una opción"))

    
        