##########################################
print ("•×"*19)
print ("\033[1;34m      Aula 13 - Repetição com FOR \033[m")
print ("\033[0;32m      Desafio 053: Palíndromo  \033[m")    
print ("•×"*19)
print("")
##########################################
'''Desafio: Leia uma string e confirme se ela é ou não um palíndromo'''

#1 pegar string e padronizar
#2 juntar a string
#3 inverter a string
#4 comparar string invertida com string padrão

frase = str(input("Insira uma frase ou palavra: ")).strip().upper() #1
palavras = frase.split() #2
unir = ''.join(palavras)
inverso = unir [::-1] #3
print("O inverso de {} é {}".format(unir, inverso))
if unir == inverso:
    print("\033[1;32m Temos \033[m aqui um Palíndromo.")
else:
    print("Isso \033[1;31m Não \033[m é um Paliíndromo")