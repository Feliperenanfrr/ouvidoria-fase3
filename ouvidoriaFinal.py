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

def quantidadeManifestacoes(conexao):
    """
            O count gera uma tupla com a quantidade de elementos do que foi selecionado
            por isso a é utilizado a variável 'quantidadeX[0][0]', que é apenas o recorte
            do numero representando a quantidade
            """
    consultaListagem = 'select * from ocorrencias'
    ouvidoria = listarBancoDados(conexao, consultaListagem)

    if len(ouvidoria) != 0:
        consultaContador = 'select count(*) from ocorrencias'
        quantidadeGeral = listarBancoDados(conexao, consultaContador)

        consultaReclamacao = "select count(*) from ocorrencias where tipo = 1 "
        quantidadeReclamacao = listarBancoDados(conexao, consultaReclamacao)

        consultaSugestao = "select count(*) from ocorrencias where tipo = 2"
        quantidadeSugestao = listarBancoDados(conexao, consultaSugestao)

        consultaElogio = "select count(*) from ocorrencias where tipo = 3 "
        quantidadeElogio = listarBancoDados(conexao, consultaElogio)

        return (f'Quantidade de manifestações: {quantidadeGeral[0][0]}\n'
               f'Quantidade de reclamações: {quantidadeReclamacao[0][0]}\n'
               f'Quantidade de sugestões: {quantidadeSugestao[0][0]}\n'
               f'Quantidade de elogios: {quantidadeElogio[0][0]}\n')

    else:
        return 'Não Há manifestação'


def pesquisaID(conexao, id):

    consultaID = f"select * from ocorrencias where ID = '{id}' "
    ouvidoria = listarBancoDados(conexao, consultaID)

    if len(ouvidoria) != 0:
        for item in ouvidoria:
            return (f'ID: {item[0]} - TIPO: {item[1]} - TÍTULO: {item[2]} - DESCRIÇÃO: {item[3]} - AUTOR: {item[4]}')

    else:
        return 'Não há manifestações com esse ID'


def modificarManifestacao(conexao, id):

    consultaID = f"select * from ocorrencias where ID = '{id}' "
    ouvidoria = listarBancoDados(conexao, consultaID)

    if len(ouvidoria) != 0:

        novoTitulo = input('Digite o novo titulo da manifestação: ')
        novaDescricao = input('Digite a nova descrição da manifestação: ')
        sqlAtualizar = f"update ocorrencias set titulo = %s, descricao = %s  where ID = {id}"
        valores = (novoTitulo, novaDescricao)

        atualizarBancoDados(conexao, sqlAtualizar, valores)
        return'Manifestação modificada com sucesso'
    else:
        return 'Não há Manifestação com este ID para ser modificado\nTente novamente'