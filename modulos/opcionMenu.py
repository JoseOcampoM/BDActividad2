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
    os.system('cls')
    for i in range(len(list_personas)):
            print(f"{list_personas[i].nombre} - {list_personas[i].direccion} - {list_personas[i].telefono} - {list_personas[i].cedula}")
    
    key = input("digite una tecla para continuar....")


def eliminar_lista():
    os.system('cls')
    print("Elimina de la lista...")
    key=input("digite una tecla para continuar....")



def eliminar_lista():
    os.system('cls')
    ced = input("Digite la cedula de la persona ==> ") 

    for i in range(len(list_personas)):
        if list_personas[i].cedula == ced:
            list_personas.pop(i)
    

def adicionar_empleado():
    

def mostrar_empleado():
    


def eliminar_empleado():
    == ced:
            list_empleados.pop(i)


def salir():
    