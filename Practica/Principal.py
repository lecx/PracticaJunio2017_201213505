import sys
import xml.dom.minidom

from os import system

system("cls")

from Practica.ListaUser import ListaUsuario

lista = ListaUsuario()

def menuPrincipal():
    while(True):
        print("")
        print("*" * 10 + "Menu Principal"+ "*" * 5)
        print("1. Crear Usuario")
        print("2. Ingresar al Sistema")
        print("3. Salir del programa")

        opcion = input('Ingrese opcion: ')

        if opcion!=None:
            if opcion == '1':
                agregarUsuario()
            elif opcion == '2':
                if loguearUsuario():
                    menuSecundario()
            elif opcion == '3':
                limpiarLogueo()
                break;
            else:
                print("ingrese una opcion valida.")
        else:
            print("ingrese una opcion valida.")

def menuSecundario():
    while(True):
        print("")
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
                leerArchivo()
            elif opcion == '2':
                menuTercero()
            elif opcion == '3':
                print("opcion 3")
            elif opcion == '4':
                mostrarUsuarios()
            elif opcion == '5':
                mostrarCola()
            elif opcion == '6':
                limpiarLogueo()
                break
            else:
                print("ingrese una opcion valida.")
        else:
            print("ingrese una opcion valida.")

#se agrega usuario a la lista
def agregarUsuario():
    print("")
    print("*" * 10 + "Crear Usuario" + "*" * 5)

    while(True):
        usuario = input('ingrese usuario: ')

        if usuario !=None:
            if lista.buscar(usuario):
                print("Ya existe el usuario.")
                break
            else:
                clave = input('ingrese su contraseña: ')
                if clave != None and clave !="":
                    lista.agregarFin(usuario,clave)
                    print("Usuario creado con exito.")
                    break
                else:
                    print("Datos invalidos.")
                    break
        else:
            print("usuario invalido.")
    print("")

#loguear usuario
def loguearUsuario():
    print("")
    print("*" * 10 + "Ingresar Sistema" + "*" * 5)

    usuario = input("Ingrese su usuario: ")

    if usuario != None:
        clave = clave = input('ingrese su contraseña: ')
        if clave != None:
            if lista.validaLogueo(usuario,clave):
                esta_logueado = True
                usuario_logueado = usuario
                return True
            else:
                print("usuario o contraseña invalida.")
                return False
    else:
        print("usuario invalida.")
        return False

#limpia logueo
def limpiarLogueo():
    logueado= False
    usuarioLogueado =None

#leer archivo
def leerArchivo():
    print("")
    print("*" * 10 + "Lectura de Archivo" + "*" * 5)

    ruta = input("Ingrese ruta de archivo: ")
    if ruta != None:
        file = xml.dom.minidom.parse(ruta)
        if file != None:
            coleccion = file.documentElement
            resultado = lista.parsearArchivo(coleccion,lista.usuarioLogueado)
            print(resultado)
        else:
            print("archivo invalido.")
    else:
        print("ruta invalida.")

#resolver operaciones
def menuTercero():
    if lista.cargaArchivo:
        while (True):
            print("")
            print("*" * 10 + "Menu Operaciones" + "*" * 5)
            print("1. Operar Siguiente")
            print("2. Regresar")

            opcion = input('Ingrese opcion: ')

            if opcion != None:
                if opcion == '1':
                    print("opcion 1")
                elif opcion == '2':
                    break
                else:
                    print("ingrese una opcion valida.")
            else:
                print("ingrese una opcion valida.")
    else:
        print("cargue un archivo, para operar.")

#mostrar usuarios
def mostrarUsuarios():
    print(lista.mostrarUsuariosIniFin())
    print(lista.mostrarUsuariosFinIni())

#mostrar cola
def mostrarCola():
    lista.mostrarCola(lista.usuarioLogueado)

menuPrincipal()