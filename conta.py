class Conta:
    def __init__(self, numero, titular, saldo, limite):
        # O"__" antes do atributo "número" da classe "Conta" torna o atributo privado, podendo ser motificado apenas pelos métodos definidos.
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):
        print("O saldo é {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor


#criação de um novo método para sacar.
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"O {valor} passou do limite e não pode ser sacado.")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    # método que dá acesso ao objeto. Property necessita que o atributo seja privado.
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    # setter tem a funcionalidade de modificar o valor, portanto, o valor que pode ser modificado se coloca no parâmetro.
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    # método estático pois é um método diretamente ligado a classe e não ao objeto(self).
    @staticmethod
    def codigo_conta():
        return "001"

    @staticmethod
    def codigos_dos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco': '237'}
