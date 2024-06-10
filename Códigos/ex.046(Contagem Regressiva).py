import time

##########################################
print ("•×"*19)
print ("\033[1;34m      Aula 13 - Repetição com FOR \033[m")
print ("\033[0;32m      Desafio 046: Hora dos Fogos\033[m")    
print ("•×"*19)
print("")
##########################################


#Versão Ander: 

print("Os fogos vão começar em:")
for c in range (10,0,-1):
	print(c)
	time.sleep(1)
print ("🔥🔥🔥")