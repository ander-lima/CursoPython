num = int(input('Insira:'))
cont = 2
fiba = 1
fib = 1
print ("1")
print ("1")
while (cont <= num):
	aux = fib
	fib = fib + fiba
	fiba = aux
	cont = cont + 1
	print (fib)