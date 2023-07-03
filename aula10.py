nome = 'Marcos Felipe'
altura = 1.75
peso = 65
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(nome, 'tem', altura, 'de altura',)
print('pesa', peso, 'quilos e seu imc é',)
print(imc)


