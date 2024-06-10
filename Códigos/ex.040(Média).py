print ("•×"*16)
print ("\033[1;33m Aula 12 - Condições aninhadas \033[m")
print ("\033[0;37m   Desafio 040: Média \033[m")
print ("•×"*16)
print("")

print("Qual foi sua primeira nota ?")
nota_1 = float(input(""))

print("Qual foi sua segunda nota ?")
nota_2 = float(input(""))

media = (nota_1 + nota_2)/2
if media < 5.0:
	print("Você esta \033[1;31m reprovado\033[m")
elif media >= 5.0 and media <= 6.9:
	print("Você está de \033[0;34 recuperação \033[m")
else:
	print("Sua media foi de {} você está \033[1;32m aprovado! \033[m".format(media))