"""
Faça um programa que peça ao usuário para digitar
um número inteiro, informe se este número é par ou impar.
Caso o usuário não digite um número inteiro,
informe que não é um número inteiro.
"""
# numero_inteiro = ""

# try:
#     numero_inteiro = int(input('Digite um numero inteiro: '))

#     #print(type(numero_inteiro))

#     if type(numero_inteiro) == int:
#         par_ou_impar = int(numero_inteiro) % 2

#         if par_ou_impar == 0:
#             print(f'{numero_inteiro} é par.')
#         elif par_ou_impar > 0:
#             print(f'{numero_inteiro} é impar')    
# except:
#     #print(TypeError('não é numero inteiro'))
#     print(f'Valor digitado não é numero inteiro')

"""
Faça um programa que pergunte a hora ao usuário e,
baseando-se no horário descrito, exiba a saudação apropriada.
Ex. Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

#hora_informada = input('Informe a hora: ')

# try:
#     hora = int(hora_informada)
    
#     if hora_informada >=0 and hora_informada <=11:
#         print(f'Bom dia!')
#     elif hora_informada >11 and hora_informada <=17:
#         print(f'Boa tarde!')
#     elif hora_informada >17 and hora_informada <24:
#         print('Boa noite!')
#     else:
#         print('Hora não reconhecida')
# except:
#     print('Digite somente horas inteiras')

"""
Faça um programa que peça o primeiro nome do
usuário. Se o nome tiver 4 letras ou menos
escreva "Seu nome é curto"; se tiver entre 5 ou 6 letras,
escreva "Seu nome é normal"; maior que 6 escreva "Seu nome 
é muito grande".
"""
# primeiro_nome = input('Informe o primeiro nome: ')
# tamanho_nome = len(primeiro_nome)

# if tamanho_nome > 1:
#     if tamanho_nome <= 4:
#         print('Seu nome é curto')
#     elif tamanho_nome > 4 and tamanho_nome <= 6:
#         print('Seu nome é normal')
#     else:
#         print('Seu nome é muito grande')
# else:
#     print('A informação do nome é obrigatória')