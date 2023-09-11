# Exercício 04: Escrever um algoritmo que solicite o nome de um vendedor,
# o seu salário fixo, o total de vendas por ele efetuadas, e o percentual
# que ganha sobre o total das vendas. Calcular o salário total do vendedor,
# e mostrar o seu nome e o seu salário total.

def calcular_salario_vendedor():
    # vendeu mais de 10 mil -> +1.5% no salário
    # vendeu mais de 20 mil -> +2.0% no salário
    # vendeu mais de 30 mil -> +2.5% no salário
    # vendeu mais de 40 mil -> +3.0% no salário
    # vendeu mais de 50 mil -> +3.5% no salário

    novo_salario = 0
    percentual_sobre_vendas = 0

    percentual_entre_10mil_inclusivo_e_20mil = 1.015
    percentual_entre_20mil_inclusivo_e_30mil = 1.020
    percentual_entre_30mil_inclusivo_e_40mil = 1.025
    percentual_entre_40mil_inclusivo_e_50mil = 1.030
    percentual_mais_de_50mil = 1.035

    msg_bonus_default = """
            Vendeu mais de 10 mil -> +1.5% no salário
            Vendeu mais de 20 mil -> +2.0% no salário
            Vendeu mais de 30 mil -> +2.5% no salário
            Vendeu mais de 40 mil -> +3.0% no salário
            Vendeu mais de 50 mil -> +3.5% no salário
    """

    nome_vendedor = input("Digite o nome do vendedor: ")
    salario_fixo_vendedor = float(
        input("Informe o salário fixo do vendedor: ")
    )
    total_de_vendas_realizadas = float(
        input("Informe o total de vendas efetuadas pelo vendedor: ")
    )
    definir_percentual = input(
        "Escolha 1- Definir um percentual / 2- Usar percentual padrão (1/2): "
    )

    if definir_percentual == "1":
        percentual_escolhido = int(input(
            "Informe quantos '%' deseja como percentual(em número inteiro): "
        ))

        acrescimo_salarial = salario_fixo_vendedor * percentual_escolhido/100
        novo_salario = round(
            salario_fixo_vendedor + acrescimo_salarial, 2
        )

        result = f"""
            O colaborador(a): {nome_vendedor}, tem o seu salário
            fixo mensal no valor de R$ {salario_fixo_vendedor:.2f}.

            Pelo seu desempenho nas vendas, conseguindo atingir a
            marca de {total_de_vendas_realizadas:.2f} reais vendidos,
            terá um bônus de {acrescimo_salarial:.2f} no seu salário.

            Sendo assim, receberá R$ {novo_salario:.2f} esse mês.

            Parabéns pelo desempenho e esforço!!!
        """
    elif definir_percentual == "2":
        if total_de_vendas_realizadas >= 50000:
            percentual_sobre_vendas = percentual_mais_de_50mil
            novo_salario = round(
                salario_fixo_vendedor * percentual_sobre_vendas, 2
            )
        elif (
                (total_de_vendas_realizadas >= 40000) and
                (total_de_vendas_realizadas < 50000)
        ):
            percentual_sobre_vendas = percentual_entre_40mil_inclusivo_e_50mil
            novo_salario = round(
                salario_fixo_vendedor * percentual_sobre_vendas, 2
            )
        elif (
                (total_de_vendas_realizadas >= 30000) and
                (total_de_vendas_realizadas < 40000)
        ):
            percentual_sobre_vendas = percentual_entre_30mil_inclusivo_e_40mil
            novo_salario = round(
                salario_fixo_vendedor * percentual_sobre_vendas, 2
            )
        elif (
                (total_de_vendas_realizadas >= 20000) and
                (total_de_vendas_realizadas < 30000)
        ):
            percentual_sobre_vendas = percentual_entre_20mil_inclusivo_e_30mil
            novo_salario = round(
                salario_fixo_vendedor * percentual_sobre_vendas, 2
            )
        elif (
                (total_de_vendas_realizadas >= 10000) and
                (total_de_vendas_realizadas < 20000)
        ):
            percentual_sobre_vendas = percentual_entre_10mil_inclusivo_e_20mil
            novo_salario = round(
                salario_fixo_vendedor * percentual_sobre_vendas, 2
            )
        else:
            novo_salario = f"""
                Infelizmente não atingiu as metas de venda.
                Sem bônus no salário. Fique atento(a) aos objetivos
                da empresa.

                {msg_bonus_default}
            """

        if percentual_sobre_vendas == 0:
            result = f"""
                {novo_salario}

                Desta forma, seu salário esse mês será o mesmo acordado
                durante a contratação, R$ {salario_fixo_vendedor:.2f}.

                Boa jornada {nome_vendedor},
                e vamos todos ajudar a você conseguir seu bônus no próximo mês!
            """
        else:
            result = f"""
                O colaborador(a): {nome_vendedor}, tem o seu salário
                fixo mensal no valor de R$ {salario_fixo_vendedor:.2f}.

                Pelo seu desempenho nas vendas, conseguindo atingir a
                marca de {total_de_vendas_realizadas:.2f} reais vendidos,
                terá um bônus de {percentual_sobre_vendas} no seu salário.

                Sendo assim, receberá R$ {novo_salario:.2f} esse mês.

                Parabéns pelo desempenho e esforço!!!
            """
    else:
        result = "Opção inválida! Selecione 1 ou 2!"
    return result
