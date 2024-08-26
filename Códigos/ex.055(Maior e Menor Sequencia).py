##########################################
print ("•×"*19)
print ("\033[1;34m      Aula 13 - Repetição com FOR \033[m")
print ("\033[0;32m    Desafio 055: Maior e Menor Sequencia  \033[m")    
print ("•×"*19)
print("")
##########################################
'''Desafio: Prorgama deve ler peso de 5 pessoas e depois dizer o maior e menor peso lido'''
#Versão Ander
'''
#1 Loop le 5 pesos armazena em lista
#2 Loop percorre lista e pega maior valor e armazena em variavel A
#3 Loop percorre lista e pega maior valor e armazena em variavel B
# Print A e B
pesos = []
maior_p = ()
menor_p = ()
aux_maior = 0
aux_menor = None

for c in range(1, 6): #1
    peso = float(input("Insira o peso da {}ª pessoa: ".format(c)))
    pesos.append (peso)

for p in pesos:#2
    if p > aux_maior:
        aux_maior = p
for p in pesos: #3
    if aux_menor is None:
        aux_menor = p
    elif p < aux_menor:
        aux_menor = p

print('O maior peso lido foi de {}Kg'.format(aux_maior)) 
print('O menor peso lido foi de {}Kg'.format(aux_menor))
'''
#Versão Guanabara
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor: 
            menor = peso

print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
