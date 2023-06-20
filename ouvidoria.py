from operacoesbd import *

def titulos(texto):
    print('-' * 60)
    print(f'{texto:^60}')
    print('-' * 60)

def listarManifestacoes(conexao):
    consultaListagem = 'select * from ocorrencias'
    ouvidoria = listarBancoDados(conexao, consultaListagem)

    if len(ouvidoria) != 0:
        for item in ouvidoria:
            if item[1] == 1:
                print('ID', item[0], ' - Titulo:', item[2], '- Autor:', item[4], '-', 'Reclamação')
            elif item[1] == 2:
                print('ID', item[0], '- Titulo:', item[2], '- Autor:', item[4], '-', 'Sugestão')
            elif item[1] == 3:
                print('ID', item[0], '- Titulo:', item[2], '- Autor:', item[4], '-', 'Elogio')
    else:
        print('Não há manifestações cadastradas')

def listarPorTipo(conexao):
    print('Qual tipo de manifestação que quer visualizar\n1 - Reclamação\n2 - Sugestão\n3 - Elogio')
    tipo = int(input('Digite sua opção: '))
    consultaListagem = 'select * from ocorrencias'
    ouvidoria = listarBancoDados(conexao, consultaListagem)

    if len(ouvidoria) != 0:

        if tipo == 1:
            consultaListagem = 'select * from ocorrencias where tipo = 1'
            ouvidoria = listarBancoDados(conexao, consultaListagem)
            if len(ouvidoria) != 0:
                for item in ouvidoria:
                    print('ID', item[0], '- Titulo:', item[1], '- Autor:', item[4])
            else:
                print('Não Há Reclamações')

        elif tipo == 2:
            consultaListagem = 'select * from ocorrencias where tipo = 2'
            ouvidoria = listarBancoDados(conexao, consultaListagem)
            if  len(ouvidoria) != 0:
                for item in ouvidoria:
                    print('ID', item[0], '- Titulo:', item[1], '- Autor:', item[4])
            else:
                print('Não há Sugestões')

        elif tipo == 3:
            consultaListagem = 'select * from ocorrencias where tipo = 3'
            ouvidoria = listarBancoDados(conexao, consultaListagem)
            if len(ouvidoria) != 0:
                for item in ouvidoria:
                    print('ID', item[0], '- Titulo:', item[1], '- Autor:', item[4])
            else:
                print('Não há Elogios')
        else:
            print('Opção invalida')
    else:
        print("Não há Manifestações")

def criarManifestacao(conexao):
    print('1 - Reclamação\n2 - Sugestão\n3 - Elogio')
    tipo = int(input('Digite sua opção: '))

    if tipo == 1:
        titulo = input('digite o titulo da sua reclamação: ')
        descricao = input('Descreva sua reclamação: ')
        nome = input('Digite seu nome: ')

        sqlInsercao = 'insert into ocorrencias (tipo,titulo,descricao,autor) values(%s,%s,%s,%s)'
        valores = (tipo, titulo, descricao, nome)
        insertNoBancoDados(conexao, sqlInsercao, valores)

        print('Manifestação criada com sucesso')

    elif tipo == 2:
        titulo = input('digite o titulo da sua sugestão: ')
        descricao = input('Descreva sua sugestão: ')
        nome = input('Digite seu nome: ')

        sqlInsercao = 'insert into ocorrencias (tipo,titulo,descricao,autor) values(%s,%s,%s,%s)'
        valores = (tipo, titulo, descricao, nome)
        insertNoBancoDados(conexao, sqlInsercao, valores)

        print('Manifestação criada com sucesso')

    elif tipo == 3:
        titulo = input('digite o titulo do seu elogio: ')
        descricao = input('Descreva seu elogio: ')
        nome = input('Digite seu nome: ')

        sqlInsercao = 'insert into ocorrencias (tipo,titulo,descricao,autor) values(%s,%s,%s,%s)'
        valores = (tipo, titulo, descricao, nome)
        insertNoBancoDados(conexao, sqlInsercao, valores)

        print('Manifestação criada com sucesso')

    else:
        print('Solicitação invalida')