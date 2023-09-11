# Exercício 07: Faça um algoritmo que receba o valor do salário de uma pessoa,
# e o valor de um financiamento pretendido. Caso o financiamento seja menor ou
# igual a 5 vezes o salário da pessoa, o algoritmo deverá escrever
# "Financiamento Concedido"; senão, ele deverá escrever "Financiamento Negado".
# Independente de conceder ou não o financiamento, o algoritmo escreverá depois
# a frase "Obrigado por nos consultar."


def verificar_financiamento():
    salario = float(input("Informe o seu salário: "))

    financiamento_desejado = float(
      input("Informe o valor do financiamento pretendido: ")
    )

    permitir_financiamento = salario * 5

    if financiamento_desejado <= permitir_financiamento:
        result = "Financiamento Concedido."
    else:
        result = "Financiamento Negado."

    return f"""
          {result}
          Obrigado por nos consultar.
    """
