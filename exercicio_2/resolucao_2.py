# Exercício 02: Faça um algoritmo que leia 3 valores - a, b e c - e calcule:
# a) A área do trapézio que tem a como base maior,b base menor e c como altura.
# b) A área do quadrado, que tem a variável b como medida do seu lado.
# c) A área da superfície de um cubo que tem c por aresta.


def calcular_area_trapezio_quadrado_cubo():
    result = ''
    menu = """
    O que deseja calcular?
    Digite:
    t - Calcular área do trapézio
    q - Calcular área do quadrado
    c - Calcular área da superfície do cubo
    s - Sair do sistema
    """
    status_system = True

    while status_system:
        input_user = input(menu).lower()
        if input_user == 't':
            base_maior = float(input("Informe o valor da base maior: "))
            base_menor = float(input("Informe o valor da base menor: "))
            altura = float(input("Informe o valor da altura: "))
            area_trapezio = ((base_maior + base_menor) * altura)/2
            result = f"A área do trapézio é igual a {area_trapezio}."
            print(result)
        elif input_user == 'q':
            lado = float(input("Informe o valor do lado: "))
            area_quadrado = lado ** 2
            result = f"A área do quadrado é igual a {area_quadrado}."
            print(result)
        elif input_user == 'c':
            aresta = float(input("Informe o valor da aresta: "))
            area_cubo = 6 * (aresta ** 2)
            result = f"A área da superfície do cubo é igual a {area_cubo}."

            print(result)
        elif input_user == 's':
            status_system = False
        else:
            print("Opção inválida.")
    return result
