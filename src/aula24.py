# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  A l e x A n
# -6-5-4-3-2-1

nome = 'AlexAn'
# print(nome[2])
# print(nome[-4])
print('xAn' in nome)
print('z' in nome)

print(10 * '-')

print('xAn' not in nome)
print('z' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar? ')


if encontrar in nome:
    print(f'{encontrar} está em {nome}')

else:
    print(f'{encontrar} não está em {nome}')
    