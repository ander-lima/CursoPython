print ("•×"*17)
print ("\033[1;33m  Aula 12 - Condições aninhadas \033[m")
print ("\033[0;37m   Desafio 044: Loja de Ander \033[m")
print ("•×"*17)
print("")

preco = float(input("Qual o valor da compra ? R$"))
print('''Formas de Pagamento
[ 1 ] Á vista
[ 2 ] Débito
[ 3 ] Crédito até 2x
[ 4 ] Crédito em 3x ou mais
''')
opcao = int(input(""))

if opcao == 1:
	total = preco - ((preco / 100)*10) #10% de desconto
elif opcao == 2:
	total = preco - ((preco / 100)*5) #5% de desconto
elif opcao == 3:
	total = preco
	parcela = total / 2
	print('Sua compra será parcelada em 2x de R$ {:.2f} ao final'.format(parcela))
elif opcao == 4:
	total = preco + ((preco / 100)*20) #20% de Juros
	totparc = int(input("Em quantas vezes deseja parcelar ?"))
	parcela = total / totparc
	print ('Sua compra será parcelada em {} de R$ {:.2f} ao final'.format(totparc, parcela))
else:
	print("Opção inválida, por favor tente novamente")
print ('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preco, total))
