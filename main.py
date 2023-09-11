from exercicio_1.resolucao_1 import calcular_area_circulo
from exercicio_2.resolucao_2 import calcular_area_trapezio_quadrado_cubo
from exercicio_3.resolucao_3 import calcular_volume_caixa_d_agua
from exercicio_4.resolucao_4 import calcular_salario_vendedor
from exercicio_5.resolucao_5 import calcular_velocidade_media
from exercicio_6.resolucao_6 import verficar_numero_par_ou_impar
from exercicio_7.resolucao_7 import verificar_financiamento
from exercicio_8.resolucao_8 import verificar_conceito_aluno
from exercicio_9.resolucao_9 import conceder_aumento_salarial


def main():
    menu = """
      Temos 9 questões resolvidas disponíveis para você!!!
      Para executar o código de determinada questão é simples!
      Basta informar o número da questão 1..9, beleza?

      Se quiser sair do sistema, informe a letra 's' que vamos
      encerrar a execução!

      Seja bem-vindo(a) ao AlgoritmoEstudar!
    """

    print(menu)
    status_system = True

    while status_system:
        resposta_user = input(
          "Informe o número da questão ou digite 's' para sair do sistema: "
        )
        if resposta_user == "1":
            print(calcular_area_circulo())
        elif resposta_user == "2":
            print(calcular_area_trapezio_quadrado_cubo())
        elif resposta_user == "3":
            print(calcular_volume_caixa_d_agua())
        elif resposta_user == "4":
            print(calcular_salario_vendedor())
        elif resposta_user == "5":
            print(calcular_velocidade_media())
        elif resposta_user == "6":
            print(verficar_numero_par_ou_impar())
        elif resposta_user == "7":
            print(verificar_financiamento())
        elif resposta_user == "8":
            print(verificar_conceito_aluno())
        elif resposta_user == "9":
            print(conceder_aumento_salarial())
        elif resposta_user.lower() == "s":
            status_system = False
            print("Obrigado por usar o sistema! Volte sempre!")
        else:
            status_system = False
            print("Opção inválida, encerramos o sistema.")


main()
