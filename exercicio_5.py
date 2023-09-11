# Exercício 05: Faça um algoritmo que leia o nome de um piloto,
# a distância percorrida (em km), e o tempo que o piloto levou
# para percorrê-la (em horas). O programa deve calcular a velocidade média,
# em km/h, e exibir a seguinte frase:
# A velocidade média do <nome do piloto> foi <x> km/h.

def calcular_velocidade_media():
    nome_piloto = input("Informe o nome do piloto: ")
    distancia_em_km = float(input("Informe a distância percorrida(em km): "))
    tempo_em_horas = float(
        input("Informe o tempo para percorrê-la(em horas): ")
    )

    velocidade_media = distancia_em_km/tempo_em_horas

    result = f"""
      A velocidade média do(a) {nome_piloto} foi {velocidade_media:.2f}km/h.
    """

    return result
