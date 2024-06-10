dis = float(input("Qual a distancia da viagem ? "))
if dis <= 200:
	valor = dis*0.5
else:
	valor = dis*0.45
print("O valor da viagem de {} KM sera de R$ {:.2f}".format(dis, valor))