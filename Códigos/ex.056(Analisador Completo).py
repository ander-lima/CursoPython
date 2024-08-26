##########################################
print ("•×"*19)
print ("\033[1;34m      Aula 13 - Repetição com FOR \033[m")
print ("\033[0;32m    Desafio 056: Analisador Completo  \033[m")    
print ("•×"*19)
print("")
##########################################
'''Desafio: Prorgama deve ler dados 4 pessoas (nome, idade e sexo) e apos isso puxar 3 informações: Idade média do grupo, Quem é o homem mais velho e quantas mulheres com - de 20 anos'''

'''#Versão Ander: Não tive capacidade de desenvolver
# 1 Criar 1 variavel para cada pessoa (array)
# 2 loop pede e armazena informações em cada variavel
# 3 Idade média: Comparar idades
# 4 Homem mais velho:
# 4.1 Verificar se tem homem
# 4.2 Comparar idades e achar o mais velho entre eles
# 5 Mulheres <20: Verificar'''

#Versão Guanabara

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
# Determina variaveis que serão puxadas no print. O código manipula elas para que não se precise de um banco de dados para consulta das Pessoas

for p in range(1,5): # Loop 
    print('--- {}ª PESSOA ---'.format(p))
# Determina variaveis e guarda as
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    somaidade += idade # Começa a somar as idades

    if p == 1 and sexo in 'Mm': # O 1º Homem recebe o titulo de mais velho
        # Obs: o 'In' determina valores dentre os digitados
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem: # Comparada quem tem mais idade entre homens
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'Ff' and idade < 20: # Verificador de quantidade de mulheres
        totmulher20 += 1

mediaidade = somaidade / 4 # Divide as idades somadas para média

print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))