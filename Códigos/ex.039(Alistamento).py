import datetime

print ("•×"*16)
print ("\033[1;33m Aula 12 - Condições aninhadas \033[m")
print ("\033[0;37m   Desafio 039: Alistamento \033[m")
print ("•×"*16)
print("")

print("Em que ano você nasceu ? ")
nascimento = int(input())
ano_atual = datetime.date.today().year
idade = (ano_atual - nascimento)
print("")

print("Você se alistou ? SIM ou NÃO: ")
pergunta = str(input()).upper()

if pergunta == 'SIM':
	if idade > 18:
		print("Que bom que se alistou. Você tem {} anos".format(idade))
	elif idade == 18:
		print("Se alistou a tempo! Você tem {} anos".format(idade)) 
	else:
		print("Você não deveria conseguir isso, tem apenas {} anos e o alistamento é com 18 anos.")
	
elif pergunta == 'NÃO' or pergunta == 'NAO':
	if idade > 18:
		print("Você deve se alistar o mais rapido possivel ! Você tem {} anos e deveria ter se alistado com 18.".format(idade))
	elif idade == 18:
		print("Você deve se alistar ainda esse ano! Você tem 18 anos.")
	else:
		print("Fique tranquilo, você tem apenas {} anos e o alistamento deve aer feito aos 18 anos".format(idade))
else:
	print ("Resposta invalida")