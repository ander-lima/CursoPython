##########################################
print ("•×"*19)
print ("\033[1;34m      Aula 13 - Repetição com FOR \033[m")
print ("\033[0;32m   Desafio 060: Cálculo de Fatorial  \033[m")    
print ("•×"*19)
print("")
##########################################
'''Desafio: Faça um programa que dado um número, calcule seu fatorial'''

'''#versão Ander: Falhei
#Fatorial é a soma da multiplicação de 1 número com 1 numero menor que o anterior multiplicado

n = int(input('Digite um número para seu fatorial: '))
fat = 1# Inicializando fat com 1, já que o fatorial de qualquer número envolve multiplicações
aux = n # Variável que usaremos para calcular o fatorial

while prox > 1:
    fat *= aux # Multiplica fat pelo valor de aux
    aux -= 1 # Diminui o valor de aux a cada passo'''

#versão Guanabara

n = int(input('Insira um número para seu fatorial: '))
c = n #Determinando contador que começa no valor máximo que é igual ao número que se deseja fatorial
f = 1 #O inicio para multiplicação/Caso nulo é = 1, assim como na soma o caso Nulo é = 0

print('Calculando {}!= '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else  ' = ', end='')
    f *= c
    c -= 1
print ('{}'.format(f))