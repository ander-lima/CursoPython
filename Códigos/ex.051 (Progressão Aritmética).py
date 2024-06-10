##########################################
print ("•×"*19)
print ("\033[1;34m      Aula 13 - Repetição com FOR \033[m")
print ("\033[0;32m  Desafio 051: Progressão Aritimétrica  \033[m")    
print ("•×"*19)
print("")
##########################################
'''Desafio: Leia o Primeiro Termo e a Razão de uma PA e mostre os 10 primeiros termos
Versão: Guanabara'''

primeiro = int (input("Primeiro Termo: "))
razao = int (input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range (primeiro, decimo + razao, razao):
	print (f'{c}', end = ' > ')
print ('Acabou')
