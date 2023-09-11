# Exercício 06: Faça um algoritmo que leia um número inteiro.
# Se o número lido for positivo, escreva uma mensagem indicando
# se ele é par ou ímpar. Se o número for negativo, escreva
# a seguinte mensagem “Este número não é positivo”.

def verficar_numero_par_ou_impar():
    numero = int(input("Digite um número, para saber se é impar ou par: "))
    verify = f"{numero} é par." if numero % 2 == 0 else f"{numero} é ímpar."
    if numero < 0:
        par_impar = "Este número não é positivo"
    else:
        par_impar = verify
    return par_impar
