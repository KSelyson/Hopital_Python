from bancodados_hospital import *

con = criar_conexao('192.168.0.1', 'root', 'AndreyEloy01')

def add_paciente():
   
    CPF      = input("Digite o CPF do paciente:")
    nome     = input("Digite o nome do paciente:")
    idade    = input("Digite a idade do paciente:")
    endereco = input("Digite o endereco do paciente:")
    telefone = input("Digite o telefone do paciente:")
    
    if not CPF or not nome or not idade or not endereco or not telefone:
        print("Por favor, preencha todos os campos")
        return
    print(adicionar_paciente(CPF, nome, idade, endereco, telefone, pacientes))

def add_medico(): 
   
    nome          = input("Digite o nome do médico:")
    especialidade = input("Digite a especialidade do médico:")
    CRM           = input("Digite o CRM do médico:")
    telefone      = input("Digite o telefone do médico:")    
    if not nome or not especialidade or not CRM or not telefone:
        print("Por favor, preencha todos os campos")
        return
    print(adicionar_medico(nome, especialidade, CRM, telefone, medicos)) 

def adicionar_paciente(CPF, nome, idade, endereco, telefone, pacientes):
    
    for paciente in pacientes:
        if paciente["CPF"] == CPF:
            return "Este CPF ja está cadastrado."
    paciente = {"CPF": CPF, "Nome": nome, "Idade": idade, "Endereço": endereco, "Telefone": telefone}
    pacientes.append(paciente)
    return "Novo paciente cadastrado com sucesso!"

def adicionar_medico(nome, especialidade, CRM, telefone, medicos):
   
    for medico in medicos:
       
        if medico["CRM"] == CRM:
            return "Este CRM ja está cadastrado."
   
    medico = {"Nome":nome, "Especialidade": especialidade, "CRM": CRM, "Telefone": telefone}
    medicos.append(medico)
    return "Novo médico cadastrado com sucesso!"

def pesquisar_paciente(CPF, pacientes):
   
    for paciente in pacientes:
        if paciente["CPF"] == CPF:
            return paciente
    return "Paciente não encontrado!"

def pesquisar_medico(CRM, medicos):
    
    for medico in medicos:
        if medico["CRM"] == CRM:
            return medico
    return "Médico não encontrado!"

def excluir_paciente(CPF, pacientes):
    
    for paciente in pacientes:
        if paciente["CPF"] == CPF:
            pacientes.remove(paciente)
            return "Paciente removido com sucesso!"
    return "Paciente não encontrado!"

def excluir_medico(CRM, medicos):
    
    for medico in medicos:
        if medico["CRM"] == CRM:
            medicos.remove(medico)
            return "Medico removido com sucesso!"
    return "Médico não encontrado!"

pacientes = []
medicos = []
    
finalizar_conexao(con)

    