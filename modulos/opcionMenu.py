import os, time, sys
from modulos.persona import Persona, Empleado

list_personas = []
list_empleados = []



def adicionar_lista():
    sw = 0
    while (sw == 0):
        os.system('cls')
        nombre = input("Digite el nombre de La Persona ==> ")
        direccion = input("Digite la direccion ==> ")
        telefono = input("Digite el telefono ==> ")
        cedula = input("Digite la cedula ==> ")

        perso = Persona(nombre, direccion, telefono, cedula)
        list_personas.append(perso)

        print(""" 
        
        """)
        opc = str(input("Quiere seguir ? (s/n) ==> "))
        if(opc == 's'):
            sw = 0
        else: 
            sw = 1
            

def mostrar_lista():
    


def eliminar_lista():
    



def eliminar_lista():
    

def adicionar_empleado():
    

def mostrar_empleado():
    


def eliminar_empleado():
    == ced:
            list_empleados.pop(i)


def salir():
    