cadastro = {'nome': [], 'sexo':[], 'ano':[]}

while True:
    terminar = input('Deseja cadastrar uma pessoa ? [S/N] ')
    if terminar.upper() in 'N':
        break
    if terminar.upper() not in 'S':
        print('digite S para SIM ou N para NÃO')
        continue
    nome = input('Qual o nome? ')
    sexo = input('Qual o sexo? ')
    ano = input('Qual o ano? ')
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)

print(cadastro)

print('\ntotal de cadastro:')
print(len(cadastro['nome']))
idades = []
for ano in cadastro[('ano')]:
    idades.append(2026 - int(ano))
media = sum(idades)/len(idades)
print(f'\nmedia de idade: {media:1f}')

print('\nMulheres com menos de 30 anos: ')
for i in range(len(cadastro['nome'])):
    idade = 2026 - int(cadastro['ano'][i])
    if cadastro['sexo'][i] == 'F' and idade < 30:
        print(f'{cadastro['nome'][i]} - {idade} anos')

print('\nHomens com idade acima da media: ')
for i in range(len(cadastro['nome'])):
    idade = 2026 - int(cadastro['ano'][i])
    if cadastro['sexo'][i] == 'M' and idade > media:
        print(f'{cadastro['nome'][i]} - {idade} anos')