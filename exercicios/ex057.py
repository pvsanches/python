cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'azul': '\033[0;34m',
    'roxo': '\033[0;35m'
}
l = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
az = cores['azul']
rx = cores['roxo']

# Minha solução
s = str(input('Informe o seu sexo: [M/F] ')).upper()
while s != 'M' and s != 'F':
    s = str(input(f'{vm}Dados inválidos.{l} Por favor, informe seu sexo: ')).upper()
if s == 'M':
    print(f'Sexo {az}{s}{l} registrado com {vd}sucesso{l}')
else:
    print(f'Sexo {rx}{s}{l} registrado com {vd}sucesso{l}')
