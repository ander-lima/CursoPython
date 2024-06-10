print ("•×"*16)
print ("\033[1;33m Aula 12 - Condições aninhadas \033[m")
print ("\033[0;37m   Desafio 036: Empréstimo \033[m")
print ("•×"*16)
print("")

valor_casa = float(input("Qual o valor da casa ? R$ "))
anos = int(input("Em quantos anos deseja parcelar ? "))
salario = float(input("Qual seu salário atual ? R$ "))
print("")

valor_parcela = (valor_casa/anos)/12 # Valor da parcela mensal
pode_pagar = salario*0.3 #Valor que a pessoa pode pagar não pode exceder 30% do salário

print("O valor da parcela seria de \033[0;31mR$ {:.2f}\033[m e o valor que você pode pagar é de \033[0;32mR$ {}\033[m então:".format(valor_parcela, pode_pagar))
print("")

if valor_parcela > pode_pagar:
	print ("Infelizmente seu salário não permite realizar o empréstimo")
else:
	print("Você pode efetuar esse empréstimo")
print ("Muito obrigado!")