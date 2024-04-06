from ContaCliente import ContaCliente
class ContaRemunerada(ContaCliente):
    def __init__(self,numero,IOF,IR,valorinvestido,taxarendimento):
        super().__init__(numeroIOFIR,valorinvestido,taxarendimento)

    def CalculoRendimento(Self): #(3)
        sef.valorinvestido += (self.valorinvestido * self.taxarendimento)
        sef.valorinvestido -= self.valorinvestido * self.IOF