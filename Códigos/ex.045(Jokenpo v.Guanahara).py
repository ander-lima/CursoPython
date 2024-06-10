from random import randint
import time

print ("•×"*19)
print ("\033[1;33m    Aula 12 - Condições aninhadas \033[m")
print ("\033[0;32m Desafio 045: GAME - JOKENPÔ v.Guanabara \033[m")
print ("•×"*19)
print("")

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0,2)

print ('''Escolha seu movimento:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input("Escolha: "))
if jogador >= 3:
	print("Escolha invalida")
else:
	print ("JO")
	time.sleep (1)
	print ("KEN")
	time.sleep (1)
	print ("PÔ")
	
	print("")
	print("~•~"*8)
	print("Jogador jogou: {}".format(itens[jogador]))
	print("Computador jogou: {}".format(itens[computador]))
	print ('~•~'*8)
	
	if jogador == 0:
		if computador == 0:
			print("Empate")
		elif computador == 1:
			print("Você perdeu")
		else:
			print("Você venceu")
	elif jogador == 1:
		if computador == 0:
			print("Você venceu")
		elif computador == 1:
			print("Empate")
		else:
			print("Você perdeu")
	elif jogador == 2:
		if computador == 0:
			print("Você perdeu")
		elif computador == 1:
			print("Você venceu")
		else:
			print("Empate")