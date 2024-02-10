import math

class FiguGeo:
    def calcu_area(self):
        return

class Triangulo(FiguGeo):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcu_area(self):
        return 0.5 * self.base * self.altura

class Cuadrado(FiguGeo):
    def __init__(self, lado):
        self.lado = lado

    def calcu_area(self):
        return self.lado * self.lado

class Circulo(FiguGeo):
    def __init__(self, radio):
        self.radio = radio

    def calcu_area(self):
        return math.pi * self.radio**2

# Ejemplo de uso:
triangulo = Triangulo(9, 18)
print("Área del triángulo:", triangulo.calcu_area())

cuadrado = Cuadrado(10)
print("Área del cuadrado:", cuadrado.calcu_area())

circulo = Circulo(4)
print("Área del círculo:", circulo.calcu_area())