print ("•×"*19)
print ("\033[1;34m     Aula 14 - Repetição com WHILE \033[m")
print ("\033[0;33m       Testando Ferramenta \033[m")    
print ("•×"*19)
print("")


'''
FOR é usado quando você sabe quantas vezes precisa ser executado (ex. for x in range (1 - 5))
WHILE é usado quando você NÃO sabe quantas vezes será executado
'''
n = 1
impar = par = 0

while n != 0:
    n = int(input('Digite número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('A quantidade de números pares foi {} e impares foi {}'.format(par, impar))