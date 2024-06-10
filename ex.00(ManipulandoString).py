frase = " Eu amo a Amanda botelho aquela rabuda gostosa do caralho"

print ("Sua frase:")
print (frase)

print ("Sua frase de 2 em 2:")
print (frase[::3])

print ("Quantidade de caracteres: ")
print (len(frase))

print("Quantidade de 'a' em sua frase: ")
print(frase.count('a'))

print("Encontrando 'Amanda' em: ")
print(frase.find('Amanda'))

print("Substituindo:")
frase = frase.replace("gostosa", "deliciosa")
print (frase) 

print ("Maiusculo: ")
print(frase.upper ())
