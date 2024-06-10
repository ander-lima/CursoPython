#Faça um programa que leia o valor de um angulo qualquer e diga o valor do seno, consseno e tangente
import math
an = float(input('Insira aqui um angulo qualquer: '))
sen = math.sin(math.radians(an))
print("O sen é {:.2f}".format(sen))
cos = math.cos(math.radians(an))
print("O Cosseno é {:.2f}".format(cos))
tan = math.tan(math.radians(an))
print("O Cosseno é {:.2f}".format(tan))
