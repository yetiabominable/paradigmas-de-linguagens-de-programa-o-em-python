from ContasClientesExtrato import Conta
from ContaPoupanca import Poupanca

class ContaRemuneradaPoupanca(Conta, Poupanca):
    def __init__(self, taxaremuneracao, clientes, numero, saldo, taxaremuneracao):
        Conta.__init__(self,clientes,numero,saldo)
        Poupanca.__init__(self,taxaremuneracao)
        self.taxaremuneracao = taxaremuneracao
        
    def remuneraConta(Self):
        self.saldo += self.saldo * (self.taxaremuneracao/30)
        self.saldo -= self.taxaremuneracao