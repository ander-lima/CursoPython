print ("\033[1m=•=\033[m"*13)
print("\033[1mQual a velocidade atual do carro ?\033[m ")
print ("\033[1m=•=\033[m"*13)

vel = int(input())

multa = (vel - 80)*7
if vel <= 80:
	print("Está \033[1;32mtudo bem\033[m, mantenha viagem mas com cuidado !")
else:
	mensagem = "Ei, você está dirigindo muito rápido, você deverá pagar uma multa de {}R$ {:,.2f}{}!!".format('\033[1;31m', multa, '\033[m')
	mensagem_formatada = mensagem.replace(",", "X").replace(".", ",").replace("X", ".")
	print (mensagem_formatada)