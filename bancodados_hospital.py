import mysql.connector
from mysql.connector import errorcode

def criar_conexao(endereco, usuario, senha, banco):
    return mysql.connector.connect(
        host = endereco,
        username = usuario,
        password = senha,
        database = banco
    )

def finalizar_conexao(conexao):
    conexao.close()

def criar_bancoDeDados(conexao, sql):
    cursor = conexao.cursor()
    cursor.execute(sql)
    cursor.close()

def criar_tabela(conexao, sql, nome_banco):
    try:
        cursor = conexao.cursor()
        cursor.execute(f"USE {nome_banco}")
        cursor.execute(sql)
        cursor.close()
        return "Banco de dados criado com sucesso!"

    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            return "Erro: Banco de dados inexistente!"
        else:
            return f"Error! {error}"

def listar_tabelas(conexao, sql):
        cursor = conexao.cursor()
        cursor.execute(sql)
        tabelas = conexao.fetchall()
        cursor.close()
        return tabelas
    
def insert_naTabela(conexao, sql, dados):
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, dados)
        conexao.commit()
        cursor.close()
        return "Dados adicionados com sucesso!"
    
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_NO_SUCH_TABLE:
            return "Erro: A tabela não existe."
        else: 
            return f"Erro ao inserir dados: {error}"

def listar_umDeTabela(conexao, sql, id):
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, (id,))
        tabelaUnica = cursor.fetchone()
        cursor.close()
        if tabelaUnica is None:
            return "Dados não encontrados!"
        else:
            return tabelaUnica
    
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_NO_SUCH_TABLE:
            return "Erro: A tabela não existe."
        elif error.errno == errorcode.ER_BAD_FIELD_ERROR:
           return "Erro: Buscagem não encontrada."
        else:
            return f"Erro ao buscar dados: {error}"


def listar_bancoDeDados(conexao, sql):
    cursor = conexao.cursor()
    cursor.execute(sql)
    bancoDados = cursor.fetchall()
    cursor.close()
    return bancoDados

def atualizar_bancoDeDados(conexao, sql, dados):
    cursor = conexao.cursor()
    cursor.execute(sql, dados)
    conexao.commit()
    cursor.close()

def excluir_dadosTabela(conexao, sql, dados):
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, (dados,))
        conexao.commit()
        cursor.close()
        return "Dados excluido com sucesso!"

    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_FIELD_ERROR:
            return "Erro: dados não encontrado!"
        else:
            return f"Erro ao encontrar dados: {error}"


def excluir_bancoDados(conexao, nome_banco):
    cursor = conexao.cursor()
    cursor.execute(f"DROP DATABASE {nome_banco}")
    conexao.commit()
    cursor.close()

def excluir_tabela(conexao, nome_tabela):
    cursor = conexao.cursor()
    cursor.execute(f"DROP TABLE {nome_tabela}")
    conexao.commit()
    cursor.close()







