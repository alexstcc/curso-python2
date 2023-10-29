"""
Exercicio
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é letra {letra}
Se nada for digitado em nome ou idade:
    exiba, "Desculpe, você deixou campos vazios."
"""

nome = input('Por favor informe seu nome: ')
idade = input('Por favor informe sua idade: ')

if (nome ) != '' and (idade) != '':
    print(f'Seu nome é {nome}')
    print('Seu nome invertido é ')
    print(nome[-1:-len(nome)-1:-1])
    if ' ' in nome:
        print('Seu nome contém espaços.')
    else:
        print('Seu nome não contém espaços.')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é a letra {nome[-1]}')

    print(idade)
else:
    print('Desculpe, você deixou campos vazios.')