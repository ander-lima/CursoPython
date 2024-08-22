##########################################
print ("•×"*19)
print ("\033[1;34m      Aula 13 - Repetição com FOR \033[m")
print ("\033[0;32m      Desafio 054: Grupo Maioridade  \033[m")    
print ("•×"*19)
print("")
##########################################
'''Desafio: Desenvolva um programa que analise 7 anos de nascimento e divida-as em grupos de maiores e menores de idade'''
#Versão Ander
'''
0- Loop para pegar anos
1- determinar variaveis maior e menos idade
2- determinar ano atual
3- loop percorre todos anos
3.1 - se data - data atual >= 18 salva em variavel maior idade
3.2 - Else, salva em menor idade 
4- print em cada'''

from datetime import date #importação

data = date.today().year
maior_i = 0
menor_i = 0

for c in range (1, 8): #loop da pergunta
    ano = int(input("Em que ano a {}ª pessoa nasceu ? ".format(c))) #Pega o ano da pessoa
    if data - ano >= 18: #Calcula idade
        maior_i = maior_i + 1
    else:
        menor_i = menor_i + 1

print ("Temos {} maiores de idade".format(maior_i)) #Print final
print ("E {} menores de idade".format(menor_i))

#Versão Guanabara

'''
from datetime import date #importação

data = date.today().year
maior_i = 0
menor_i = 0

for c in range (1, 8): #loop da pergunta
    ano = int(input("Em que ano a {}ª pessoa nasceu ? ".format(c))) #Pega o ano da pessoa
    idade = data - ano #Calcula idade
    if idade >= 18: 
        maior_i += 1
    else:
        menor_i += 1

print ("Temos {} maiores de idade".format(maior_i)) #Print final
print ("E {} menores de idade".format(menor_i))

'''