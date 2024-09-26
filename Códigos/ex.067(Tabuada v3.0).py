##########################################
print ("•×"*19)
print ("\033[1;34m      Aula 15 - Break \033[m")
print ("\033[0;32m   Desafio 067: Tabuada v3.0  \033[m")    
print ("•×"*19)
print("")
##########################################
'''Desafio: Deve entregar tabuada de varios numeros até que o numero exigido seja negativo '''

#versão Ander
#logica: enquanto verdade >  \if valor variavel =< 0 ; BREAK\ > print valor da variavel em tabuada
#logica tabuada: para i in range 1~10 ; print (variavel * {i})

while True:
    num = int(input('Insira um número [Negativo para parar]: '))
    if num <= 0:
        print('FIM')
        break
    print('='*20)
    for i in range(1, 11):
        print(f' {num} X {i} = ', num*i)
    print('='*20)