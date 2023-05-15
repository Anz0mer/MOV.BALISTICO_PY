# Biblioteca de matemática para conseguir realizar os cálculos
from math import *

# Dados que o exercício oferece
altura_da_bola = float(input("Digite a altura da bola: "))
velocidade_0_bola = float(input("Digite a velocidade 0 da bola em m/s: "))                          

# Conversões que precisamos fazer para rodar o programa
gravidade = 9.80
altura_da_bola = altura_da_bola / 100
#velocidade_0_bola = velocidade_0_bola / 3.6

altura_da_bola = round(altura_da_bola, 3)
velocidade_0_bola = round(velocidade_0_bola, 3)

angulo_bola = (altura_da_bola * (2 * gravidade)) / (velocidade_0_bola ** 2)
angulo_bola = sqrt(angulo_bola)
angulo_bola = radians (angulo_bola)
angulo_bola = asin (angulo_bola)

# Relações trigonométricas que os exercícios pedem
cosseno = cos(angulo_bola)
seno = sin(angulo_bola)

cosseno = round(cosseno, 3)
seno = round(seno, 3)

# Cálculos para descobrir a velocidade inicial de x e a velocidade inicial de y
v0x = velocidade_0_bola * cosseno
v0y = velocidade_0_bola * seno

v0x = round(v0x, 3)
v0y = round(v0y, 3)

# Resultados para descobrir a velocidade inicial de x e a velocidade inicial de y
print(" ")
print("Velocidade de v0x: %.3f\n" % v0x)
print("Velocidade de v0y: %.3f\n" % v0y)

# Cálculos para descobrir o tempo de alcance da bola
#posicao_final = altura_da_bola + (v0y * tempo_alcance_bola_final) - (5 * (tempo_alcance_bola_final ** 2))
delta = (v0y ** 2) - (4 * - 4.9 * altura_da_bola)
tempo_alcance_bola1 = - (v0y + (sqrt(delta)))/-10
tempo_alcance_bola2 = - (v0y - (sqrt(delta)))/-10

tempo_alcance_bola1 = round(tempo_alcance_bola1, 2)
tempo_alcance_bola2 = round(tempo_alcance_bola2, 2)

# Resultados para descobrir o tempo de alcance da bola
print("Tempo de alcance da bola 1: %.3f\n" % tempo_alcance_bola1)
print("Tempo de alcance da bola 2: %.3f\n" % tempo_alcance_bola2)

# Cálculos para descobrir as velocidades de x e y em um determinado tempo
vx_d = (velocidade_0_bola * cosseno)
vy_d = (velocidade_0_bola * seno) - (gravidade * tempo_alcance_bola1)
modulo_v_d = (vx_d**2) + (vy_d**2)
modulo_v_d = sqrt(modulo_v_d)

vx_d = round(vx_d, 3)
vy_d = round(vy_d, 3)
modulo_v_d = round(modulo_v_d, 3)

vx_d1 = (velocidade_0_bola * cosseno)
vy_d1 = (velocidade_0_bola * seno) - (gravidade * tempo_alcance_bola2)
modulo_v_d1 = (vx_d1**2) + (vy_d1**2)
modulo_v_d1 = sqrt(modulo_v_d1)

vx_d1 = round(vx_d1, 3)
vy_d1 = round(vy_d1, 3)
modulo_v_d1 = round(modulo_v_d1, 3)

# Resultados para descobrir as velocidades de x e y em um determinado tempo
print ("Velocidade de X: %.3f\n" % vx_d)
print ("Velocidade de Y: %.3f\n" % vy_d)
print ("Módulo da velocidade: %.3f\n" % modulo_v_d)
print ("------")
print ("Velocidade de X: %.3f\n" % vx_d1)
print ("Velocidade de Y: %.3f\n" % vy_d1)
print ("Módulo da velocidade: %.3f\n" % modulo_v_d1)

# Cálculos para descobrir o alcance horizontal máximo que a bola alcança
a1 = v0x * tempo_alcance_bola1
a2 = v0x * tempo_alcance_bola2

a1 = round(a1, 3)
a2 = round(a2, 3)

# Resultados para descobrir o alcance horizontal máximo que a bola alcança
print('Alcance horizontal da bola de tempo 1 (A): %.3f\n' % a1)
print('Alcance horizontal da bola de tempo 2 (A): %.3f\n' % a2)

# Cálculos para descobrir a distância de origem.
x0_1 = (a1 - velocidade_0_bola * tempo_alcance_bola1)
x0_2 = (a2 - velocidade_0_bola * tempo_alcance_bola2)
x0_3 = (a1 - velocidade_0_bola * tempo_alcance_bola2)
x0_4 = (a2 - velocidade_0_bola * tempo_alcance_bola1)

# Resultados para descobrir a distância de origem.
print ("A posição de Origem de X1: %.3f\n" % x0_1)
print ("A posição de Origem de X2: %.3f\n" % x0_2)
print ("A posição de Origem de X3: %.3f\n" % x0_3)
print ("A posição de Origem de X4: %.3f\n" % x0_4)
