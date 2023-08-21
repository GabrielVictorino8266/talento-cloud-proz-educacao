"""
Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

Resolucao (Etapas)

1. Listar as variaives
2. Funcao para calcular a idade
"""
#Definicao de variaveis

nome = ''
idade = 0
repetir = True

def calcular_idade (ano_nascimento):
    idade = 2022 - ano_nascimento
    return idade

while(repetir):

    try:    
        nome = str(input('informe seu nome: '))
        ano_nascimento = int(input('informe seu ano de nascimento: '))

        if ano_nascimento < 1922 or ano_nascimento > 2021:
            raise Exception('Fora de Intervalo')
        else:
            repetir = False # Nao ira repetir

            print(f'Seu nome é {nome} e sua idade {calcular_idade(ano_nascimento)}')

    except Exception as err:
        print("Houve um erro, tente novamente.", err)        
