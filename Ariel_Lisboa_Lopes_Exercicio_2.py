"""ARIEL LISBOA LOPES - ANÁLISE E DESENVOLVIMENTO DE SISTEMAS"""
qtd = 1           # variáveis
Maior_Valor = 0
Menor_Valor = 0
total = 0
while qtd <= 10:                 # loop para percorrer 10 valores e defini-los como maior ou menor + calcular o total
    valor = input("Informe um valor: ")  # entrada dos valores
    valor = int(valor)                        # convertendo o valor para inteiro

    if qtd == 1:                              # estabelecendo parâmetro para o próximo bloco
        Maior_Valor = valor
        Menor_Valor = valor
    else:
        if valor > Maior_Valor:              # definindo o maior valor
            Maior_Valor = valor

        if valor < Menor_Valor:               # definindo o menor valor
            Menor_Valor = valor
    qtd += 1                                 # incrementando o meu contador
    total += valor
Media = total / 10                           # calculando a média

print(f'"O maior valor é: {Maior_Valor}"')         # exibindo os dados solicitados
print(f'"O menor valor é: {Menor_Valor}"')
print(f'A média dos valores é {Media}')
