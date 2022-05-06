from time import sleep
from ex115 import dados

cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'destaque': '\033[1;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}
limp = cores['limpar']
verm = cores['vermelho']
dest = cores['destaque']
verd = cores['verde']
amar = cores['amarelo']
azul = cores['azul']

while True:
    sleep(1)
    dados.titulo('MENU PRINCIPAL')
    print(f'''{amar}1{limp} - {azul}Ver pessoas cadastradas
{amar}2{limp} - {azul}Cadastrar nova Pessoa
{amar}3{limp} - {azul}Sair do Sistema{limp}''')
    print('-' * 40)
    while True:
        try:
            opc = int(input(f'{verd}Sua opção:{limp} '))
        except:
            print(f'{dest}ERRO:{verm} por favor, digite um número inteiro válido.{limp}')
        else:
            break
    if opc < 1 or opc > 3:
        print(f'{dest}ERRO!{verm} Digite uma opção válida!{limp}')
    elif opc == 1:
        dados.titulo('PESSOAS CADASTRADAS')
        # Mostrar linha por linha com nome e idade
        arquivo = open('dados/cadastro')
        linhas = arquivo.readlines()
        for linha in linhas:
            print(f'{linha}', end='')
    elif opc == 2:
        dados.titulo('NOVO CADASTRO')
        nome = str(input('Nome: '))
        while True:
            try:
                idade = int(input('Idade: '))
            except:
                print(f'{dest}ERRO:{verm} por favor, digite um número inteiro válido.{limp}')
            else:
                print(f'Novo registro de {nome} adicionado.')
                break
        # Adicionar uma pessoa pessoa no cadastro
        dados.adicionar(nome, idade)
    else:
        # Sair do Sistema
        dados.titulo('Saindo do sistema... Até logo!')
        break
