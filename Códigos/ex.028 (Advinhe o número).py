import random
import time
a = random.randrange(0,6)
print("="*41)
print ("Tente adivinhar o número que estou pensando. Dica: Entre 0 e 5: ")

print("="*41)

num = int(input())

print ("")
print ("Pensando...")
print ("")

time.sleep (2)

if a == num:
	print("Caramba, você acertou, foi esse numero que eu pensei!")
else:
	print ("Nah, não foi esse número que eu pensei. O número que pensei foi {} ".format(a))