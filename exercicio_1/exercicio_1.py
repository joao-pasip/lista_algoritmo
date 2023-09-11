import math

# Exercício 01: Faça um Algoritmo para calcular a área de um círculo,
# após o usuário informar o valor do raio, que deve ser positivo.
# Fórmula para o cálculo de área: 𝑨 = 𝝅𝒓𝟐


def calcular_area_circulo():
    valor_pi = math.pi
    pi = round(valor_pi, 2)
    input_raio = float(input("Digite o valor do raio: "))
    if input_raio > 0:
        area = pi * (input_raio ** 2)
    else:
        area = "O valor do raio precisa ser positivo."
    return area
