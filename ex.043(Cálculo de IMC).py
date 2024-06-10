print ("•×"*17)
print ("\033[1;33m  Aula 12 - Condições aninhadas \033[m")
print ("\033[0;37m    Desafio 043: Cálculo IMC \033[m")
print ("•×"*17)
print("")

peso = float(input("Qual seu peso em Kg ? "))
altura = float(input("Qual sua altura em M ? "))

imc = peso / (altura ** 2)

print ('O IMC é de {:.1f}'.format(imc))

if imc < 18.5:
	print ('Abaixo do peso')
elif 18.5 <= imc < 25:
	print('Peso ideal')
elif 25 <= imc < 30:
	print ('Sobrepeso')
elif 30 <= imc < 40:
	print ('Obesidade')
else:
	print('Obesidade mórbida')