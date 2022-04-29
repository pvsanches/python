cores = {
    'limpar': '\033[m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}
li = cores['limpar']
am = cores['amarelo']
az = cores['azul']

# Minha solução


def área(larg, comp):
    calc = larg * comp
    print(f'A área de um terreno {az}{larg:.1f}{li}x{az}{comp:.1f}{li} é de {am}{calc:.1f}m²{li}.')


# Programa Principal
print(' Controle de Terrenos ')
print('-' * 22)
área(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))

# Solução de Gustavo Guanabara


'''def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')


# Programa principal
print(' Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)'''
