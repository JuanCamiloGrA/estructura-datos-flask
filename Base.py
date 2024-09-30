class Base:
    def __init__(self):
        self.items = []

    def crear(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def imprimir(self):
        return self.items
