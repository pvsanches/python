cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m',
    'cinza': '\033[0;37m'
}
li = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']
az = cores['azul']
cz = cores['cinza']

# Minha segunda solução
'''
from random import randint
computador = randint(0, 10)
print(f'{az}=-{li}'*15)
print(f'{am}VAMOS JOGAR PAR OU ÍMPAR{li}')
print(f'{az}=-{li}'*15)
vitoria = 0
while True:
    valor = int(input('Diga um valor: '))
    pi = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    while pi != 'P' and pi != 'I':
        pi = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    tot = valor + computador
    if tot % 2 == 0:
        deu = 'PAR'
    elif tot % 2 == 1:
        deu = 'ÍMPAR'
    print(f'-' * 30)
    print(f'Você jogou {valor} e o computador {computador}. Total de {cz}{tot}{li} DEU {am}{deu}{li}')
    print(f'-'*30)
    if tot % 2 == 0 and pi in 'Pp' or tot % 2 == 1 and pi in 'Ii':
        print(f'{vd}Você VENCEU!{li}')
        print('Vamos jogar novamente...')
        vitoria += 1
    else:
        print(f'{vm}Você PERDEU!{li}')
        perdeu = True
        print(f'{az}=-{li}' * 15)
        break
    print(f'{az}=-{li}' * 15)
if vitoria > 1 or vitoria == 0:
    print(f'GAME OVER! Você venceu {am}{vitoria}{li} vezes.')
else:
    print(f'GAME OVER! Você venceu {am}{vitoria}{li} vez.')
'''

# Minha solução
'''
from random import randint
computador = randint(0, 10)
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
vitoria = 0
deu = ''
perdeu = False
while True:
    valor = int(input('Digite um valor: '))
    pi = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('-'*30)
    tot = valor + computador
    if tot % 2 == 0:
        # PAR
        deu = 'PAR'
        if pi == 'P':
            # Se o jogador VENCEU
            resultado = 'Você VENCEU! \nVamos jogar novamente...'
            vitoria += 1
        else:
            # Se o jogador PERDEU
            resultado = 'Você PERDEU!'
            perdeu = True
    else:
        # ÍMPAR
        deu = 'ÍMPAR'
        if pi == 'I':
            # Se o jogador VENCEU
            resultado = 'Você VENCEU! \nVamos jogar novamente...'
            vitoria += 1
        else:
            # Se o jogador PERDEU
            resultado = 'Você PERDEU!'
            perdeu = True
    print(f'Você jogou {valor} e o computador {computador}. Total de {tot} DEU {deu}')
    print('-'*30)
    print(resultado)
    print('=-'*15)
    if perdeu == True:
        break
print(f'GAME OVER! Você venceu {vitoria} vezes.')
'''

# Solução Gustavo Guanabara
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
