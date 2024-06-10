import random 
import time

print ("•×"*19)
print ("\033[1;33m    Aula 12 - Condições aninhadas \033[m")
print ("\033[0;32m Desafio 045: GAME - JOKENPÔ v.Ander \033[m")
print ("•×"*19)
print("")

print ('''Escolha seu movimento:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
print("")
jogador = int(input(">"))
computador = random.randrange(1,4)
print("")

print ("JO")
time.sleep (0.5)
print ("KEN")
time.sleep (0.5)
print ("PÔ!")
print("")

if jogador == 1:
	if computador == 1:
		print("Escolhi Pedra: Empate")
	elif computador == 2:
		print("Escolhi Papel: Você perdeu")
	else:
		print("Escolhi Tesoura: Você venceu")
elif jogador == 2:
	if computador == 1:
		print("Escolhi Pedra: Você venceu")
	elif computador == 2:
		print("Escolhi Papel: Empate")
	else:
		print("Escolhi Tesoura: Você perdeu")
elif jogador == 3:
	if computador == 1:
		print("Escolhi Pedra: Você perdeu")
	elif computador == 2:
		print("Escolhi Papel: Você venceu")
	else:
		print("Escolhi Tesoura: Empate")
else:
	print ("Mas o que caralhos é {} ?".format(jogador))
	time.sleep (1)
	print ("Eu nem te dei essa opção, logo...") 
	time.sleep (2)
	print ("VOCÊ PERDE MUAHAHAHAH")