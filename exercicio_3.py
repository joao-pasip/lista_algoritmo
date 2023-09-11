import math

# Exercício 03: Faça um algoritmo que determine o volume de uma caixa d’água
# cilíndrica, sendo que o raio e a altura devem ser fornecidos pelo usuário.


def calcular_volume_caixa_d_agua():
    valor_pi = math.pi
    pi = round(valor_pi, 2)

    raio = float(input("Informe o valor do raio: "))
    altura = float(input("Informe o valor da altura(m): "))
    volumeM3 = round(pi * (raio ** 2) * altura, 2)
    volumeLitros = volumeM3 * 1000

    result = f"""
    O volume da caixa d'água é igual a {volumeM3}m3.
    E, {volumeLitros} em litros."""
    return result
