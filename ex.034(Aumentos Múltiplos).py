'''sal = float (input("Qual o salário a obter aumento ? ")) #Guarda salário em variavel

if sal > 0 and sal >= 1250: #Salário Maior
	aum = sal/100*10 #Valor aumento 10%
	sala = sal + aum #Valor Salário atualizado
	val = "R$ {:,.2f}".format(sala).replace(",", "X").replace(".", ",").replace("X", ".") #formata valor
	print (f"Aumento de R$ {sal} para R$ {val}")
	
elif sal <= 0: #Salario 0
	print ("Salário Incorreto")

else: #Saláerio menor
	aum = sal/100*15 #Valor aumento 10%
	sala = sal + aum #Valor Salário atualizado
	val = "R$ {:,.2f}".format(sala).replace(",", "X").replace(".", ",").replace("X", ".") #formata salario
	print (f"Aumento de R$ {sal} para R$ {val}")'''
	
sal = float (input("Qual o salário a obter aumento ? R$")) #Guarda salário em variavel
if sal <= 1250:
	novo = sal + (sal*15/100)
elif sal <= 0:
	novo = "Salário Invalido"
else:
	novo = sal + (sal*10/100)
print ("Quem ganhava R$ {:,.2f} passa a ganhar R$ {:,.2f}".format(sal, novo).replace(",", "X").replace(".", ",").replace("X", "."))