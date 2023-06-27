"""
Programação em linguagem estruturada
FASE 2
Alunos:
    Matheus Pinto Clemente - RA: 2313080132
    Felipe Renan dos Santos Ferreira - RA: 2313080103
    Mateus Patricio Vasconcelos - RA: 2313080094
    Wilami Ferreira de Pontes - RA: 2313080119
    Luan Rodrigo Ribeiro de Souza - RA: 2313080078
"""

from operacoesbd import *
from ouvidoriaFinal import *

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
        manifestacoes = listarManifestacoes(conexao)
        for manifestacao in manifestacoes:
            print(manifestacao)


    elif opcao == 2:
        print('LISTAGEM POR MANIFESTAÇÃO')
        print('Qual tipo de manifestação que quer visualizar\n1 - Reclamação\n2 - Sugestão\n3 - Elogio')
        tipo = int(input('Digite sua opção: '))
        manifestacoes_tipo = listarPorTipo(conexao, tipo)
        for manifestacao in manifestacoes_tipo:
            print(manifestacao)


    elif opcao == 3:
        print('CRIAR MANIFESTAÇÃO')
        print('1 - Reclamação\n2 - Sugestão\n3 - Elogio')
        tipo = int(input('Digite sua opção: '))
        titulo = input('Digite o título da sua manifestação: ')
        descricao = input('Descreva sua manifestação: ')
        autor = input('Digite seu nome: ')
        criado = criarManifestacao(conexao, tipo, titulo, descricao, autor)
        print(criado)

    elif opcao == 4:
        titulos('QUANTIDADE DE MANIFESTAÇÕES')
        quantidade = quantidadeManifestacoes(conexao)
        print(quantidade)

    elif opcao == 5:
        titulos('PESQUISAR POR ID')
        id = int(input('Digite o ID da Manifestação: '))
        pesquisa = pesquisaID(conexao, id)
        print(pesquisa)

    elif opcao == 6:
        titulos('MODIFICANDO MANIFESTAÇÕES')
        id = int(input('Digite o ID da Manifestação: '))
        modificado = modificarManifestacao(conexao,id)
        print(modificado)