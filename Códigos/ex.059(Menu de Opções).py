##########################################
print ("•×"*19)
print ("\033[1;34m      Aula 13 - Repetição com FOR \033[m")
print ("\033[0;32m   Desafio 059: Menu de Opções  \033[m")    
print ("•×"*19)
print("")
##########################################
'''Desafio: Faça um programa que armazene 2 valores e de 5 opções ao usuario: somar, multiplicar, maior, novos números, sair do programa'''

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
        print(' \n Opção inválida! Tente novamente. \n')
        