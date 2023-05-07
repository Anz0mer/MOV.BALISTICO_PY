# Biblioteca de matemática para conseguir realizar os cálculos
from math import *

# Dados que o exercício oferece
altura_da_bola = float(input("Digite a altura da bola: "))
velocidade_0_bola = float(input("Digite a velocidade 0 da bola em m/s: "))                          

# Conversões que precisamos fazer para rodar o programa
gravidade = 10.00
altura_da_bola = altura_da_bola / 100
velocidade_0_bola = velocidade_0_bola / 3.6

altura_da_bola = round(altura_da_bola, 3)
velocidade_0_bola = round(velocidade_0_bola, 3)

# Questão 02 do questionário de Mov. Bálistico
x0_1 = (a1 - velocidade_0_bola * tempo_alcance_bola1)
x0_2 = (a2 - velocidade_0_bola * tempo_alcance_bola2)

# Resultados para a questão 02 do questionário de Mov. Bálistico
print ("(Q2) A posição de Origem de X1: %.3f\n" % x0_1)
print ("(Q2) A posição de Origem de X2: %.3f\n" % x0_2)
