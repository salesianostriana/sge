# -*- coding: utf-8 -*- 
'''
Created on 7/11/2014

@author: Luismi
'''


nombre = raw_input("Introduzca el nombre del alumno votado: ")
dict = {}
while (nombre != 'FIN'):
    if (dict.has_key(nombre)):
        dict[nombre] = dict.get(nombre)+1
    else:
        dict.setdefault(nombre,1)
        
    nombre = raw_input("Introduzca el nombre del alumno votado: ")
        
max_votos = 0
mas_votado = []    
for clave, valor in dict.items():
        if (valor > max_votos):
            max_votos = valor
            mas_votado = []
            mas_votado.append(clave)
        elif (valor == max_votos):
            mas_votado.append(clave)
        print clave, str(valor) + " votos"
        
if (len(mas_votado) == 1):
    print "El mas votado ha sido ", mas_votado[0], " con ", max_votos, " votos"
else:
    print "Empate de los siguientes candidatos con ", max_votos, " votos"
    print mas_votado