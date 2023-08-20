"""
Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 
"""

# print('Bem-vindo a Calculadora Avancada em Python!')

# escolha_operacao = 1 # 1: Repetir e 0: Parar

# def calculadora (n1, n2, operacao):
#     if operacao == 1: return n1+n2 # Adicao
#     elif operacao == 2: return n1-n2 # Subtracao
#     elif operacao == 3: return n1*n2 # Multiplicacao
#     else: return n1/n2 # Divisao

# while (escolha_operacao != 0):
#     escolha_operacao =  int(input('Para comecar, escolha uma operacao: \r\n(0) Sair \r\n(1) Adicao\r\n(2) Subtracao\r\n(3) Multiplicacao\r\n(4) Divisao\r\n'))
#     if escolha_operacao == 0: # Sai do sistema
#         print('Voce saira do sistema.')
#         break
#     elif escolha_operacao in [1,2,3,4]:
#         numero1 = float(input('Digite o numero 1: '))
#         numero2 = float(input('Digite o numero 2: '))
#         resultado = calculadora(numero1,numero2, escolha_operacao)
#         print(f'Resultado: {resultado}\r\n')
#     else:
#         print('Essa opção não existe.')
    
print('Bem-vindo a Calculadora Avancada em Python!')

escolha_operacao = 1 # 1: Repetir e 0: Parar

def calculadora (n1, n2, operacao):
    if operacao == 1: return n1+n2 # Adicao
    elif operacao == 2: return n1-n2 # Subtracao
    elif operacao == 3: return n1*n2 # Multiplicacao
    else: return n1/n2 # Divisao



while (escolha_operacao != 0):
    escolha_operacao =  int(input('Para comecar, escolha uma operacao: \r\n(0) Sair \r\n(1) Adicao\r\n(2) Subtracao\r\n(3) Multiplicacao\r\n(4) Divisao\r\n'))
    
    if escolha_operacao == 0: # Sai do sistema
        print('Voce saira do sistema.')
        break
    elif escolha_operacao > 4 or escolha_operacao < 0:
        print('Essa opção não existe')
    else:
        numero1 = float(input('Digite o numero 1: '))
        numero2 = float(input('Digite o numero 2: '))
