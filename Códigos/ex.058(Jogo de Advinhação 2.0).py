##########################################
print ("•×"*19)
print ("\033[1;34m      Aula 13 - Repetição com FOR \033[m")
print ("\033[0;32m   Desafio 058: Jogo de Advinhação 2.0  \033[m")    
print ("•×"*19)
print("")
##########################################
'''Desafio: Faça um programa que pense em um número de 0 a 10 e permita o usuario chutar até acertar'''

#1 Pensa em um número e armazena em variavel
#1.1 Armazena em variavel numero aleatório
#2 Pede um chute do usuario e confirma se é o correto
#2.1 Enquanto número for diferente do pensado: 
#3 Se não for o correto, diz se é maior ou menor
#3.1 Se for maior printa X, se for menor printa Y

import random
tent = 0
print("Olá sou o Computador do Ander, vamos jogar!")
print ('')
comp = random.randint(0, 10)
print('Acabei de pensar em um número de 0 a 10, em quantas tentativas você consegue acertar ?')
print('')
user = int(input('Faça seu palpite: '))
tent += 1
print('')
if user > 10 or user < 0:
    print('')
    print('Ei esse número não vale!')
else:
    while user != comp:
        if user > comp:
            print('É menor... tente novamente.')
            user = int(input('Qual seu palpite ?: '))
            print('')
            tent += 1
        else:
            print('É maior... tente novamente.')
            user = int(input('Qual seu palpite ?: '))
            print('')
            tent += 1
print('\033[0;32m Você acertou! \033[m Conseguiu com {} tentativas dessa vez.'.format(tent))
print('')