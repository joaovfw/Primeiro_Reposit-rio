usuario = input(' Digite seu nome: ')
qtde_caracteres = len(usuario)
print(usuario, qtde_caracteres, type(qtde_caracteres))

num_1 = input('digite um numero ')

if num_1.isdigit():
    num_1 = int(num_1)
    if num_1 % 2 == 0:
        print('Esse é um número par')
    else:
        print('Esse é um número impar')
else:
    print('esse não é um número inteiro')

num_2 = 15
num_3 = 7
divisao = num_2 / num_3
print(f'{divisao:.2f}')