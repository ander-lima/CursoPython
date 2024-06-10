frase = str(input("Insira uma palavra ou frase: ")).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto [::-1]
'''for letra in range (-1, -1, -1):
	inverso += junto[letra]
print (f'O inverso de {junto} é {inverso}')'''
if inverso == junto:
	print ('É um palindromo')
else:
	print ("Não é palindromo")