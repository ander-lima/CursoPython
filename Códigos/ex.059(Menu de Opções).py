##########################################
print ("•×"*19)
print ("\033[1;34m      Aula 14 - Repetição com WHILE \033[m")
print ("\033[0;32m   Desafio 059: Menu de Opções  \033[m")    
print ("•×"*19)
print("")
##########################################
'''Desafio: Faça um programa que armazene 2 valores e de 5 opções ao usuario: somar, multiplicar, maior, novos números, sair do programa'''

'''#versão Ander
#1 armazena 2 valores
#1.1 Criar variavel 'sair' 
#2 While sair = false: Mostra menu e Armazena resposta
#3 Compara resposta com elif's e executa determinada parte do programa
val_1 = int(input('Primeiro valor: '))
val_2 = int(input('Segundo valor: '))
sair = False
opcao = 0

while not sair:
    print('==='*10 + '\n [1] Somar \n [2] Multiplicar \n [3] Maior \n [4] Novos números \n [5] Sair do Programa')
    opcao = int(input('>>>>> Qual é a sua opção ? '))
    if opcao == 1:
        soma = val_1 + val_2
        print ('\n A soma entre {} e {} é {} \n'.format(val_1, val_2, soma))
    elif opcao == 2:
        multi = val_1 * val_2
        print('\n A multiplicação entre {} e {} é {} \n'.format(val_1, val_2, multi))
    elif opcao == 3:
        maior = val_1
        if val_2 > val_1:
            maior = val_2
        print('\n O maior número entre {} e {} é {} \n'.format(val_1, val_2, maior))
    elif opcao == 4:
        val_1 = int(input('Primeiro valor: '))
        val_2 = int(input('Segundo valor: '))
        print('\n {} e {} são os novos valores. \n'.format(val_1, val_2))
    elif opcao == 5:
        print ('5')
        print('\n Obrigado e até a próxima! \n')
        sair = True
    else:
        print(' \n Opção inválida! Tente novamente. \n')'''
        
#versão guanabara

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
maior = 0
while opcao != 5:
    print('==='*10 + '\n [1] Somar \n [2] Multiplicar \n [3] Maior \n [4] Novos números \n [5] Sair do Programa')
    opcao = int(input('>>>>>> Qual sua opção ? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        multi = n1 * n2
        print('A multiplicação entre {} e {} é {}.'.format(n1, n2, multi))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior numero entre {} e {} é {}.'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else: 
        print ('Opção invalida ! Tente novamente.')

