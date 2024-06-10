frase = str(input("Digite uma frase: ")).upper().strip()
print("A frase contem {} letras 'A'.".format(frase.count('A')))
print("O primeiro 'A' aparece na posição {}.".format(frase.find('A')+1))
print("O ultimo 'A' aparece na posição {}.".format(frase.rfind('A')+1))