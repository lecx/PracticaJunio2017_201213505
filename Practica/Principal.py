import sys
from os import system

system("cls")

from Practica.ListaUser import ListaUsuario

lista = ListaUsuario()

def menuPrincipal():
    while(True):
        print("*" * 10 + "Menu Principal"+ "*" * 5)
        print("1. Crear Usuario")
        print("2. Ingresar al Sistema")
        print("3. Salir del programa")

        opcion = input('Ingrese opcion: ')

        if opcion!=None:
            if opcion == '1':
                agregarUsuario()
            elif opcion == '2':
                print("opcion 2")
            elif opcion == '3':
                break;
            else:
                print("ingrese una opcion valida.")
        else:
            print("ingrese una opcion valida.")
    print("")

def menuSecundario():
    while(True):
        print("*" * 10 + "Menu Sistema" + "*" * 5)
        print("1. Leer archivo ")
        print("2. Resolver operaciones ")
        print("3. Operar la matriz ")
        print("4. Mostrar usuarios ")
        print("5. Mostrar cola ")
        print("6. Cerrar sesión ")

        opcion = input('Ingrese opcion:')

        if opcion != None:
            if opcion == '1':
                print("opcion 1")
            elif opcion == '2':
                print("opcion 2")
            elif opcion == '3':
                print("opcion 3")
            elif opcion == '4':
                print("opcion 4")
            elif opcion == '5':
                print("opcion 5")
            elif opcion == '6':
                print("opcion 6")
            else:
                print("ingrese una opcion valida.")
        else:
            print("ingrese una opcion valida.")
    print("")

#se agrega usuario a la lista
def agregarUsuario():
    print("*" * 10 + "Crear Usuario" + "*" * 5)

    while(True):
        usuario = input('ingrese usuario: ')

        if usuario !=None:
            if lista.buscar(usuario):
                print("Ya existe el usuario.")
                break;
            else:
                clave = input('ingrese su contraseña: ')
                if clave != None:
                    lista.agregarInicio(usuario,clave)
                    print("Usuario creado con exito.")
                    break;
                else:
                    print("Datos invalidos.")
        else:
            print("usuario invalido.")
    print("")

menuPrincipal()