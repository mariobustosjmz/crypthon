#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands


debug = False
 
# Cifrado por sustitucion CESAR OPTIMIZADO
 
def get_alfabeto():
    """Devuelve una lista con mayusculas, minuscula, numeros y un espacio"""

    alfabeto = []
 
    # mayusculas:65-90 =25
    for i in range(65,91):
        alfabeto.append(chr(i))
 
    # minusculas:97-122 =25
    for i in range(97,123):
        alfabeto.append(chr(i))
 
    # numeros =10
    for i in range(10):
        alfabeto.append(str(i))
 
    # espacio
    alfabeto.append(" ")
 
    #print len(alfabeto) = 63 elementos
    return alfabeto
     
     
 
def get_index(index = 0, largo = 0):
    """Devuelve un indice valido dentro de un rango, evitando desbordamiento"""
     
    min_index = 0               # indice minimo
    max_index = largo - 1       # indice maximo = longitud - 1
 
    while True:
         
        # index excede el limite superior
        if index > max_index:
            index -= largo
 
        # index es menor al limite inferior
        elif index < min_index:
            index += largo
             
        # index es valido
        else:
            break
 
    return index    
 
 
 
 
def crypt(mensaje = "", llave = 0):
    """Cifra un mensaje usando sustitucion"""
     
    encriptado = ""                   # mensaje cifrado
 
    alfabeto = get_alfabeto()         # todo el alfabeto
    largo = len(alfabeto)             # longitud del alfabeto
    index = 0                         # indice de la letra en el alfabeto
 
    for caracter in mensaje:
 
        # se obtiene el indice de caracter dentro de alfabeto, si existe
        try:        
            index = alfabeto.index(caracter)  # indice dentro del alfabeto
        except:
            print "No existe %s en el alfabeto creado" % (caracter,)
            continue
 
 
        # se obtiene la nueva posicion, evitando desbordamiento
        move = index + llave      # nueva posicion
        move = get_index(move,largo)   
     
        # debug
        if debug:
            print "move %d"%(move,)
 
        encriptado += alfabeto[move]   # agrega la letra al mensaje cifrado
 
        #debug
        if debug:
            print "%s = %s" % (alfabeto[index],alfabeto[move])
 
    return encriptado
 


 
def decrypt(mensaje = "", llave = 0):
    """Decifra un mensaje usando sustitucion"""
     
    desencriptado = ""          # mensaje decifrado
 
    alfabeto = get_alfabeto()   # alfabeto
    largo = len(alfabeto)      # longitud del alfabeto
    index = 0
 
    for caracter in mensaje:
 
        try:
            index = alfabeto.index(caracter)  # indice dentro del alfabeto
        except:
            print "No existe %s en el alfabeto creado" % (caracter,)
            continue       
 
        move = index - llave      # nueva posicion
        move = get_index(move,largo)
 
        # debug
        if debug:
            print "move %d"%(move,)
 
 
        desencriptado += alfabeto[move] # agrega al mensaje decifrado
         
        #debug
        if debug:
            print "%s = %s" % (alfabeto[index],alfabeto[move])
 
    return desencriptado
 
 




# inicio
print "\n"
print "===================================================================="
print "\t Cifrado por sustitucion, Algoritmo Cesar Optimizado "
print "==================================================================== \n"









