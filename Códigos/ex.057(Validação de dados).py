##########################################
print ("•×"*19)
print ("\033[1;34m      Aula 14 - Repetição com WHILE \033[m")
print ("\033[0;32m   Desafio 057: Validação de dados  \033[m")    
print ("•×"*19)
print("")
##########################################
'''Desafio: Programa deve pedir SEXO [M/F] e não parar até ser um dos valores permitidos'''

s = input('Insira seu sexo [M/F]: ').strip().upper()
while s not in ['M', 'F']:
    s = input('Insira seu sexo [M/F]: ').strip().upper()
print('Sexo {} registrado com sucesso'.format(s))
