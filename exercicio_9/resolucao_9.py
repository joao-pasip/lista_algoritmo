# Exercício 09: A empresa SpaceX decidiu conceder um aumento de salários a seus
# funcionários de acordo com a tabela a seguir:

# salário atual / índice de aumento
# 0 - 400       / 15%
# 401 - 700     / 12%
# 701 - 1000    / 10%
# 1001 - 1800   / 7%
# 1801 - 2500   / 4%
# ACIMA DE 2500 / SEM AUMENTO

# Construa um algoritmo que leia, para cada funcionário, o seu nome e o
# seu salário atual. Após receber esses dados, o algoritmo deverá calcular
# e mostrar o novo salário, conforme modelo a seguir:
# <Nome do funcionário> <% de aumento> <salário atual> <novo salário>
def conceder_aumento_salarial():

    nome_funcionario = input("Informe o nome do funcionário(a): ")
    salario = float(input("Informe o salário do funcionário(a): "))

    if salario > 2500:
        result = f"""
          {nome_funcionario} <% de aumento: SEM AUMENTO>
          <salário atual: {salario:.2f}>
          <novo salário: {salario:.2f}>
        """
    elif salario > 1800 and salario <= 2500:
        bonus = salario * 4/100
        novo_salario = salario + bonus
        result = f"""
          {nome_funcionario} <% de aumento: {bonus:.2f}>
          <salário atual: {salario:.2f}>
          <novo salário: {novo_salario:.2f}>
        """
    elif salario > 1000 and salario <= 1800:
        bonus = salario * 7/100
        novo_salario = salario + bonus
        result = f"""
          {nome_funcionario} <% de aumento: {bonus:.2f}>
          <salário atual: {salario:.2f}>
          <novo salário: {novo_salario:.2f}>
        """
    elif salario > 700 and salario <= 1000:
        bonus = salario * 10/100
        novo_salario = salario + bonus
        result = f"""
          {nome_funcionario} <% de aumento: {bonus:.2f}>
          <salário atual: {salario:.2f}>
          <novo salário: {novo_salario:.2f}>
        """
    elif salario > 400 and salario <= 700:
        bonus = salario * 12/100
        novo_salario = salario + bonus
        result = f"""
          {nome_funcionario} <% de aumento: {bonus:.2f}>
          <salário atual: {salario:.2f}>
          <novo salário: {novo_salario:.2f}>
        """
    elif salario > 0 and salario <= 400:
        bonus = salario * 15/100
        novo_salario = salario + bonus
        result = f"""
          {nome_funcionario} <% de aumento: {bonus:.2f}>
          <salário atual: {salario:.2f}>
          <novo salário: {novo_salario:.2f}>
        """
    else:
        result = "Faixa salarial não analisada para aumento."

    return result
