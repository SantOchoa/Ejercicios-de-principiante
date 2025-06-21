#Un archivo .py no es una clase, estas se deben crear en el mismo 

class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca 
        self.modelo = modelo    
        self.color = color 

    def show(self)->str:
        return (f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}")

