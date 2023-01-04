from controller import *
import os

def main():
########### MENU ############
    lista_jogadores = []
    lista_lj = []
    lista_partidas = [1, 3, 4]
    lista_vitorias = [1, 2, 3]

    
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
    
        if opcao_menu == "ij":                                                                            #iniciar jogo
            if len(lista_jogadores) > 1:                                                                  #indicar os jogadores que irão jogar
                jogadores_jogo = []
                jogador_1 = input("Introduza o nome do jogador 1. ")
                jogador_2 = input("Introduza o nome do jogador 2. ")
                while (jogador_1 not in lista_jogadores) or (jogador_2 not in lista_jogadores):
                    print("Jogador não registado.")
                    jogador_1 = input("Introduza o nome do jogador 1. ")
                    jogador_2 = input("Introduza o nome do jogador 2. ")
                nome_jogadores_ij(jogador_1, jogador_2, jogadores_jogo)
            
                comprimento = int(input("Introduza o comprimento da grelha: "))                           #indicar as dimensoes da grelha
                altura = int(input("Introduza a altura da grelha: "))
                while (altura > comprimento) or (altura < comprimento/2): 
                    print("Dimensões de grelha invalidas.")
                    comprimento = int(input("Introduza o comprimento da grelha: "))
                    altura = int(input("Introduza a altura da grelha: "))
                    #necessário uma função que cria a grelha consoante a dimensao da mesma 
                
                seq_vencedora = int(input("Introduza o número da sequencia vencedora: "))
                while seq_vencedora == 1 or seq_vencedora == 2 or seq_vencedora > comprimento:
                    print("Tamanho de sequência invalido.")
                    seq_vencedora = int(input("Introduza o número da sequencia vencedora: "))
                    #funçao que regista o n em linha

                #ultimo ponto: peças especiais 
                 
                
            else:
                print("É necessários estarem registados 2 jogadores.")
                

                
                   
            
            

        elif opcao_menu == "rj":                                                                            #registar jogador
            nome_registar = input("Introduza o nome a registar: ").lower()
            while nome_registar in lista_jogadores:                                                         #loop que só é quebrado quando o jogador nao está na lista.
                print("Jogador existente.")
                nome_registar = input("Introduza o nome a registar: ").lower()
            registar_jogador(nome_registar, lista_jogadores)                                                #registar jogadores, adicionando a lista de jogadores
            print("Jogador registado com sucesso.")

        #ver ficheiros e armazenar os nomes dentro dos ficheiros

        elif opcao_menu == "ej":                                                                            #eliminar jogador
            if len(lista_jogadores) == 0:                                                                   #verificação de número de jogadores, se estiver vazia é resultante uma saida com insucesso
                print("Não existem jogadores registados")
            else:
                nome_remover = input("Introduza o nome a remover: ").lower()
                while nome_remover not in lista_jogadores:                                                  #loop que só é quebrado quando o jogador está na lista.
                    print("Jogador não existente.")
                    nome_remover = input("Introduza o nome a eliminar: ").lower()
                remover_jogador(nome_remover, lista_jogadores)                                              #remover jogadores, removendo da lista de jogadores
                print("Jogador removido com sucesso.")

                # EM FALTA !!!!!!!!!
                # Saída com insucesso: Quando o jogador indicado não se encontra registado.
                
        elif opcao_menu == "lj":                                                                            #listar jogadores              
            if len(lista_jogadores) == 0:                                                                   #verificação de número de jogadores, se estiver vazia é resultante uma saida com insucesso
                print("Não existem jogadores registados.")
            else:
                lista_lj = []                                                                               #serve para reiniciar os valores caso seja adicionado um nojogo jogador
                listar_jogadores(lista_jogadores, lista_partidas, lista_vitorias, lista_lj) 
                for jogadores, partidas, vitorias in lista_lj:                                              #ve a primeira lista dentro da lista_lj
                    print(f"Nome: {jogadores} / Partidas: {partidas} / Vitórias: {vitorias}")

        elif opcao_menu == "sm":
            break
        
        else:
            print("Opção inválida.")

main()