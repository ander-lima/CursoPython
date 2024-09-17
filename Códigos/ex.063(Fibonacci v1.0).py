##########################################
print ("•×"*19)
print ("\033[1;34m      Aula 13 - Repetição com FOR \033[m")
print ("\033[0;32m   Desafio 063: Fibonacci v1.0  \033[m")    
print ("•×"*19)
print("")
##########################################
'''Desafio: Faça um programa que pergunte quantos termos deseja e realize a sequencia de fibonacci até ele'''
#Lógica Fibonacci: Primeiro termo é 0 e o segundo e terceiro são 1 > Prox = ultimo + penulmo
#Lógica: Pergunta termo e armazena em variavel > enquanto contador for menor que termo > print fibo

#versão Ander
ciclos = int(input('Quantos termos você deseja mostrar ? '))
count = 0
fibo = 0
prox = 1

print('~~'*10)
while ciclos > count:
    print(fibo,' > ', end='')
    temp = fibo
    fibo = prox
    prox += temp
    count +=1
print ('FIM')
print('')
print('~~'*10)