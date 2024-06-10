print ("•×"*17)
print ("\033[1;33m  Aula 12 - Condições aninhadas \033[m")
print ("\033[0;37m Desafio 038: Comparando Números \033[m")
print ("•×"*17)
print("")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
	print("O primeiro valor é \033[1m maior \033[m")
elif num2 > num1:
	print ("O segundo valor é \033[1m maior \033[m")
else:
	print("Não existe valor maior, os dois são \033[1m iguais \033[m")