#Armazena variaveis
a = eval(input('Escolha um valor: '))
b = eval(input('Escolha outro valor: '))

#Define uma variavel como maior
maior = a

#Condição da função
if (b>maior):
	maior = b
print(f'O maior valor é: {maior}')