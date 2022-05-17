"""ARIEL LISBOA LOPES - ANÁLISE E DESENVOLVIMENTO DE SISTEMAS"""

n = input("Digite um número: ")  # input para a entrada do número a ser calculado
n = int(n)                       # input retorna string, então fiz um casting str para int
contador = 0                     # contador que será incrementado em cada volta do meu loop
fatorial = 1
while contador < n:              # strutura do loop
    contador += 1
    fatorial = fatorial * contador

print(fatorial)                 # mostrar o resultado
