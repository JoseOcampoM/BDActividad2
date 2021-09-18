
from modulos.menu import mostrarMenu
from modulos.opcionMenu import *


eleccion={
    "1":adicionar_lista,
    "2":eliminar_lista,
    "3":mostrar_lista,
    "4":adicionar_empleado,
    "5":eliminar_empleado,
    "6":mostrar_empleado,
    "S":salir
}
def run():
    while True:
        mostrarMenu()
        opc=input("Digita la opción==> ")
        accion=eleccion.get(opc)
        if accion:
            accion()
        else:
            print("La opcion no es valida...")
			
			
def main():
    run()

if __name__ == '__main__':
    main()