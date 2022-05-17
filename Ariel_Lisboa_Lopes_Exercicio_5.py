"""ARIEL LISBOA LOPES - ANÁLISE E DESENVOLVIMENTO DE SISTEMAS"""

print("CÁLCULO VALOR FUTURO")
print(" ")

valor = int(input("Qual valor será aplicado? Digite aqui sua resposta: "))  # inputs para receber s valores
porcentagem = int(input("Agora digite aqui a porcentagem dos juros: "))
meses = int(input("Quantos meses: "))

juros = porcentagem / 100   # calculo valor futuro
vx = (1 + juros) ** meses
valorfuturo = valor * vx

print(f' "O valor futuro é: {valorfuturo}"')
