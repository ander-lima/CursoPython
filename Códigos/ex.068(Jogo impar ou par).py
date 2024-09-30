##########################################
print ("•×"*19)
print ("\033[1;34m          Aula 15 - Break \033[m")
print ("\033[0;32m   Desafio 068: Jogo Impar ou Par   \033[m")    
print ("•×"*19)
print("")
##########################################
'''Desafio: Jogo de par ou impar só deve encerrar se jogador perder e mostrar quantidade de vitórias'''

#versão Ander
#logica: Enquanto vitória é 1 > soma numeros, se impar/se par compara resposta > se vitoria :vitoria =1
import random
continua = 1
vit = 0

while continua == 1:
    valor = int(input('Diga um valor: '))
    comp_valor = random.randint(1,10)
    print(comp_valor)
    resposta = str(input('Impar ou par [I/P]: ')).strip().upper()
    resultado = (valor + comp_valor)%2
    print (f'Eu escolhi {comp_valor} e você {valor} temos {comp_valor + valor} então:')
    if resultado == 0 and resposta == "P":
        print('Você venceu ! Vamos novamente')
        vit += 1
    elif resultado == 0 and resposta == "I":
        print ('Você errou.')
        break
    elif resultado != 0 and resposta == "P":
        print ('Você errou.')
        break
    elif resultado != 0 and resposta == "I":
        print('Você venceu ! Vamos novamente')
print('FIM')



print(4 % 2)
