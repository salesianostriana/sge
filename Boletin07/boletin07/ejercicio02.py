# -*- coding: utf-8 -*- 
'''
Created on 7/11/2014

@author: Luismi


Crear un m�dulo para validaci�n de contrase�as. Dicho m�dulo, deber� cumplir con los siguientes criterios de aceptaci�n:

    La contrase�a debe contener un m�nimo de 8 caracteres.
    Una contrase�a debe contener letras min�sculas, may�sculas, n�meros y 
    al menos 1 car�cter no alfanum�rico.
    La contrase�a no puede contener espacios en blanco.
    Contrase�a v�lida, retorna True.
    Contrase�a no v�lida, retorna el mensaje "La contrase�a elegida no es segura".


'''

def validar_pass(passw):
    
    longitud = False
    mayus = False
    minus = False
    nums = False    
    especial = False
    espacio = False
    
    if (len(passw) >= 8):
        longitud = True
        for letra in passw:
            if (letra.isupper()):
                mayus = True
            elif (letra.islower()):
                minus = True
            elif (letra.isdigit()):
                nums = True
            elif (not letra.isalnum()):
                especial = True
            elif(not letra.isspace()):
                espacio = True
    
    if (longitud and mayus and minus and nums and especial and espacio):
        return True
    else:
        return False


if (__name__ == "__main__"):
    
    
    passw = raw_input("Introduzca una contraseña: ")

    if (validar_pass(passw)):
        print "Contraseña segura"   
    else:
        print "La contraseña elegida no es segura"
    
    
    
    
    

    
    