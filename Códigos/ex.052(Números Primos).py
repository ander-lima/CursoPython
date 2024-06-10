##########################################
print ("•×"*19)
print ("\033[1;34m      Aula 13 - Repetição com FOR \033[m")
print ("\033[0;32m      Desafio 052: Números Primos  \033[m")    
print ("•×"*19)
print("")
##########################################
'''Desafio: Leia um número e verifique se ele é primo (só pode ser dividido 2 vezes) e informe quais são.

Versão: Ander (Não consegui)'''

'''cont = 0
num = int(input("Insira um número: "))
for c in range (1, 11):
	if c%num==0 or num%c==0: #verifica se é divisivel
		cont += 1
		print(f" por {c} é divisivel")
if cont <= 2:
	print (f"{num} é primo")
else:
	print (f"{num} não é primo")'''


#Versão: Guanabara
num = int(input("Insira um número: "))
tot = 0
for c in range (1, num + 1):
	if num % c == 0:
		print ("\033[32m", end = " ")
		tot += 1
	else:
		print ("\033[31m", end = " ")
	print(f"{c}", end = " ")
print (f"\n\033[m O número {num} foi divisivel {tot} vezes.")
if tot == 2:
	print ("  Por isso ele é Primo")
else:
	print ("  Por isso ele não é Primo")