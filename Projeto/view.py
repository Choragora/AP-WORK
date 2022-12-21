from controller import *
import os

def main():
### MENU ###
    lista_jogadores = []
    lista_lj = []
    lista_partidas = [1, 3, 4]
    lista_vitorias = [1, 2, 3]

    os.system("cls")
    while True: 
        print("""
    =-==-==-==-==-==-==-==-==-==-==-
    |                              |
    |        "N" em Linha \U0001f579\uFE0F        |
    |                              |
    |    [IJ] - Iniciar Jogo       |
    |    [RJ] - Registar Jogador   |
    |    [EJ] - Eliminar Jogador   |
    |    [LJ] - Listar Jogador     |
    |    [SM] - Sair do Menu       |
    |                              |
    =-==-==-==-==-==-==-==-==-==-==-
    """)
        
        opcao_menu = input("Introduza a sua opção: ").lower()
    
        if opcao_menu == "ij": #iniciar jogo
            pass

        elif opcao_menu == "rj": #registar jogador
            nome_registar = input("Introduza o nome a registar: ").lower()
            while nome_registar in lista_jogadores: #loop que só é quebrado quando o jogador nao está na lista.
                print("Jogador existente.")
                nome_registar = input("Introduza o nome a registar: ").lower()
            registar_jogador(nome_registar, lista_jogadores) #registar jogadores, adicionando a lista de jogadores
            print("Jogador registado com sucesso.")

            #ver ficheiros e armazenar os nomes dentro dos ficheiros
                
        elif opcao_menu == "ej": #eliminar jogador
            if len(lista_jogadores) == 0: #verificação de número de jogadores, se estiver vazia é resultante uma saida com insucesso
                print("Não existem jogadores registados")
            else:
                nome_remover = input("Introduza o nome a remover: ").lower()
                while nome_remover not in lista_jogadores: #loop que só é quebrado quando o jogador está na lista.
                    print("Jogador não existente.")
                    nome_remover = input("Introduza o nome a eliminar: ").lower()
                remover_jogador(nome_remover, lista_jogadores) #remover jogadores, removendo da lista de jogadores
                print("Jogador removido com sucesso.")

                # EM FALTA !!!!!!!!!
                # Saída com insucesso: Quando o jogador indicado não se encontra registado.
                
        elif opcao_menu == "lj": #listar jogadores              
            if len(lista_jogadores) == 0: #verificação de número de jogadores, se estiver vazia é resultante uma saida com insucesso
                print("Não existem jogadores registados.")
            else:
                lista_lj = [] #serve para reiniciar os valores caso seja adicionado um nojogo jogador
                listar_jogadores(lista_jogadores, lista_partidas, lista_vitorias, lista_lj) 
                for jogadores, partidas, vitorias in lista_lj: #ve a primeira lista dentro da lista_lj
                    print(f"Nome: {jogadores} / Partidas: {partidas} / Vitórias: {vitorias}")

        elif opcao_menu == "sm":
            break
        
        else:
            print("Opção inválida.")

main()

        