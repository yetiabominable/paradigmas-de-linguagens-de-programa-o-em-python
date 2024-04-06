class Cliente:
    def __init__(self,cpf,nome,endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco

class Conta:
   def __init__(self, clientes, numero, saldo):
      self.clientes = clientes
      self.numero = numero
      self.saldo = saldo
   def depositar(self, valor):
      self.saldo += valor
   def sacar(self,valor):
      if self.saldo < valor:
         return False
      else:
         self.saldo -= valor
         return True
   def transfereValor(self,contaDestino,valor):
      if self.saldo < valor:
         return ("Não existe saldo suficiente")
      else:
         contaDestino.depositar(valor)
         self.saldo -= valor
         return("Transferencia Realizada")
   def gerarsaldo(self):
      print(f"numero:{self.numero} \n saldo: {self.saldo}")

class Extrato:
    def __init_(self):
        self.transacoes = []
    def extrato(self, numeroconta):
        print(f"Extrato: {numeroconta} \n")
        for p in self.transacoes:
            print(f"{p[0]:15s} {p[1]:10.2f} {p[2]:10s} {p[3].strftime('%d/%b/%y')}")