from ex107 import moeda

cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m'
}
limpar = cores['limpar']
vermelho = cores['vermelho']
verde = cores['verde']
amarelo = cores['amarelo']

p = float(input(f'Digite o preço: {amarelo}R${limpar}'))
print(f'A metade de {p} é {vermelho}{moeda.metade(p)}{limpar}')
print(f'O dobro de {p} é {verde}{moeda.dobro(p)}{limpar}')
print(f'Reduzindo 13%, temos {vermelho}{moeda.diminuir(p, 13)}{limpar}')
print(f'Aumentando 10%, temos {verde}{moeda.aumentar(p, 10)}{limpar}')

# Solução Gustavo Guanabara

'''from ex107 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10)}')'''
