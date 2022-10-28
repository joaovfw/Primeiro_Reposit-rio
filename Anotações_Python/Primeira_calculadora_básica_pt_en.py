# Criando uma calculadora com o comando while
# Eu sou foda criei de primeira
# OBS: Falta colocar os erros para quando o operador é diferente das opções porem ainda não consegui.

while True:
    num_1 = input('Digite um número ')
    num_2 = input('Digite um outro número ')
    operador = input('Digite um operador ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Favor digitar um número')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)
    operador = str(operador)

    if operador == '+':
        print(f'A soma é {num_1 + num_2}')
        break
    elif operador == '-':
        print(f'A subtração é {num_1 - num_2}')
        break
    elif operador == '*':
        print(f'O produto é {num_1 * num_2}')
        break
    elif operador == '/':
        print(f'A divisão é {num_1 / num_2}')
        break

while True:
    sair = input('Deseja sair ? [s] para sim e [n] para não ')
    if sair == 's':
        break
    num_1 = input('Digite um número ')
    num_2 = input('Digite um outro número ')
    operador = input('Digite um operador ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Favor digitar um número')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)
    operador = str(operador)

    if operador == '+':
        print(f'The sum is {num_1 + num_2}')
    elif operador == '-':
        print(f'The subtract is {num_1 - num_2}')
    elif operador == '*':
        print(f'The prouduct is {num_1 * num_2}')
    elif operador == '/':
        print(f'The division is {num_1 / num_2}')
    else:
        print('Operador inválido!')
print('Até logo!')

#  if not operador == '+' or not operador == '-' or not operador == '*':
#  print('Favor digitar um operador válido')'''
