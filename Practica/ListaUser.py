from Practica.User import user

class ListaUsuario:

    def __init__(self):
        self.inicio = None
        self.fin = None


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


    def recorrerLista(self):
        self.recorreInicioFin()
        self.recorreFinInicio()

    def recorreInicioFin(self):
        temp = self.inicio
        while temp:
            print(temp.usuario)
            print(temp.clave)
            temp = temp.siguiente
            if temp == self.inicio:
                break

    def recorreFinInicio(self):
        temp = self.fin
        while temp:
            print(temp.usuario)
            print(temp.clave)
            temp = temp.anterior
            if temp == self.fin:
                break

    def buscar(self,usuario):
        temp = self.inicio
        while temp:
            if temp.usuario == usuario:
                return True
            else:
                temp = temp.siguiente
                if temp == self.inicio:
                    return False
