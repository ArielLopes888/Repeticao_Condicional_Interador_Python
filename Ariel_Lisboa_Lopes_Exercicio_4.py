"""ARIEL LISBOA LOPES - ANÁLISE E DESENVOLVIMENTO DE SISTEMAS"""
opcao = input(
    "1 Celsius / Fahrenheit \n"                     # input para o usuário escolher a conversão. '\n' quebra linha
    "2 Celsius / Kelvin \n"
    "3 Fahrenheit / Kelvin \n"
    "4 Fahrenheit / Celsius \n"
    "5 Kelvin / Fahrenheit \n"
    "6 Kelvin / Celsius \n"
    " \n"
    "Escolha uma opção: ")
print(" ")

if opcao == '1':                                  # if , elif, else condicionais para determinar o bloco a ser executado
    numero = float(input("Digite o valor (Exemplo: 23.5): "))
    resultado = (numero * 9/5) + 32               # cálculo de conversão
    print(f'"O resultado é {resultado}°F"')       # exibir resultados

elif opcao == '2':
    numero = float(input("Digite o valor (Exemplo: 23.5): "))
    resultado = numero + 273.15
    print(f'"O resultado é {resultado}°K')

elif opcao == '3':
    numero = float(input("Digite o valor (Exemplo: 23.5): "))
    resultado = (numero - 32) * 5/9 + 273.15
    print(f'"O resultado é {resultado}°K"')

elif opcao == '4':
    numero = float(input("Digite o valor (Exemplo: 23.5): "))
    resultado = (numero - 32) * 5/9
    print(f'"O resultado é {resultado}°C"')

elif opcao == '5':
    numero = float(input("Digite o valor (Exemplo: 23.5): "))
    resultado = (numero - 273.15) * 9/5 + 32
    print(f'"O resultado é {resultado}°F"')

elif opcao == '6':
    numero = float(input("Digite o valor (Exemplo: 23.5): "))
    resultado = (numero * 9 / 5) + 32
    print(f'"O resultado é {resultado}°C"')

else:
    print('Digite um número entre 1 e 6')        # mensagem de erro caso o usuário selecione uma opçao errada
