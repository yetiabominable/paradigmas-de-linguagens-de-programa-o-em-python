# Escopo global
x = 10
x

# Escopo local
def multiplicador(numero):
        a = 2 # esta variável tem escopo local
        print(f"Dentro da função, a variável vale: {a}")
        return a * numero

a = 3 # esta variável tem escopo global
b = multiplicador(5)
print(f"Fora da função, a variável a vale: {a}")

def multiplicador(numero):
        return a * numero

a = 3 # esta variável tem escopo global
b = multiplicador(5)
print(f"A variável b vale: {b}")

# Alteração da visibilidade
def multiplicador(numero):
        global a # todas as referências à variável a são para a global
        a = 2      # a global será alterado
        print(f"Dentro da função,  variável  vale: {a}")
        return a * numero


a = 3  # esta variável tem escopo global
b = multiplicador(5)
print(f"A variável b vale: {b}")
print(f"Fora da função, a variável a vale: {a}")