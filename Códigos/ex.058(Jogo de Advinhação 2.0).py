##########################################
print ("•×"*19)
print ("\033[1;34m      Aula 14 - Repetição com WHILE \033[m")
print ("\033[0;32m   Desafio 058: Jogo de Advinhação v2.0  \033[m")    
print ("•×"*19)
print("")
##########################################
'''Desafio: Faça um programa que pense em um número de 0 a 10 e permita o usuario chutar até acertar'''

'''#Versão Ander
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
print('')'''



'''#Versão Guanabra
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue acertar qual foi ?')
acertou = False #Utilização de booleano é bem esperto
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite ?'))
    palpites += 1
    if jogador == computador:
        acertou = True #Muda o Booleano e quebra o Loop
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))'''