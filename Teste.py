from math import *

altura_da_bola = float(input("Digite a altura da bola: " ))
velocidade_0_bola = float(input("Digite a velocidade 0 da bola: "))
angulo_bola = float(input('Digite o angulo da bola: '))                               

angulo_bola = radians(angulo_bola)
gravidade = 10.00

cosseno = cos(angulo_bola)
seno = sin(angulo_bola)

seno_ao_quadrado = angulo_bola ** 2
cosseno_ao_quadrado = angulo_bola ** 2

seno_ao_quadrado = sin(seno_ao_quadrado)
cosseno_ao_quadrado = cos(cosseno_ao_quadrado)

v0x = velocidade_0_bola * cosseno
v0y = velocidade_0_bola * seno

print("Velocidade de v0x: %.2f\n" % v0x)
print("Velocidade de v0y: %.2f\n" % v0y)

tempo_alcance_bola = (2 * velocidade_0_bola * seno) / gravidade
print("Tempo de alcance da bola: %.2f\n" % tempo_alcance_bola)

h = ((velocidade_0_bola ** 2) * (seno ** 2))/ (2 * gravidade)
print('O ponto mais alto da trajetória (H): %.2f\n' % h)

a = ((velocidade_0_bola ** 2) * (seno * 2))/gravidade
print('Alcance horizontal da bola (A): %.2f\n' % a)
