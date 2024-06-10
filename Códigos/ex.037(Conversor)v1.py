print ("•×"*16)
print ("\033[1;33m Aula 12 - Condições aninhadas \033[m")
print ("\033[0;37m   Desafio 037: Conversor \033[m")
print ("•×"*16)
print("")

num = int(input("Digite um número: "))
print("")
print("""Escolha a base de conversão
Digite 1 para: Binário
Digite 2 para: Octal
Digite 3 para: Hexadecimal""")
print("")
escolha = int(input("Base de conversão: "))
if escolha == 1:
	binario = bin(num).replace('0b', '{} em Binário: '.format(num))
	print(binario)
elif escolha == 2:
	octal = oct(num).replace('0o', '{} em Octal: '.format(num))
	print(octal)
elif escolha == 3:
	hexadecimal = hex(num).replace('0x', '{} em Hexadecimal: '.format(num))
	print(hexadecimal)
else:
	print("Esse número não é válido")