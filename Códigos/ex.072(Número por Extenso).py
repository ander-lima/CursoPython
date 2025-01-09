##########################################
print ("•×"*19)
print ("\033[1;34m          Aula 16 - Tuplas \033[m")
print ("\033[0;32m   Desafio 072: Número por Extenso  \033[m")    
print ("•×"*19)
print("")
##########################################
'''Desafio: Programa deve armazenar em uma tupla numeros por extenso e a partir dela pedir um numero do usuario e imprimir por extenso'''

#versão Ander
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

escolha = int(input('Digite um número entre 0 e 20: '))

while escolha < 0 or escolha > 20:
    escolha = int(input('Tente Novamente. Digite um número entre 0 e 20: '))

print(F'Você digitou o número {numeros[escolha]}')
