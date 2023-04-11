from math import *

altura_da_bola = float(input("Digite a altura da bola:" ))
velocidade_0_bola = float(input("Digite a velocidade 0 da bola: ")
angulo_bola = radians(input('Digite o angulo da bola: '))                               

gravidade = 10

cosseno = cos(angulo_bola)
seno = sin(angulo_bola)

v0x = velocidade_0_bola * cosseno
v0y = velocidade_0_bola * seno

print("Velocidade de v0x: %.2f" % v0x)
print("Velocidade de v0y: %.2f" % v0y)

tempo_alcance_y = (2 * (v0x * seno))/gravidade
print("Tempo de alcance de y: %.2f" % tempo_alcance_y)
