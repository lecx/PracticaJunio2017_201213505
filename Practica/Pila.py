class pila:

    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.es_vacia():
            return "La pila esta vacia"
        else:
            return self.items.pop()

    def es_vacia(self):
        return self.items == []