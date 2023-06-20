"""
Programação em linguagem estruturada
FASE 2
Alunos:
    Matheus Pinto Clemente - RA: 2313080132
    Felipe Renan dos Santos Ferreira - RA: 2313080103
    Mateus Patricio Vasconcelos - RA: 2313080094
    Wilami Ferreira de Pontes - RA: 2313080119
    Luan Rodrigo Ribeiro de Souza - RA: 2313080078
    Matheus Henrique Rocha de Almeida - RA: 2313080108
"""

from operacoesbd import *
from ouvidoria import *

conexao = abrirBancoDados('localhost', 'root', 'Mat16062000!', 'ouvidoria1')

print('BEM VINDO À OUVIDORIA')
opcao = 1

while opcao != 0:

    print('[  1  ] Listagem de manifestações')
    print('[  2  ] Listagem de manifestações por tipo')
    print('[  3  ] Criar uma nova manifestação')
    print('[  4  ] Exibir quantidade de manifestações')
    print('[  5  ] Pesquisar manifestação por ID')
    print('[  6  ] Modificar manifestação por ID')
    print('[  7  ] Excluir manifestação pelo ID')
    print('[  0  ] Sair do sistema')
    opcao = int(input('DIGITE SUA OPÇÃO: '))

    if opcao == 1:
        titulos('LISTANDO MANIFESTAÇÕES')
        listarManifestacoes(conexao)

    elif opcao == 2:
        titulos('LISTAGEM POR MANIFESTAÇÃO')
        listarPorTipo(conexao)

    elif opcao == 3:
        titulos('QUAL O TIPO DE MANIFESTAÇÃO QUE DESEJA CRIAR?:\n')
        criarManifestacao(conexao)












encerrarBancoDados(conexao)