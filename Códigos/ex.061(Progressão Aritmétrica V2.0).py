##########################################
print ("•×"*19)
print ("\033[1;34m      Aula 13 - Repetição com FOR \033[m")
print ("\033[0;32m   Desafio 061: Progressão Aritmétrica 2.0  \033[m")    
print ("•×"*19)
print("")
##########################################
'''Desafio: Programa exige primeiro termo e razão PA, após isso realiza a progressão dos 10 primeiros termos'''

'''#versão Ander

#Lógica: Define Primeiro; Razão e Contador >> Enquanto Contador for Menor que 11 executar >> Para cada 'c' no range // Contador +1

primeiro = int(input('Insira o primeiro termo: '))
r = int(input('Insira a razão: '))
count = 0
termo = primeiro

while count < 10:
    print(termo, end=' > ')
    termo += r  # Atualiza o termo somando a razão
    count += 1  # Incrementa o contador
print('Acabou')'''

#Versão Guanabara
#Identico