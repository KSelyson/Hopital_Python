from metodos_hospital import *

menu = """
╔═══════════════════════════════╗
║        Menu Principal         ║
║                               ║ 
║1) Adicionar novo paciente.    ║
║2) Adicionar novo médico.      ║
║3) Pesquisar paciente por CPF. ║
║4) Pesquisar médico por CRM.   ║
║5) Excluir paciente pelo CPF.  ║
║6) Excluir médico pelo CRM.    ║
║7) Gerenciar consultas.        ║
║8) Gerenciar procedimentos.    ║
║9) Sair                        ║
╚═══════════════════════════════╝

Digite a sua opção:  """

reload()
#METODO DE MENU PRINCIPAL
def main():
    while True:
        try:
            opcao = int(input(menu))

            if opcao == 1:
                print(add_paciente())

            elif opcao == 2:
                print(add_medico())

            elif opcao == 3:
                print(pesquisar_paciente())

            elif opcao == 4:
                print(pesquisar_medico())

            elif opcao == 5:
                print(excluir_paciente())

            elif opcao == 6:
                print(excluir_medico())

            elif opcao == 7:
                gerenciar_consultas()

            elif opcao == 8:
                gerenciar_procedimentos()

            elif opcao == 9:
                print(" → Fechando programa...")
                exit()

            else:
                print("\n → Opção inválida! Digite uma opção válida.")

        except ValueError:
            print("\n → ERROR! Opção inválida!")

#METODO QUE CHAMA O MENU DE GERENCIAMENTO DE CONSULTA
def gerenciar_consultas():
    sub_menu = """
    ╔═══════════════════════════════════╗
    ║ Menu de Gerenciamento de Consulta ║
    ║                                   ║
    ║1) Adicionar consultas.            ║
    ║2) Visualizar consultas marcadas.  ║
    ║3) Cancelar consultas.             ║
    ║4) Sair                            ║
    ╚═══════════════════════════════════╝
    
    Digite a sua opção:   """
    while True:
        try:
            opcao = int(input(sub_menu))

            if opcao == 1:
                print(adicionar_consulta())
            elif opcao == 2:
                print(visualizar_consulta())
            elif opcao == 3:
                print(cancelar_consulta())
            elif opcao == 4:
                print(" → Saindo do gerenciamento de consultas...")
                break
            else:
                print(" → Opção inválida! Digite uma opção válida.")
        except ValueError:
            print(" → ERROR! Opção inválida!")

#METODO QUE CHAMA O MENU DE GERENCIAMENTO DE PROCEDIMENTOS MÉDICOS
def gerenciar_procedimentos():
    sub_menu = """
    ╔════════════════════════════════════════╗
    ║ Menu de Gerenciamento de Procedimentos ║
    ║                                        ║
    ║1) Adicionar procedimentos.             ║
    ║2) Visualizar procedimentos.            ║
    ║3) Cancelar procedimentos.              ║
    ║4) Sair                                 ║        
    ╚════════════════════════════════════════╝
    
    Digite a sua opção:   """
    while True:
        try:
            opcao = int(input(sub_menu))

            if opcao == 1:
                print(adicionar_procedimento())
            elif opcao == 2:
                print(visualizar_procedimento())
            elif opcao == 3:
                print(cancelar_procedimento())
            elif opcao == 4:
                print("\n → Saindo do gerenciamento de procedimentos...")
                break
            else:
                print("\n → Opção inválida! Digite uma opção válida.")
        except ValueError:
            print("\n → ERROR! Opção inválida!")

#USADO PARA CHAMAR O METODO MAIN 
if __name__ == "__main__":
    main()
