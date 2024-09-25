##########################################
print ("•×"*19)
print ("\033[1;34m      Aula 14 - Repetição com WHILE \033[m")
print ("\033[0;32m   Desafio 065: Maior e Menor  \033[m")    
print ("•×"*19)
print("")
##########################################
'''Desafio: Deve ler valores enquanto a resposta for 'S' >> Ao final deve trazer: Quantidade de números digitados, média entre os números, Maior valor, menor valor'''

'''#versão Ander
#Lógica: Uma variavel para cada uma das 4 situações >>> While resposta for == S >>> Uma operação para cada variavel
cont = 0
media = 0
media_f = 0
maior = 0
menor = 0
r = 's'
#"val = 0" eu não precisava criar a variavel aqui pois ela é criada dentro do primeiro While na linha 20
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
    r = str(input('Quer continuar ? [S/N]')).lower().strip() #há um BUG aqui, afinal se eu colocar SS ele rejeita e considera como N

media_f = media/cont

print ('Você digitou {} números e a média foi {:.2f}'.format(cont, media_f))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
print('FIM')'''


#versão Guanabara
resp = 'S'
soma = quant = media = maior = menor = 0
while resp == 'S':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar [S/N] ')).upper().strip()[0] #O [0] faz considerar apenas a primeira letra
media = soma /quant
print ('Você digitou {} números e a média foi {:.2f}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))