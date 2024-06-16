from bancodados_hospital import *

con = criar_conexao('localhost', 'root', 'root')

def add_paciente():
   
    CPF      = input("Digite o CPF do paciente:")
    nome     = input("Digite o nome do paciente:")
    idade    = input("Digite a idade do paciente:")
    endereco = input("Digite o endereco do paciente:")
    telefone = input("Digite o telefone do paciente:")
    
    if not CPF or not nome or not idade or not endereco or not telefone:
        return "Por favor, preencha todos os campos"
    
    sql = "INSERT INTO TABLE PACIENTE(CPF, nome, idade, endereco, telefone) VALUES (%s, %s, %s, %s, %s )" 
    dados = (CPF, nome, idade, endereco, telefone)
    
    return insert_naTabela(con, sql, dados)
    
def add_medico(): 
   
    nome          = input("Digite o nome do médico:")
    especialidade = input("Digite a especialidade do médico:")
    CRM           = input("Digite o CRM do médico:")
    telefone      = input("Digite o telefone do médico:")    
    if not nome or not especialidade or not CRM or not telefone:
        return "Por favor, preencha todos os campos"
    
    sql = "INSERT INTO TABLE PACIENTE(CRM, nome, especialidade, telefone) VALUES (%s, %s, %s, %s )"
    dados = (CRM, nome, especialidade, telefone)
    
    return insert_naTabela(con, sql, dados)
    
def pesquisar_paciente():
    pesquisaCPF = input ("Digite o CPF do paciente que deseja consultar:")
    
    if not pesquisaCPF:
        return "Preencha o campo corretamente"
    
    else:
        sql = "SELECT * FROM PACIENTE WHERE CPF = %s"
        return listar_umDeTabela (con, sql, pesquisaCPF)

def pesquisar_medico():
    pesquisaCRM = input ("Digite o CRM do medico que deseja consultar:")
    
    if not pesquisaCRM:
        return "Preencha o campo corretamente"
    
    else: 
        sql = "SELECT * FROM MEDICO WHERE CRM = %s"
        return listar_umDeTabela (con, sql, pesquisaCRM)

def excluir_paciente():
    excluirCPF = input("Digite o CPF que deseja excluir:")
    
    if not excluirCPF:
        return "Preencha o campo corretamente"
    
    else: 
        sql = "SELECT * FROM PACIENTE WHERE CPF = %s"
        return excluir_dadosTabela (con, sql, excluirCPF)

def excluir_medico():
    excluirCRM = input("Digite o CRM que deseja excluir:")
    
    if not excluirCRM:
        return "Preencha o campo corretamente"
    
    else:
        sql = "SELECT * FROM MEDICO WHERE CRM = %s"
        return excluir_dadosTabela (con, sql, excluirCRM)

def adicionar_consulta():
    pesquisarCPF = input ("Digite o CPF do paciente para agendar a consulta: ")
    horario      = input ("Digite o horario da consulta")
    tipoConsulta = input ("Digite o tipo de consulta que será feita")
    pesquisarCRM = input ("Digite o CRM do medico que deseja ser atendido: ")
    
    if not pesquisarCPF or not horario or not tipoConsulta or not pesquisarCRM:
        return "Preencha todos os campos corretamente!"
    
    sql = "INSERT INTO CONSULTA (CPF ,horario, tipo_consulta, CRM) VALUES (%s, %s, %s, %s);"
    dados = (pesquisarCPF, horario, tipoConsulta, pesquisarCRM)
    
    return insert_naTabela(con, sql, dados)
    
def visualizar_consulta():
    pesquisarId = input ("Digite o ID da consulta: ")
    
    if not pesquisarId:
        return "Preencha o campo corretamente"
    
    sql = "SELECT * FROM CONSULTA WHERE ID = %s"
    
    return listar_umDeTabela(con, sql, pesquisarId)

def cancelar_consulta():
    pesquisarId = input ("Digite o ID da consulta que será cancelada: ")
    
    if not pesquisarId:
        return "Preencha o campo corretamente"
    
    sql = "SELECT * FROM CONSULTA WHERE ID = %s"
    
    return excluir_dadosTabela(con, sql, pesquisarId)

def adicionar_procedimento():
    pesquisarCRM          = input ("Digite o CRM do medico que vai realizar o procedimento: ")
    pesquisarCPF          = input ("Digite o CPF do paciente: ")
    procedimentoMedico    = input ("Descreva o procedimento realizado: ")
    
    if not pesquisarCRM or not pesquisarCPF or not procedimentoMedico:
        return "Preencha o campo corretamente"
    
    sql = "INSERT INTO PROCEDIMENTO (CRM, PROCEDIMENTO_MEDICO) VALUES (%s, %s)"
    dados = (pesquisarCRM, procedimentoMedico, pesquisarCPF)
    
    return insert_naTabela(con, sql, dados)

def visualizar_procedimento():
    pesquisarId = input ("Digite o ID do procedimento: ")
    
    if not pesquisarId:
        return "Preencha o campo corretamente"
    
    sql = "SELECT * FROM PROCEDIMENTO WHERE ID = %s"
    
    return listar_umDeTabela(con, sql, pesquisarId)

def reload():
    sqlPaciente = """
    CREATE TABLE IF NOT EXISTS PACIENTE (
    CPF varchar(14) primary key,
    NOME varchar(80), 
    IDADE int, 
    ENDERECO varchar(100), 
    TELEFONE int
    )"""
    print(criar_tabela(con, sqlPaciente, "hospital"))

    sqlMedico = """
    CREATE TABLE IF NOT EXISTS MEDICO (
    CRM varchar(4) primary key,
    nome varchar(80),
    especialidade varchar(50),
    telefone int 
    )"""
    print(criar_tabela(con, sqlMedico, "hospital"))

    sqlConsulta = """
    CREATE TABLE IF NOT EXISTS CONSULTA(
    id int auto_increment primary key,
    CPF varchar(14),
    CRM varchar(4),
    horario varchar(5),
    tipo_consulta varchar(80),
    FOREIGN KEY CPF REFERENCES PACIENTE(CPF),
    FOREIGN KEY CRM REFERENCES MEDICO(CRM)
    )"""
    print(criar_tabela(con, sqlConsulta, "hospital"))

    sqlProcedimento = """
    CREATE TABLE IF NOT EXISTS PROCEDIMENTO (
    ID int auto_increment primary key,
    CPF varchar(14),
    CRM varchar(4),
    PROCEDIMENTO_MEDICO varchar(80),
    FOREIGN KEY CPF REFERENCES PACIENTE(CPF),
    FOREIGN KEY CRM REFERENCES MEDICO(CRM) 
    )"""
    print(criar_tabela(con, sqlProcedimento, "hospital"))
    
finalizar_conexao(con)

    