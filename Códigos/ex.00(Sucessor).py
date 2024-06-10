#Passos:
	#Analisar varivel; Armazenar; Diminuir 1 para Predecessor e Aumentar 1 para Sucessor.
	
#Arm. variavel
n = int(input("Insira um numero: "))
#Função
pre = n - 1
suc = n +1

print ("O sucessor de {} é {}. E seu predecessor é {}.".format(n, suc, pre))