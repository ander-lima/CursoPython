##########################################
print ("•×"*19)
print ("\033[1;34m      Aula 13 - Repetição com FOR \033[m")
print ("\033[0;32m   Desafio 062: Progressão Aritmétrica 3.0  \033[m")    
print ("•×"*19)
print("")
##########################################
'''Desafio: Programa exige primeiro termo e razão PA, após isso realiza a progressão dos 10 primeiros termos. Após ele deve questionar quantos termos a mais mostrar e mostrar essa quantidade'''

'''#versão Ander
#Lógica: Programa executa > Pergunta > Se != 0 > Executa enquanto qnt for != 0

primeiro = int(input('Insira o primeiro termo: '))
razao = int(input('Insira a razão: '))
termo = primeiro
count = 0
qnt = 10 #Quantidade inicial de termos 
total = 0 # Quantidade total de termos exibidos

print('')
print('Eis a Progressão Aritmétrica')

while qnt != 0:
    total += qnt #atualiza total de termos
    while count < total: 
        print(termo, end = ' > ')
        termo += razao
        count += 1
    print('FIM')
    print('')
    qnt = int(input('Quantos termos a mais você deseja ?'))
print(' ')
print(f'Progressão finalizada com {total} termos no total.')
'''

#Versão Guanabara

primeiro = int(input('Insira o primeiro termo: '))
r = int(input('Insira a razão: '))
count = 0
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total += mais
    while count <= total:
        print(termo, end=' > ')
        termo += r  # Atualiza o termo somando a razão
        count += 1  # Incrementa o contador
    print('PAUSA')
    mais = int(input('Quantos termos a mais você deseja ?   '))
print('Progressão finalizada com {} termos'.format(total))