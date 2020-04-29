# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 19:05:39 2020

@author: floza
"""

#practica1
#print ("Bienvenido a emparejando.com")
#print("=======================================")
#print("Necesitamos conocer algunos datos sobre ti para encontrar tu pareja ideal")
#
#nombre = input("Nombre: ")
#fecha = int(input("¿Año de nacimiento? "))
#pregunta = input("¿Te gusta Taburete?")
#
#edad = 2020-fecha
#
#print("Hola "+nombre+". Si no me equivoco tienes", edad,"años.")
#
#if pregunta in ('Si','si'):
#    print("OK boomer. Lo tuyo va a ser un caso difícil")
#else:
#    print("Bueno, al menos es un comienzo. Veremos qué se puede hacer contigo.")

#practica2
#num=1
#
#while (num<edad):
#    print("Que no cumple",num)
#    num+=1
#
#print("¡ Que sí cumple",num,"!") 

#practica3
#num=1
#for num in range(17):
#    print("Que no cumpla",num)
#    print("¡Que si cumpla",num,"!") 


#practica4
#datos=[nombre,edad,pregunta]
#
#for lista in datos:
#    print(lista)

#practica5
#datos={
#      "nombre":nombre,
#      "edad":edad,
#      "pregunta":pregunta
#      }
#
#for tabla in datos.values():
#    print(tabla)

#practica6

# Declaración de constantes necesarias para todo el programa
abecedario= ' abcdefghijklmnñopqrstuvwxyz '

print("Bienvenidos a mi cifrador César")

texto_claro=input("Introduce una frase para cifrarla: ")
clave=int(input("Introduce un numero para cifrar(Un número del 1 al 27):"))

texto_cifrado=""


for letra in texto_claro:
    nueva_posicion=abecedario.find(letra)+ clave
    letra_cifrada=int(nueva_posicion)%len(abecedario)
    texto_cifrado= texto_cifrado+str(abecedario[letra_cifrada])
print ("El mensaje cifrado es:" ,texto_cifrado)
print ("=====================================================")


#practica7
texto_descifrado=""
for letra in texto_cifrado:
    nueva_posicion= abecedario.find(letra)-clave
    letra_cifrada= int(nueva_posicion)%len(abecedario)
    texto_descifrado= texto_descifrado+str(abecedario[letra_cifrada])
print ("El mensaje descifrado es: " ,texto_descifrado)