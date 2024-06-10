a = int(input("[1/3] Insira um numero: "))
b = int(input("[2/3] Insira um numero: "))
c = int(input("[3/3] Insira um numero: "))

menor = a
if b < a and b < c:
	menor = b
if c < a and c < b:
	menor = c
	
maior = a
if b > a and b > c:
	maior = b
if c > a and c > b:
	maior = c
	
print ("O menor valor é {}".format(menor))
print ("O maior valor é {}".format(maior))