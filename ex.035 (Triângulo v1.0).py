print ("-="*15)
print ("\033[7;39mAnalise de triângulo\033[m")
print ("-="*15)

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro Segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
	print ("Eles \033[0;32mPODEM\033[m formar um triângulo.")
else:
	print ("Eles \033[31mNÃO PODEM\033[m formar um triângulo.")