##########################################
print ("•×"*19)
print ("\033[1;34m      Aula 15 - Break \033[m")
print ("\033[0;32m   Desafio 066: Tratando valores v2.0   \033[m")    
print ("•×"*19)
print("")
##########################################
'''Desafio: Igual ao V1.0 mas sistema deve parar com break e mostrar a quantidade de ciclos e soma total'''

#versão Ander
#lógica: enquanto não 999 > soma em variavel e add +1 cont > if 999 break
n = s = c = 0
while True:
    n = int(input('Insira um número [999 para sair]: '))
    if n == 999:
        break
    s += n
    c += 1
 

print(f'A quantidade de números digitados foi de {c} e a soma é {s}')

#versão Guanabara
#identico