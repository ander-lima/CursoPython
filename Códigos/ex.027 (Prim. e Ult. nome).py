nome = input("Insira aqui seu nome: ").split() #split separa nome
ult = len(nome)-1 #pega o ultimo nome
print ("O primeiro nome é {} e o ultimo nome é {}".format(nome[0], nome[ult]))