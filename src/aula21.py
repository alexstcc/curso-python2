# Operadores Lógicos
# and (e) or (ou) not (não)
# and - todas as condições precisam ter
# verdadeiras
# Se qualquer valor for considerado falso,
# a expressaõ inteira será avaliada naquele valor
# São considerados falsy (que vd já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

"""
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entar')
else:
    print('Sair')
"""
print(True and False and True)
print(True and 0 and True)