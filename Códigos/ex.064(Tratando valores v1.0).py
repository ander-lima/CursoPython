##########################################
print ("•×"*19)
print ("\033[1;34m      Aula 14 - Repetição com WHILE \033[m")
print ("\033[0;32m   Desafio 064: Tratando valores v1.0  \033[m")    
print ("•×"*19)
print("")
##########################################
'''Desafio: Programa deve ler numeros e enquanto não for 999 ele não encerra. Ao encerrar deve retornar a soma de todos os valores digitados desconsiderando o 999'''

'''#versão Ander
# Lógica: armazena numero digitado > enquanto não for 999 executa: > soma valor digitado no contador

cont = 0
val_dig = 0
while val_dig != 999:
    val_dig = int(input('Digite um número [999 para parar]: '))
    if val_dig != 999:
        cont += val_dig
print('A soma é de: {}'.format(cont))'''

#versão Guanabara

cont = num = soma = 0
num = int(input('Digite um número [999 para sair]: ')) #essa linha é descartavel
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para sair]: '))
print ('Você digitou {} números e a soma é de {}'.format(cont, soma))