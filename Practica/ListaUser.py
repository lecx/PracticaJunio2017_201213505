import xml.dom.minidom

from os import system
from Practica.User import user
from Practica.Pila import pila

class ListaUsuario:

    def __init__(self):
        self.inicio = None
        self.fin = None
        self.usuarioLogueado = None
        self.isLogueado = False

    def validaVacia(self):
        if self.inicio == None:
            return True
        else:
            return False

    def agregarInicio(self,usuario,clave):
        if self.validaVacia():
            self.inicio = self.fin = user(usuario,clave)
        else:
            temp = user(usuario,clave)
            temp.siguiente = self.inicio
            self.inicio.anterior = temp
            self.inicio = temp
        self.__enlazaNodos()

    def agregarFin(self,usuario,clave):
        if self.validaVacia():
            self.inicio = self.fin = user(usuario,clave)
        else:
            temp = self.fin
            self.fin = temp.siguiente = user(usuario,clave)
            self.fin.anterior = temp
        self.__enlazaNodos()

    def __enlazaNodos(self):

        self.inicio.anterior = self.fin
        self.fin.siguiente = self.inicio

    def recorreInicioFin(self):
        temp = self.inicio
        while temp:
            print(temp.usuario)
            print(temp.clave)
            temp = temp.siguiente
            if temp == self.inicio:
                break

    def mostrarUsuariosIniFin(self):
        temp = self.inicio
        listaUsuarios = None
        while temp:
            if listaUsuarios ==None:
                listaUsuarios = temp.usuario
            else:
                listaUsuarios = listaUsuarios +" -> " + temp.usuario
            temp = temp.siguiente
            if temp == self.inicio:
                if listaUsuarios == None:
                    listaUsuarios = temp.usuario
                else:
                    listaUsuarios = listaUsuarios + " -> " + temp.usuario
                break
        if listaUsuarios == None:
            return "No hay usuarios."
        else:
            return listaUsuarios

    def recorreFinInicio(self):
        temp = self.fin
        while temp:
            print(temp.usuario)
            print(temp.clave)
            temp = temp.anterior
            if temp == self.fin:
                break

    def mostrarUsuariosFinIni(self):
        temp = self.fin
        listaUsuarios = None
        while temp:
            if listaUsuarios ==None:
                listaUsuarios = temp.usuario
            else:
                listaUsuarios = listaUsuarios +" -> " + temp.usuario
            temp = temp.anterior
            if temp == self.fin:
                if listaUsuarios == None:
                    listaUsuarios = temp.usuario
                else:
                    listaUsuarios = listaUsuarios + " -> " + temp.usuario
                break
        if listaUsuarios == None:
            return "No hay usuarios."
        else:
            return listaUsuarios

    def buscar(self,usuario):
        temp = self.inicio
        while temp:
            if temp.usuario == usuario:
                return True
            else:
                temp = temp.siguiente
                if temp == self.inicio:
                    return False

    def validaLogueo(self, usuario, clave):
        temp = self.inicio
        while temp:
            if temp.usuario == usuario:
                if temp.clave == clave:
                    self.usuarioLogueado = usuario
                    self.isLogueado = True
                    return True
                else:
                    return False
            else:
                temp = temp.siguiente
                if temp == self.inicio:
                    return False

    def parsearArchivo(self,coleccion,usuarioLogueado):
        #print("logueado: " + usuarioLogueado)

        matriz = coleccion.getElementsByTagName("matriz")
        for mat in matriz:
            valorX = mat.getElementsByTagName('x')[0]
            x = int(valorX.childNodes[0].data)
            valorY = mat.getElementsByTagName('y')[0]
            y = int(valorY.childNodes[0].data)

        #print("valor x: "+ str (x) + " valor y: " + str (y))
        operaciones = coleccion.getElementsByTagName("operaciones")

        temp = self.inicio
        while temp:
            if temp.usuario == usuarioLogueado:
                if not temp.matriz :
                    temp.matriz = [[0] * y for i in range (x)]
                    temp.matrizTranspuesta = [[0] * x for i in range (y)]
                else:
                    print("Matriz ya esta definida.")

                for operacion in operaciones:
                    opeTemp = operacion.getElementsByTagName('operacion')
                    for opeTemp2 in opeTemp:
                        ope = opeTemp2.childNodes[0].data
                        # print("operacion: "+ ope)
                        if ope != None:
                            temp.listaOpera.push(ope)

                temp.cargaArchivo = True
                return "Carga exitosa."
            else:
                temp = temp.siguiente
                if temp == self.inicio:
                    return "Usuario no existe para asocias."

    def mostrarCola(self,usuarioLogueado):
        temp = self.inicio
        while temp:
            if temp.usuario == usuarioLogueado:
                pilaTemp = pila()
                if temp.listaOpera.es_vacia() == True:
                    print("la pila esta vacia.")
                else:
                    i =0
                    while temp.listaOpera.es_vacia() == False:
                        valor = temp.listaOpera.pop()
                        print("indice "+str(i) +": " + valor)
                        pilaTemp.push(valor)
                        i = i + 1

                    while pilaTemp.es_vacia() == False:
                        valor2 = pilaTemp.pop()
                        temp.listaOpera.push(valor2)
                break
            else:
                temp = temp.siguiente
                if temp == self.inicio:
                    return "No hay usuario logueado."
                    break

    def operarQueue(self,usuarioLogueado):
        tempPila = pila()
        temp = self.inicio
        while temp:
            if temp.usuario == usuarioLogueado:
                operacionQueue = temp.listaOpera.pop()
                #print("operacion base: "+operacionQueue)
                if operacionQueue != None and operacionQueue != "":
                    valorPila = ""
                    for x in operacionQueue:
                        #print("caracter: " + x)
                        tipo = self.validaCaracter(x)
                        if tipo == "int":
                            valorPila = valorPila +""+ x
                        elif tipo == "space":
                            #print("almacena valor de pila: " +valorPila)
                            if valorPila != "":
                                tempPila.push(valorPila)
                                valorPila = ""
                        elif tipo == "ope":
                            tempPila.push(x)

                            tipoOperacion = tempPila.pop()
                            #print("ope: " + tipoOperacion)
                            valor2 = tempPila.pop()
                            #print("val2: " + valor2)
                            valor1 = tempPila.pop()
                            #print("val1: " + valor1)

                            resultado = self.realizarOperacion(valor1,valor2,tipoOperacion)
                            tempPila.push(str(resultado))
                        elif tipo == "stc":
                            print("la operacion contiene caracteres, no se pudo operar.")
                            break
                    print("resultado: " + tempPila.pop())
                    break

            else:
                temp = temp.siguiente
                if temp == self.inicio:
                    return "No hay usuario logueado."
                    break

    def validaCaracter(self,caracter):
        if caracter.isalpha():
            return "str"
        elif caracter.isdigit():
            return "int"
        elif (caracter == "+") or (caracter == "-") or (caracter == "*"):
            return "ope"
        elif caracter.isspace():
            return "space"
        else:
            return ""

    def realizarOperacion(self,valor1,valor2,tipoOperacion):
        if tipoOperacion == "+":
            val1 = int(valor1)
            val2 = int(valor2)
            resultado = val1 + val2
            print(str(valor1) + "+" + str(valor2) + "=" + str(resultado))
            return resultado
        elif tipoOperacion == "-":
            val1 = int(valor1)
            val2 = int(valor2)
            resultado = val1 - val2
            print(str(valor1) + "-" + str(valor2) + "=" + str(resultado))
            return resultado
        elif tipoOperacion == "*":
            val1 = int(valor1)
            val2 = int(valor2)
            resultado = val1 * val2
            print(str(valor1) + "*" + str(valor2) + "=" + str(resultado))
            return resultado
        else:
            print("operacion no encontrada: " + tipoOperacion)
            return ""

    def llenarMatriz(self,usuarioLogueado):
        temp = self.inicio
        while temp:
            if temp.usuario == usuarioLogueado:
                for x in range(len(temp.matriz)):
                    for y in range(len(temp.matriz[0])):
                        valor = input("ingrese valor posicion [" +str(x)+"][" + str(y)+ "]: ")
                        while valor!="":
                            if valor.isdigit():
                                temp.matriz[x][y] = valor
                                break
                            else:
                                valor = input("invalido, ingrese valor posicion [" + str(x) + "][" + str(y) + "]: ")
                temp.matrizLlena = True
                break
            else:
                temp = temp.siguiente
                if temp == self.inicio:
                    return "No hay usuario logueado."
                    break

    def operarMatrizTranspuesta(self,usuarioLogueado):
        temp = self.inicio
        while temp:
            if temp.usuario == usuarioLogueado:
                if temp.matrizLlena:
                    for i in range(len(temp.matriz)):
                        for j in range(len(temp.matriz[0])):
                            temp.matrizTranspuesta[j][i] = temp.matriz[i][j]
                    temp.matrizTransOperada = True
                else:
                    print("llene la matriz antes de operar.")
                break
            else:
                temp = temp.siguiente
                if temp == self.inicio:
                    return "No hay usuario logueado."
                    break

    def mostrarMatrizOriginal(self,usuarioLogueado):
        temp = self.inicio
        while temp:
            if temp.usuario == usuarioLogueado:
                if temp.matrizLlena:
                    for x in range(len(temp.matriz)):
                        valor ="|"
                        for y in range(len(temp.matriz[0])):
                            valor =valor +" "+ temp.matriz[x][y]
                        print(valor+"|")
                    break
                else:
                    print("debe llenar la matriz.")
                break
            else:
                temp = temp.siguiente
                if temp == self.inicio:
                    return "No hay usuario logueado."
                    break

    def mostrarMatrizTranspuesta(self, usuarioLogueado):
        temp = self.inicio
        while temp:
            if temp.usuario == usuarioLogueado:
                if temp.matrizTransOperada:
                    for x in range(len(temp.matrizTranspuesta)):
                        valor = "|"
                        for y in range(len(temp.matrizTranspuesta[0])):
                            valor = valor + " " + temp.matrizTranspuesta[x][y]
                        print(valor + "|")
                    break
                else:
                    print("debe operar la matriz transpuesta.")
                break
            else:
                temp = temp.siguiente
                if temp == self.inicio:
                    return "No hay usuario logueado."
                    break

    def validaArchivoCargado(self,usuarioLogueado):
        temp = self.inicio
        while temp:
            if temp.usuario == usuarioLogueado:
                if temp.cargaArchivo:
                    return True
                else:
                    return False
            else:
                temp = temp.siguiente
                if temp == self.inicio:
                    return False
