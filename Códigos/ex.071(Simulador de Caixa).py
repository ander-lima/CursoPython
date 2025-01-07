##########################################
print ("•×"*19)
print ("\033[1;34m         Aula 15 - Break \033[m")
print ("\033[0;32m  Desafio 071: Simulador de Caixa  \033[m")    
print ("•×"*19) 
print("")
##########################################
'''Desafio: Crie um programa de Caixa que peça um valor e traga quantas cédulas serão necessarias. O caixa tem cédulas de: 50$, 20$, 10$ e 1$'''

#versão Ander
'''val = int(input('Insira valor:'))
qnt_50 = qnt_20 = qnt_10 = qnt_1 = 0

while val > 0:
    if val >= 50:
        val = val - 50
        qnt_50 += 1
    elif val >= 20:
        val = val - 20
        qnt_20 += 1
    elif val >= 10:
        val = val - 10
        qnt_10 += 1
    elif val >= 1:
        val = val - 1
        qnt_1 += 1
if qnt_50 > 0:
    print (f'Total de cédulas {qnt_50} de 50$')
if qnt_20 > 0:
    print (f'Total de cédulas {qnt_20} de 20$')
if qnt_10 > 0:
    print (f'Total de cédulas {qnt_10} de 10$')
if qnt_50 > 0:
    print (f'Total de cédulas {qnt_1} de 1$')'''

#versão Guanabara
print('= =' * 10)
print('{:^30}'.format('Banco'))
print('= =' * 10)

valor = total = int(input('Insira o valor a se retirar: '))
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
             print(f'Total de {totced} de cédulas de R$ {ced}')

        if ced == 50:
            ced = 20
            totced = 0
        elif ced == 20:
            ced = 10
            totced = 0
        elif ced == 10:
            ced = 1
            totced = 0
        if total == 0:
            break
