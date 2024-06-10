from datetime import date

print ("•×"*17)
print ("\033[1;33m  Aula 12 - Condições aninhadas \033[m")
print ("\033[0;37m Desafio 041: Classificação \033[m")
print ("•×"*17)
print("")


atual = date.today().year
nascimento = int (input("Em que ano você nasceu ?"))
idade = atual - nascimento
print(f"Você tem {idade} anos")
if idade <= 2:
	print ("Pela sua idade, você não pode participar.")
elif idade <= 9 and idade >= 3:
	print ("Classificação: Mirim")
elif idade <= 14:
	print ("Classificação: Infantil")
elif idade <= 19:
	print ("Classificação: Junior")
elif idade <= 25:
	print ("Classificação: Senior")
else:
	print ("Classificação: Masterr")