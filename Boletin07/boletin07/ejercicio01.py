# -*- coding: utf-8 -*- 
'''
Created on 7/11/2014

@author: Luismi

Crear un módulo para validación de nombres de usuarios. Dicho módulo, deberá cumplir con los siguientes criterios de aceptación:

    El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12.
    El nombre de usuario debe ser alfanumérico.
    Nombre de usuario con menos de 6 caracteres, retorna el mensaje "El nombre de usuario debe contener al menos 6 caracteres".
    Nombre de usuario con más de 12 caracteres, retorna el mensaje "El nombre de usuario no puede contener más de 12 caracteres".
    Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el mensaje "El nombre de usuario puede contener solo letras y números".
    Nombre de usuario válido, retorna True.

'''

def validar_user(user):
    if (len(user) < 6):
        print "El nombre de usuario debe contener al menos 6 caracteres"
    elif (len(user) > 12):
        print "El nombre de usuario no puede contener más de 12 caracteres"
    elif (not user.isalnum()):
        print "El nombre de usuario puede contener solo letras y números" 
    else:
        return True
    
    return False

if (__name__ == "__main__"):

    user = raw_input("Introduzca un nombre de usuario: ")

    if (validar_user(user)):
        print "Nombre de usuario correcto"