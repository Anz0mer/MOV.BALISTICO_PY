# Biblioteca de matemática para conseguir realizar os cálculos
from math import *

# Dados que o exercício oferece
altura_da_bola = float(input("Digite a altura da bola: "))
velocidade_0_bola = float(input("Digite a velocidade 0 da bola em m/s: "))
angulo_bola = float(input('Digite o angulo da bola: '))                             

# Conversões que precisamos fazer para rodar o programa
angulo_bola = radians(angulo_bola)
gravidade = 9.80
#altura_da_bola = altura_da_bola / 100
#velocidade_0_bola = velocidade_0_bola / 3.6

altura_da_bola = round(altura_da_bola, 3)
velocidade_0_bola = round(velocidade_0_bola, 3)

# Relações trigonométricas que os exercícios pedem
cosseno = cos(angulo_bola)
seno = sin(angulo_bola)

cosseno = round(cosseno, 3)
seno = round(seno, 3)

# Q1 Cálculos para a primeira questão que seria descobrir a velocidade inicial de x e a velocidade inicial de y
v0x = velocidade_0_bola * cosseno
v0y = velocidade_0_bola * seno

v0x = round(v0x, 3)
v0y = round(v0y, 3)

# Resultados para a primeira questão que seria descobrir a velocidade inicial de x e a velocidade inicial de y
print(" ")
print("(A) Velocidade de v0x: %.3f\n" % v0x)
print("(A) Velocidade de v0y: %.3f\n" % v0y)

# Q2 Cálculos para a segunda questão que seria descobrir o tempo de alcance da bola
#posicao_final = altura_da_bola + (v0y * tempo_alcance_bola_final) - (5 * (tempo_alcance_bola_final ** 2))
delta = (v0y ** 2) - (4 * - 4.9 * altura_da_bola)
tempo_alcance_bola1 = - (v0y + (sqrt(delta)))/-9.8
tempo_alcance_bola2 = - (v0y - (sqrt(delta)))/-9.8

tempo_alcance_bola1 = round(tempo_alcance_bola1, 2)
tempo_alcance_bola2 = round(tempo_alcance_bola2, 2)

# Resultados para a segunda questão que seria descobrir o tempo de alcance da bola
print("(B) Tempo de alcance da bola 1: %.3f\n" % tempo_alcance_bola1)
print("(B) Tempo de alcance da bola 2: %.3f\n" % tempo_alcance_bola2)

# Q3 Cálculos para a terceira questão que seria descobrir as posições de x e y em um determinado tempo
tempo_c = float(input("Digite o tempo da questão c: "))

x = (velocidade_0_bola * cosseno) * tempo_c
y = ((altura_da_bola + (v0y * tempo_c)) - (4.9 * (tempo_c**2)))

x = round(x, 3)
y = round(y, 3)

# Resultados para a terceira questão que seria descobrir as posições de x e y em um determinado tempo
print (" ")
print ("(C) Posição de X: %.3f\n" % x)
print ("(C) Posição de Y: %.3f\n" % y)

# Q4 Cálculos para a quarta questão que seria descobrir as velocidades de x e y em um determinado tempo
vx_d = (velocidade_0_bola * cosseno)
vy_d = (velocidade_0_bola * seno) - (gravidade * tempo_c)
modulo_v_d = (vx_d**2) + (vy_d**2)
modulo_v_d = sqrt(modulo_v_d)

vx_d = round(vx_d, 3)
vy_d = round(vy_d, 3)
modulo_v_d = round(modulo_v_d, 3)

# Resultados para a quarta questão que seria descobrir as velocidades de x e y em um determinado tempo
print ("(D) Velocidade de X: %.3f\n" % vx_d)
print ("(D) Velocidade de Y: %.3f\n" % vy_d)
print ("(D) Módulo da velocidade: %.3f\n" % modulo_v_d)

# Q5 Cálculos para a quinta questão que seria descobrir a altura máxima que a bola alcança
h = ((velocidade_0_bola ** 2) * (seno ** 2))/ (2 * gravidade)
altura_maxima = h + altura_da_bola

h = round(h, 3)
altura_maxima = round(altura_maxima, 3)

# Resultados para a quinta questão que seria descobrir a altura máxima que a bola alcança
print('(E) O ponto mais alto da trajetória (H): %.3f\n' % altura_maxima)

# Q6 Cálculos para a sexta questão que seria descobrir o alcance horizontal máximo que a bola alcança
a1 = v0x * tempo_alcance_bola1
a2 = v0x * tempo_alcance_bola2

a1 = round(a1, 3)
a2 = round(a2, 3)

# Resultados para a sexta questão que seria descobrir o alcance horizontal máximo que a bola alcança
print('(F) Alcance horizontal da bola de tempo 1 (A): %.3f\n' % a1)
print('(F) Alcance horizontal da bola de tempo 2 (A): %.3f\n' % a2)


# Q7 Cálculos para a sétima questão que seria descobrir a velocidade de x e a velocidade de y antes de chegar no solo
vx_g = (velocidade_0_bola * cosseno)
vy_g = (velocidade_0_bola * seno) - (gravidade * tempo_alcance_bola1)
modulo_v_g = (vx_g**2) + (vy_g**2)
modulo_v_g = sqrt(modulo_v_g) 

vx_g = round(vx_g, 3)
vy_g = round(vy_g, 3)
modulo_v_g = round(modulo_v_g, 3)
# Resultados para a sétima questão que seria descobrir a velocidade de x e a velocidade de y antes de chegar no solo
print ("(G) Velocidade de X: %.3f\n" % vx_g)
print ("(G) Velocidade de Y: %.3f\n" % vy_g)
print ("(G) Módulo da velocidade: %.3f\n" % modulo_v_g)

# Q8 Cálculos para a oitava questão que seria descobrir a velocidade de x e a velocidade de y no seu tempo de subida
tempo_subida = (v0y / gravidade)

tempo_subida = round(tempo_subida, 3)

vx_h = (velocidade_0_bola * cosseno)
vy_h = (velocidade_0_bola * seno) - (gravidade * tempo_subida)
modulo_v_h = (vx_h**2) + (vy_h**2)
modulo_v_h = sqrt(modulo_v_h) 

vx_h = round(vx_h, 3)
vy_h = round(vy_h, 3)
modulo_v_h = round(modulo_v_h, 3)

# Resultados para a oitava questão que seria descobrir a velocidade de x e a velocidade de y no seu tempo de subida
print ("(H) Velocidade de X: %.3f\n" % vx_h)
print ("(H) Velocidade de Y: %.3f\n" % vy_h)
print ("(H) Módulo da velocidade: %.3f\n" % modulo_v_h)
