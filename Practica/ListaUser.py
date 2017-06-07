import xml.dom.minidom

from Practica.User import user

class ListaUsuario:

    def __init__(self):
        self.inicio = None
        self.fin = None
        self.usuarioLogueado = None
        self.isLogueado = False
        self.cargaArchivo = False


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

        listaOperaciones = []

        operaciones = coleccion.getElementsByTagName("operaciones")

        for operacion in operaciones:
            opeTemp = operacion.getElementsByTagName('operacion')
            for opeTemp2 in opeTemp:
                ope = opeTemp2.childNodes[0].data
                #print("operacion: "+ ope)
                if ope != None:
                    listaOperaciones.append(ope)

        temp = self.inicio
        while temp:
            if temp.usuario == usuarioLogueado:
                if not temp.matriz :
                    temp.matriz = [[0] * y for i in range (x)]
                else:
                    print("Matriz ya esta definida.")

                if temp.listaOpera == None:
                    temp.listaOpera = listaOperaciones
                else:
                    for ope in listaOperaciones:
                        temp.listaOpera.append(ope)

                self.cargaArchivo = True
                return "Carga exitosa."
            else:
                temp = temp.siguiente
                if temp == self.inicio:
                    return "Usuario no existe para asocias."

    def mostrarCola(self,usuarioLogueado):
        temp = self.inicio
        while temp:
            if temp.usuario == usuarioLogueado:
                i = 0
                for operacion in temp.listaOpera:
                    print("indice "+str(i) +": " + operacion)
                    i = i + 1
                break
            else:
                temp = temp.siguiente
                if temp == self.inicio:
                    return "No hay usuario logueado."
                    break