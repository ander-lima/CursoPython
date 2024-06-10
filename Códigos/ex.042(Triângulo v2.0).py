print ("•×"*17)
print ("\033[1;33m  Aula 12 - Condições aninhadas \033[m")
print ("\033[0;37m Desafio 042: Triângulo V2.0 \033[m")
print ("•×"*17)
print("")

r1 = float(input("Primeiro Segmento: "))
r2 = float(input("Segundo Segmento: "))
r3 = float(input("Terceiro Segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
	print("Os segmentos \033[1;32m podem \033[m formar um Triângulo ", end = "")
	if r1 == r2 == r3:
		print ("Equilátero")
	elif r1 != r2 != r3 != r1:
		print ("Escaleno")
	else:
		print ("Isóceles")
else:
	print("Os segmentos \033[1;31m não podem \033[m formar um triângulo")