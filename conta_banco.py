class Conta:
    def __init__(self, titular, saldo, numero, limite):
        print("criando conta...")
        self.__numero = numero
        self.__limite = limite
        self.__saldo = saldo
        self.__titular = titular

    def extrato(self):
        print("saldo: {} do titular: {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.saldo + self.limite
        return valor_a_sacar <= valor_disponivel

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, receptor):
        self.saca(valor)
        receptor.deposita(valor)
        print("O valor de {} foi depositado na conta de {} por {}".format(valor, receptor.__titular, self.__titular))

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"


# exemplo abaixo:
conta1 = Conta("Yoshikage", 25, 1819, 1000)
conta2 = Conta("Joseph", 75, 2321, 1000)

conta1.extrato()
conta2.extrato()

conta2.transfere(20, conta1)
conta1.transfere(5, conta2)

conta1.extrato()
conta2.extrato()

print(conta1.codigo_banco())
