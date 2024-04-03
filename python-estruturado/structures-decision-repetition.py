# Qual número é maior

# Estratégia 1
a = 10
b = 20

if (a > b):
    maior = a
else:
    maior = b

print(f"O maior número é: {maior}")

# Estratégia 2
a = 10
b = 20
maior = a

if (b > maior):
    maior = b

print(f"O maior número é: {maior}")

# Par ou ímpar
numero = 46

if (numero % 2 == 0):
    situacao = "O número é par"
else:
    situacao = "O número é ímpar"

print(situacao)

# Nota estudante
nota = 8.2

if (nota >= 7):
    situacao = "Aprovado"
elif (nota >= 5 and nota < 7):
    situacao = "Em recuperação"
elif (nota < 5):
    situacao = "Reprovado"

print(situacao)

# Valor da compra
preco_unitario = 10
DESCONTO10 = 0.1
DESCONTO20 = 0.2
quantidades = eval(input("Digite a quantidade que vai comprar: "))

if (quantidades <= 10):
    valor_final = preco_unitario * quantidades
elif (quantidades <= 20):
    valor_final = preco_unitario * quantidades * (1 - DESCONTO10)
else:
    valor_final = preco_unitario * quantidades * (1 - DESCONTO20)

print(f"O valor final da compra é: {valor_final}")

# Soma número pares

# Estratégia 1
lista = [10, 2, 5, 7, 6, 3]
n = len(lista)
soma = 0

for i in range(n):
    if (lista[i] % 2 == 0):
        soma += lista[i]

print(f"O somatório dos elementos pares da lista é: {soma}")

# Estratégia 2
lista = [10, 2, 5, 7, 6, 3]
soma = 0

for num in lista:
    if (lista[i] % 2 == 0):
        soma += lista[i]

print(f"O somatório dos elementos pares da lista é: {soma}")