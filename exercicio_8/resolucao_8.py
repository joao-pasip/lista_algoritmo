# Exercício 08: Faça um algoritmo que solicite a nota de um aluno
# (somente valores inteiros e positivos). O critério para conceitos
# é o seguinte:

# notas inferiores a 3 -> conceito E
# notas de 3 a 5 -> conceito D
# notas de 6 e 7 -> conceito C
# notas de 8 e 9 -> conceito B
# nota 10 -> conceito A


def verificar_conceito_aluno():
    nota_aluno = int(
        input("Informe a sua nota(somente valores positivos e inteiros): ")
    )

    if nota_aluno < 0:
        result = "Nota negativa, informe apenas valores positivos e inteiros."
    elif not isinstance(nota_aluno, int):
        result = "Nota não inteira, aceita-se só valores positivos e inteiros."
    else:
        if nota_aluno < 3:
            result = "conceito E"
        elif nota_aluno >= 3 and nota_aluno <= 5:
            result = "conceito D"
        elif nota_aluno == 6 or nota_aluno == 7:
            result = "conceito C"
        elif nota_aluno == 8 or nota_aluno == 9:
            result = "conceito B"
        elif nota_aluno == 10:
            result = "conceito A"
        else:
            result = """
              Nota informada sem conceito.
              Apenas notas entre 1 - 10 avaliadas.
            """
    return result
