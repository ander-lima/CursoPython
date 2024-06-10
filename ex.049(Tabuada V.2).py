import time
##########################################
print ("•×"*19)
print ("\033[1;34m      Aula 13 - Repetição com FOR \033[m")
print ("\033[0;32m        Desafio 049: Tabuada V.2 \033[m")    
print ("•×"*19)
print("")
##########################################

# •| Desafio: Faça uma Tabuada com For


#Versão: Ander

'''tab = int(input("Insira um numero para sua Tabuada: "))

for c in range (1, 11):
	print (f'{tab} X {c} = {tab*c}')
	time.sleep(0.5)'''
	
#Versão: Guanabara

num = int(input("Digite um número para sua tabuada: "))
for c in range (1, 11):
	print('{} × {:2} = {}'.format (num, c , num*c))
	