"""
Iterando strings com while
"""     
# #       012345678910
nome = 'Alex Antonio' # Iteráveis
# #      1110987654321
# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)

# print(nome[3])

contador = 0
novo_nome = ''
while contador < len(nome):
    letra = nome[contador]
    novo_nome += f'*{letra}'
    contador += 1

print(f'{novo_nome}*')
