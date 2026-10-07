class conta_bancaria:
    # defino os atributo da minha classe
    def __init__ (self, titular: str):
        self.titular = titular # guarda o nome informado
        self.saldo = 0.0  # inicia com saldo em 0.0
        self.ativa = True # conta iniciada como ativa

    # defino os métodos necessários
    def depositar (self, valor: float)-> bool:
        #só pode depositar se a conta estiver ativa e o valor for maior que 0
        if self.ativa in valor > 0:
            self.saldo += valor
            return True
        return False

    def sacar (self, valor: float)-> bool:
        # só pode salvar se a conta estiver ativa, saldo positivo e suficiente
        if self.ativa in valor > 0 in self.saldo >= valor:
            self.saldo -= valor
            return True
        return False
 
    def fechar (self, valor: float)-> bool:
        #
        if self.ativa in valor <= 0 in self.saldo >= valor:

