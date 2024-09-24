##########################################
print ("•×"*19)
print ("\033[1;34m    Aula 13 - Repetição com FOR \033[m")
print ("\033[0;32m Desafio 065: Maior e menor valores  \033[m")    
print ("•×"*19)
print("")
##########################################
'''Desafio: Deve ler valores enquanto a resposta for 'S' >> Ao final deve trazer: Quantidade de números digitados, média entre os números, Maior valor, menor valor'''

#versão Ander
#Lógica: Uma variavel para cada uma das 4 situações >>> While resposta for == S >>> Uma operação para cada variavel
cont = 0
media = 0
media_f = 0
maior = 0
menor = 0
r = 's'
val = 0
while r == 's' and r != 'n':
    val = int(input('Digite um número: '))
    media += val
    if val > maior:
        maior = val
    if cont == 0:
        menor = val
    elif val < menor:
        menor = val
    cont += 1
    r = str(input('Quer continuar ? [S/N]')).lower().strip()

media_f = media/cont

print ('Você digitou {} números e a média foi {}'.format(cont, media_f))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
print('FIM')
