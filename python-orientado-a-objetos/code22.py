from ContaCliente import ContaCliente
class ContaComum(ContaCliente):
    def __init__(self,numero,IOF,IR,valorinvestido,taxarendimento):
        super().__init__(numeroIOFIR,valorinvestido,taxarendimento)

    def CalculoRendimento(Self): #(2)
        sef.valorinvestido += (self.valorinvestido * self.taxarendimento)