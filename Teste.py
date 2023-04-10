from math import *

altura_da_bola = 71.00
velocidade_0_bola = 20.50
angulo_bola = radians(35)

cosseno = cos(angulo_bola)
seno = sin(angulo_bola)

v0x = velocidade_0_bola * cosseno
v0y = velocidade_0_bola * seno

print("%f" % v0x)
print("%.2f" % v0y)
