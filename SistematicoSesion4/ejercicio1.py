class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular(self):
        print(f"El area del rectangulo es {self.base*self.altura}")


#Crear objeto calcular
calculo1 = Rectangulo(5, 8)
calculo1.calcular()