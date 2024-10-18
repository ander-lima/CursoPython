##########################################
print ("•×"*19)
print ("\033[1;34m      Aula 15 - Break \033[m")
print ("\033[0;32m   Desafio 070: Estátisticas em Produtos  \033[m")    
print ("•×"*19)
print("")
##########################################
'''Desafio: Deve armazenar nome preço de produtos em Loop até que usuário diga que quer sair. Com programa finalizado deve trazer informações: Total da compra; Quantidade de produtos que custaram mais de R$1000,00; Nome e preço do produto mais barato'''

#versão Ander
print('='*20)
print ('   LOJA DO ANDER')
print('='*20)

tot_compra = prod_maior1000 = preco_mbarato = 0

while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))

    tot_compra += preco

    if preco >= 1000:
        prod_maior1000 += 1
        
    if preco_mbarato == 0:
        nome_mbarato = nome
        preco_mbarato = preco
    elif preco < preco_mbarato:
        nome_mbarato = nome
        preco_mbarato = preco

    resp = ' '
    while resp not in 'sn':
        resp = str(input('Quer continuar? [S/N]')).strip().lower()[0]
    if resp == 'n':
        break

print ('---------FIM DO PROGRAMA---------')

print(f'O total da compra foi {tot_compra}')
print(f'Temos {prod_maior1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_mbarato} que custa R${preco_mbarato}')