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