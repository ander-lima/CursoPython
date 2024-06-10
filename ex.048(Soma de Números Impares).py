##########################################
print ("•×"*19)
print ("\033[1;34m      Aula 13 - Repetição com FOR \033[m")
print ("\033[0;32m      Desafio 048: Soma de Números \033[m")    
print ("•×"*19)
print("")
##########################################

#Desafio: Calcule soma entre números impares, multiplos de três no intervalo de 1 até 500
#Versão: Ander

soma = 0
for c in range (3,501, 3):
	soma += c
print (f"A somatória de valores impares de 1 até 500 é de: {soma}")
	