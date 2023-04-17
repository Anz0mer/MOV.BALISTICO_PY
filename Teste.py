# Biblioteca de matemática para conseguir realizar os cálculos
from math import *

# Dados que o exercício oferece
altura_da_bola = float(input("Digite a altura da bola: "))
velocidade_0_bola = float(input("Digite a velocidade 0 da bola em m/s: "))
angulo_bola = float(input('Digite o angulo da bola: '))                             

# Conversões que precisamos fazer para rodar o programa
angulo_bola = radians(angulo_bola)
gravidade = 10.00
#altura_da_bola = altura_da_bola / 100
#velocidade_0_bola = velocidade_0_bola / 3.6

# Relações trigonométricas que os exercícios pedem
cosseno = cos(angulo_bola)
seno = sin(angulo_bola)

# Q1 Cálculos para a primeira questão que seria descobrir a velocidade inicial de x e a velocidade inicial de y
v0x = velocidade_0_bola * cosseno
v0y = velocidade_0_bola * seno

# Resultados para a primeira questão que seria descobrir a velocidade inicial de x e a velocidade inicial de y
print("(Q1) Velocidade de v0x: %.3f\n" % v0x)
print("(Q1) Velocidade de v0y: %.3f\n" % v0y)

# Q2 Cálculos para a segunda questão que seria descobrir o tempo de alcance da bola
#posicao_final = altura_da_bola + (v0y * tempo_alcance_bola_final) - (5 * (tempo_alcance_bola_final ** 2))
delta = (v0y ** 2) - (4 * -5 * altura_da_bola)
tempo_alcance_bola1 = - (v0y + (sqrt(delta)))/-10
tempo_alcance_bola2 = - (v0y - (sqrt(delta)))/-10

# Resultados para a segunda questão que seria descobrir o tempo de alcance da bola
print("(Q2) Tempo de alcance da bola 1: %.3f\n" % tempo_alcance_bola1)
print("(Q2) Tempo de alcance da bola 2: %.3f\n" % tempo_alcance_bola2)

# Q3 Cálculos para a terceira questão que seria descobrir as posições de x e y em um determinado tempo
tempo_c = float(input("Digite o tempo da questão c: "))

x = (velocidade_0_bola * cosseno) * tempo_c
y = ((altura_da_bola + (v0y * tempo_c)) - (5 * (tempo_c**2)))

# Resultados para a terceira questão que seria descobrir as posições de x e y em um determinado tempo
print ("(Q3) Posição de X: %.3f\n" % x)
print ("(Q3) Posição de Y: %.3f\n" % y)

# Q4 Cálculos para a quarta questão que seria descobrir as velocidades de x e y em um determinado tempo
vx_d = (velocidade_0_bola * cosseno)
vy_d = (velocidade_0_bola * seno) - (gravidade * tempo_c)
modulo_v_d = (vx_d**2) + (vy_d**2)
modulo_v_d = sqrt(modulo_v_d)

# Resultados para a quarta questão que seria descobrir as velocidades de x e y em um determinado tempo
print ("(Q4) Velocidade de X: %.3f\n" % vx_d)
print ("(Q4) Velocidade de Y: %.3f\n" % vy_d)
print ("(Q4) Módulo da velocidade: %.3f\n" % modulo_v_d)

# Q5 Cálculos para a quinta questão que seria descobrir a altura máxima que a bola alcança
h = ((velocidade_0_bola ** 2) * (seno ** 2))/ (2 * gravidade)
altura_maxima = h + altura_da_bola

# Resultados para a quinta questão que seria descobrir a altura máxima que a bola alcança
print('(Q5) O ponto mais alto da trajetória (H): %.3f\n' % altura_maxima)

# Q6 Cálculos para a sexta questão que seria descobrir o alcance horizontal máximo que a bola alcança
a1 = v0x * tempo_alcance_bola1
a2 = v0x * tempo_alcance_bola2

# Resultados para a sexta questão que seria descobrir o alcance horizontal máximo que a bola alcança
print('(Q6) Alcance horizontal da bola de tempo 1 (A): %.3f\n' % a1)
print('(Q6) Alcance horizontal da bola de tempo 2 (A): %.3f\n' % a2)


# Q7 Cálculos para a sétima questão que seria descobrir a velocidade de x e a velocidade de y antes de chegar no solo
vx_g = (velocidade_0_bola * cosseno)
vy_g = (velocidade_0_bola * seno) - (gravidade * tempo_alcance_bola1)
modulo_v_g = (vx_g**2) + (vy_g**2)
modulo_v_g = sqrt(modulo_v_g) 

# Resultados para a sétima questão que seria descobrir a velocidade de x e a velocidade de y antes de chegar no solo
print ("(Q7) Velocidade de X: %.3f\n" % vx_g)
print ("(Q7) Velocidade de Y: %.3f\n" % vy_g)
print ("(Q7) Módulo da velocidade: %.3f\n" % modulo_v_g)

# Q8 Cálculos para a oitava questão que seria descobrir a velocidade de x e a velocidade de y no seu tempo de subida
tempo_subida = (v0y / gravidade)

vx_h = (velocidade_0_bola * cosseno)
vy_h = (velocidade_0_bola * seno) - (gravidade * tempo_subida)
modulo_v_h = (vx_h**2) + (vy_h**2)
modulo_v_h = sqrt(modulo_v_h) 

# Resultados para a oitava questão que seria descobrir a velocidade de x e a velocidade de y no seu tempo de subida
print ("(Q8) Velocidade de X: %.3f\n" % vx_h)
print ("(Q8) Velocidade de Y: %.3f\n" % vy_h)
print ("(Q8) Módulo da velocidade: %.3f\n" % modulo_v_h)
