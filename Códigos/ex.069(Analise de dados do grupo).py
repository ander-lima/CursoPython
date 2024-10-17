##########################################
print ("•×"*19)
print ("\033[1;34m      Aula 15 - Break \033[m")
print ("\033[0;32m   Desafio 069: Analise de dados do grupo  \033[m")    
print ("•×"*19)
print("")
##########################################
'''Desafio: Programa deve ler até indicado que não, perguntando idade e esexo de pessoas e depois puxar total de pessoas com mais de 18 anos, quantos homens e quantas mulheres com menos de 20 anos'''

#versão Ander
''' pessoas_maiores = qnt_homens = qnt_mulheres = 0
while True:
    print('-'*20)
    print ('Cadastre uma Pessoa')
    print('-'*20)

    idade = int(input('Idade:'))
    sexo = str(input('Sexo: [M/F]')).strip().lower()[0]

    if idade >= 18:
        pessoas_maiores += 1
    if sexo == 'm':
        qnt_homens +=1
    if sexo == 'f' and idade <= 20:
        qnt_mulheres += 1


    loop = input('Quer continuar ? [S/N]').strip().lower()[0]
    if loop == 'n':
        break
    elif loop == 's':
        continue

print (f'Você cadastrou {pessoas_maiores} pessoas com mais de 18 anos')
print(f'Você cadastrou {qnt_homens} homens no total')
print(f'Você cadastrou {qnt_mulheres} mulheres com menos de 20 anos')
print('')
print('======= FIM DO PROGRAMA =======')'''

#versão Guanabara
tot_18 = tot_h = tot_m20 = 0
while True:

    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'mf': 
        sexo = str(input('Sexo: [M/F]')).strip().lower()[0]

        if idade >= 18:
            tot_18 += 1
        if sexo == 'm':
            tot_h +=1
        if sexo == 'f' and idade <= 20:
            tot_m20 += 1
    resp = ' '

    while resp not in 'sn':
        resp = input('Quer continuar ? [S/N]').strip().lower()[0]
    if resp == 'n':
        break

print (f'Você cadastrou {tot_18} pessoas com mais de 18 anos')
print(f'Você cadastrou {tot_h} homens no total')
print(f'Você cadastrou {tot_m20} mulheres com menos de 20 anos')
print('')
print('======= FIM DO PROGRAMA =======')
