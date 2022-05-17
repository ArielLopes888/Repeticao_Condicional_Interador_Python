"""ARIEL LISBOA LOPES - ANÁLISE E DESENVOLVIMENTO DE SISTEMAS"""
contador = 0                         # variáveis
somaidadehomem = 0
somaidademulher = 0
totalhomem = 0
totalmulher = 0
idade18a35 = 0
totalalturamulher = 0
totalalturahomem = 0

while contador < 20:                    # loop para receber valores
    print(f'Cadastro n°{contador + 1}/20') # número do cadastro atual
    cadastro = input('Escolha uma opção (0 - Homem / 1 - Mulher ): ')  # entrada que determina qual bloco será executado
    cadastro = int(cadastro)
    if cadastro == 0:    # condicional if para cadastro de homem
        idadehomem = input('Informe a idade: ')
        idadehomem = int(idadehomem)
        if 18 <= idadehomem <= 35:   # condicional para incrementar a variável idade18a35
            idade18a35 += 1

        alturahomem = input('Informe a altura (Exemplo: 1.80): ')
        alturahomem = float(alturahomem)
        somaidadehomem += idadehomem         # soma
        totalalturahomem += alturahomem      # soma
        totalhomem += 1  # incrementando
        contador += 1    # incrementando

    elif cadastro == 1:   # condicional if para cadastro de mulher
        idademulher = input('Informe a idade: ')
        idademulher = int(idademulher)
        if 18 <= idademulher <= 35:  # condicional para incrementar a variável idade18a35
            idade18a35 += 1

        alturamulher = input("Informe a altura (Exemplo: 1.80): ")
        alturamulher = float(alturamulher)
        somaidademulher += idademulher
        totalalturamulher += alturamulher
        totalmulher += 1
        contador += 1

    else:  # condicional para caso digite opção inválida
        print("Escolha 0 ou 1")
        print('')

mediaidade = (somaidadehomem + somaidademulher) / 20   # calculo media
mediaalturamulheres = totalalturamulher / totalmulher   # calculo media
mediaidadehomens = somaidadehomem / totalhomem      # calculo media
percentual18_35 = idade18a35 / contador * 100        # calculo porcentagem

print(f'"A média da idade do grupo coletado é: {mediaidade}"')     # mostrar resultados
print(f'"A média da altura das mulheres é: {mediaalturamulheres}"')
print(f'"A média da idade dos homens é: {mediaidadehomens}"')
print(f'"{percentual18_35} % tem idade entre 18 e 35 anos"')
