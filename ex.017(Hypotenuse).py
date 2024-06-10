#crie um progamanque leoa os catetos e diga a hipotenusa |__
'''co = float(input("Cateto oposto: "))
ca = float(input("Cateto adjacente: "))
hip = (co**2 + ca**2)**(1/2)
print ("Então essa é a hipotenusa: {:.2f}".format(hip))'''
import math
co = float(input("Cateto oposto: "))
ca = float(input("Cateto adjacente: "))
hip = math.hypot(co,ca)
print ("A hipotenusa é: {:.2f}".format(hip))