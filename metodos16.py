from bancodados_hospital import *

con = criar_conexao('192.168.0.1', 'root', 'AndreyEloy01')

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
    CRM        = input("Digite o CRM do médico:")
    telefone      = input("Digite o telefone do médico:")    
    if not nome or not especialidade or not CRM or not telefone:
        return "Por favor, preencha todos os campos"
    
    sql = "INSERT INTO TABLE PACIENTE(CRM, nome, especialidade, telefone) VALUES (%s, %s, %s, %s )"
    dados = (CRM, nome, especialidade, telefone)
    
    return insert_naTabela(con, sql, dados)
    
def pesquisar_paciente():
    pesquisaCPF = input ("Digite o CPF do paciente que deseja consultar:")
    
    if not pesquisaCPF:
        return "Digite um CPF valido."
    
    else:
        sql = "SELECT * FROM PACIENTE WHERE CPF = %s"
        return listar_umDeTabela (con, sql, pesquisaCPF)
    
    
   
  

def pesquisar_medico():
    pesquisaCRM = input ("Digite o CRM do medico que deseja consultar:")
    
    if not pesquisaCRM:
        return "Digite um CRM valido."
    
    else: 
        sql = "SELECT * FROM MEDICO WHERE CRM = %s"
        return listar_umDeTabela (con, sql, pesquisaCRM)
    


def excluir_paciente():
    excluirCPF = input("Digite o CPF que deseja excluir:")
    
    if not excluirCPF:
        return "Digite um CPF valido."
    
    else: 
        sql = "SELECT * FROM PACIENTE WHERE CPF = %s"
        return excluir_dadosTabela (con, sql, excluirCPF)

def excluir_medico():
    excluirCRM = input("Digite o CRM que deseja excluir:")
    
    if not excluirCRM:
        return "Digite um CRM valido."
    
    else:
        sql = "SELECT * FROM MEDICO WHERE CRM = %s"
        return excluir_dadosTabela (con, sql, excluirCRM)


    
finalizar_conexao(con)

    