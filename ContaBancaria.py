class ContaBancaria:
    def __init__(self,numero, nome, tipo):
        self.numero = numero
        self.nome = nome
        self.tipo = tipo
        self.limite =0
        self.saldo = 0
        self.status = False
        self.NovoLimite=0

    def AtivarConta(self):
        if self.status:
            print(f"A conta de {self.nome} já está ativada")
        else:
            self.status=True
            print(f"A conta de {self.nome} foi ativa")

    def VerificarSaldo(self):
        if self.status:
            print(f"Saldo atual da conta {self.numero}: R${self.saldo:.2f}")
        else:
            print("A conta está desativada. Nao é possível verificar o saldo.")

    def Depositar(self, valor):
        if self.status:
            self.saldo += valor
            print(f"Deposito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("A conta tá desativada. Nao é possível depositar.")

    def Sacar(self, valor):
        if self.status:
            if valor <= (self.saldo + self.limite):
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
            else:
                print("Saldo insuficiente para realizar o saque.")

        else:
                print("A conta está desativada. Não é possível sacar.")

    def AjustaLimite(self, NovoLimite):
        if self.status:
            if NovoLimite >= 0:
                self.limite = NovoLimite
                print(f"Limite ajustado para R${self.limite:.2f}")