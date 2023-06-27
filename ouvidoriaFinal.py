from operacoesbd import *

def titulos(texto):
    print('-' * 60)
    print(f'{texto:^60}')
    print('-' * 60)

def listarManifestacoes(conexao):
    consultaListagem = 'select * from ocorrencias'
    ouvidoria = listarBancoDados(conexao, consultaListagem)

    if len(ouvidoria) != 0:
        manifestacoes = []
        for item in ouvidoria:
            tipo = ""
            if item[1] == 1:
                tipo = "Reclamação"
            elif item[1] == 2:
                tipo = "Sugestão"
            elif item[1] == 3:
                tipo = "Elogio"
            manifestacoes.append(f'ID {item[0]} - Título: {item[2]} - Autor: {item[4]} - {tipo}')
        return manifestacoes
    else:
        return 'Não há manifestações cadastradas'



def listarPorTipo(conexao,tipo):
    consultaListagem = f'SELECT * FROM ocorrencias WHERE tipo = {tipo}'
    ouvidoria = listarBancoDados(conexao, consultaListagem)

    if len(ouvidoria) != 0:
        manifestacoes = []
        for item in ouvidoria:
            manifestacoes.append(f'ID {item[0]} - Título: {item[2]} - Autor: {item[4]}')
        return manifestacoes
    else:
        return 'Não há manifestações desse tipo'


def criarManifestacao(conexao,tipo, titulo, descricao, autor):
    sqlInsercao = 'INSERT INTO ocorrencias (tipo, titulo, descricao, autor) VALUES (%s, %s, %s, %s)'
    valores = (tipo, titulo, descricao, autor)
    insertNoBancoDados(conexao, sqlInsercao, valores)

    return 'Manifestação criada com sucesso'