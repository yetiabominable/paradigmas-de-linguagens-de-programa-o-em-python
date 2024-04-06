class Banco():
    def __init__(self, codigo,nome):
        self.codigo = codigo
        self.nome = nome
        self.contas = []

    def adicionaconta(self,contacliente):
        self.contas.append(contacliente)

    def calcularendimentomensal(self): #(7)
        for c in self.contas:
            c.CalculoRendimento()
            
    def imprimesaldocontas(self):
        for c in self.contas:

banco1 = Banco(999,"teste")
contacliente1 = ContaCliente (1,0.01,0.1,1000,0.05)
contacomum1 = ContaComum(2,0.01,0.1,2000,0.05)
contaremunerada1 = ContaRemunerada(3,0.01,0.1,2000,0.05)

banco1.adicionaconta(contacliente1) #(4)
banco1.adicionaconta(contacomum1) #(5)
banco1.adicionaconta(contaremunerada1) #(6)
banco1.calcularendimentomensal#(7)
banco1.imprimesaldocontas() #(8)