"""
Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.
"""

def calculadora (numero1, numero2, operacao):
    if operacao == 1: return numero1+numero2 # Soma
    elif operacao == 2: return numero1-numero2 # Subtracao
    elif operacao == 3: return numero1*numero2 # Multiplicacao
    elif operacao==4: return numero1/numero2 # Divisao
    else:
        return 'Nao existe essa operacao'

print(calculadora(1,2,1))
# expected output: 3