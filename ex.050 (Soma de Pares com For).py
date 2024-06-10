##########################################
print ("•×"*19)
print ("\033[1;34m      Aula 13 - Repetição com FOR \033[m")
print ("\033[0;32m      Desafio 050: Soma de Números \033[m")    
print ("•×"*19)
print("")
##########################################

#Desafio: Leia 6 números inteiros, separe apenas os impares e os some.
#Versão: Ander

'''num = []
soma = 0
for c in range (1,7):
	num.append(int(input("Insira um número: ")))
for i in num:
	if i %2==0:
		soma += i
	
print (f'A soma total dos valores pares entre os digitados é: {soma}')'''

#Versão: Guanabara
soma = 0
cont = 0
for c in range (1,7):
	num = int (input(f"Digite o {c}° valor: "))
	if num %2 == 0:
		soma += num
		cont += 1
print (f'Voçê informou {cont} valores pares e a soma foi {soma}!')