class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Se depositaron {cantidad} unidades.")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Se retiraron {cantidad} unidades.")
        else:
            print("Fondos insuficientes.")

    def consultar_saldo(self):
        return self.__saldo


# Ejemplos  :
cuenta = CuentaBancaria(100)
print("Saldo inicial:", cuenta.consultar_saldo())

cuenta.depositar(50)
print("Saldo después del depósito:", cuenta.consultar_saldo())

cuenta.retirar(30)
print("Saldo después del retiro:", cuenta.consultar_saldo())

cuenta.retirar(200)