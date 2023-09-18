nome = 'Alex Antonio'
altura = 1.69
peso = 76
imc = ...

# Alex Antonio tem 1.69 de altura,
# pesa 76 kilos e seu IMC é 
# 26.61

#f-strings
imc = f'{peso / altura ** 2:.2f}'

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} kilos e seu IMC é'
print(linha_1)
print(linha_2)
print(imc)

