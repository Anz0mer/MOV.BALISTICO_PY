# Biblioteca de matemática para conseguir realizar os cálculos
from math import *

# Dados que o exercício oferece
altura_da_bola = float(input("Digite a altura da bola: \n"))
velocidade_0_bola = float(input("Digite a velocidade 0 da bola: \n"))
angulo_bola = float(input('Digite o angulo da bola: \n'))                               

# Conversões que precisamos fazer para rodar o programa
altura_da_bola = altura_da_bola / 100
angulo_bola = radians(angulo_bola)
gravidade = 10.00

# Relações trigonométricas que os exercícios pedem
cosseno = cos(angulo_bola)
seno = sin(angulo_bola)

# Cálculos para a primeira questão que seria descobrir a velocidade inicial de x e a velocidade inicial de y
v0x = velocidade_0_bola * cosseno
v0y = velocidade_0_bola * seno

# Resultados para a primeira questão que seria descobrir a velocidade inicial de x e a velocidade inicial de y
print("Velocidade de v0x: %.3f\n" % v0x)
print("Velocidade de v0y: %.3f\n" % v0y)

# Cálculos para a segunda questão que seria descobrir o tempo de alcance da bola
#posicao_final = altura_da_bola + (v0y * tempo_alcance_bola_final) - (5 * (tempo_alcance_bola_final ** 2))
delta = (v0y ** 2) - (4 * -5 * altura_da_bola)
tempo_alcance_bola1 = - (v0y + (sqrt(delta)))/-10
tempo_alcance_bola2 = - (v0y - (sqrt(delta)))/-10

# Resultados para a segunda questão que seria descobrir o tempo de alcance da bola
print("Tempo de alcance da bola 1: %.3f\n" % tempo_alcance_bola1)
print("Tempo de alcance da bola 2: %.3f\n" % tempo_alcance_bola2)

# Cálculos para a terceira questão que seria descobrir as posições de x e y em um determinado tempo

# Resultados para a terceira questão que seria descobrir as posições de x e y em um determinado tempo

# Cálculos para a quarta questão que seria descobrir as velocidades de x e y em um determinado tempo

# Resultados para a quarta questão que seria descobrir as velocidades de x e y em um determinado tempo

# Cálculos para a quinta questão que seria descobrir a altura máxima que a bola alcança
h = ((velocidade_0_bola ** 2) * (seno ** 2))/ (2 * gravidade)
altura_maxima = h + altura_da_bola

# Resultados para a quinta questão que seria descobrir a altura máxima que a bola alcança
print('O ponto mais alto da trajetória (H): %.3f\n' % altura_maxima)

# Cálculos para a sexta questão que seria descobrir o alcance horizontal máximo que a bola alcança
tempo_alcance_bola = tempo_alcance_bola1 + tempo_alcance_bola2
a = v0x * tempo_alcance_bola

# Resultados para a sexta questão que seria descobrir o alcance horizontal máximo que a bola alcança
print('Alcance horizontal da bola (A): %.3f\n' % a)

# Cálculos para a sétima questão que seria descobrir a velocidade de x e a velocidade de y antes de chegar no solo

# Resultados para a sétima questão que seria descobrir a velocidade de x e a velocidade de y antes de chegar no solo

# Cálculos para a oitava questão que seria descobrir a velocidade de x e a velocidade de y no seu tempo de subida

# Resultados para a oitava questão que seria descobrir a velocidade de x e a velocidade de y no seu tempo de subida
