from controller import *
import os

def main():
            ########### MENU ############
    
    tabela = []
    lista_jogadores = []
    lista_lj = []
    lista_partidas = [1, 3, 4]
    lista_vitorias = [1, 2, 3]

    os.system("cls")
    while True: 
    #     print("""
    # =-==-==-==-==-==-==-==-==-==-==-==
    # |                                |
    # |         "N" em Linha \U0001f579\uFE0F         |
    # |                                |
    # |     [IJ] - Iniciar Jogo        | 
    # |     [RJ] - Registar Jogador    |
    # |     [EJ] - Eliminar Jogador    |
    # |     [LJ] - Listar Jogador      |
    # |     [DJ] - Detalhes de Jogo    |
    # |     [D] - Desistir             | 
    # |     [CP] - Colocar Peça        |
    # |     [V] - Vizualizar Resultado |
    # |     [G] - Gravar               |
    # |     [L] - Ler                  |
    # |     [SM] - Sair do Menu        |
    # |                                |
    # =-==-==-==-==-==-==-==-==-==-==-==
    # """)
        
        opcao = input("Introduza a sua opção: ").lower().split(' ')

        
            ########### INICIAR JOGO ############


        if opcao[0] == "ij":                                                                                #iniciar jogo
            comprimento = int(opcao[3])
            altura = int(opcao[4])
            sequencia_vencedora = int(opcao[5])
                                                                                       
            if len(lista_jogadores) > 1:                                                                  
                jogadores_jogo = []
                ## Nomes ##
                if (opcao[1] not in lista_jogadores) or (opcao[2] not in lista_jogadores):    
                    print("Jogador não registado.")
                else:    
                    nome_jogadores_ij(opcao[1], opcao[2], jogadores_jogo)
                
                ## Dimensoes ##
                if (comprimento < altura) or (comprimento/2 > altura): 
                    print("Dimensões de grelha invalidas.")
                else:  
                    criar_tabela(comprimento, altura, tabela)
                    print(tabela)

                ## Sequencia vencedora ##
                if sequencia_vencedora == 1 or sequencia_vencedora == 2 or sequencia_vencedora > comprimento:
                    print("Tamanho de sequência invalido.")
                else:
                    pass
                    #funçao que regista o n em linha

                #ultimo ponto: peças especiais 

            else:
                print("É necessários estarem registados 2 jogadores.")
                
            
            ########### REGISTAR JOGADOR ############


        elif opcao[0] == "rj":                                                                            #registar jogador
            if opcao[1] in lista_jogadores:                                                         #loop que só é quebrado quando o jogador nao está na lista.
                print("Jogador existente.")
            else:
                registar_jogador(opcao[1], lista_jogadores)                                                #registar jogadores, adicionando a lista de jogadores
                print("Jogador registado com sucesso.")
                print(lista_jogadores)
            

            ########### ELIMINAR JOGADOR ############
           
            
        elif opcao[0] == "ej":                                                                            #eliminar jogador
            if len(lista_jogadores) == 0:                                                                   #verificação de número de jogadores, se estiver vazia é resultante uma saida com insucesso
                print("Não existem jogadores registados")
            else:
                if opcao[1] not in lista_jogadores:                                                  #loop que só é quebrado quando o jogador está na lista.
                    print("Jogador não existente.")
                else:
                    remover_jogador(opcao[1], lista_jogadores)                                              #remover jogadores, removendo da lista de jogadores
                    print("Jogador removido com sucesso.")
                    print(lista_jogadores)

                # EM FALTA !!!!!!!!!
                # Saída com insucesso: Quando o jogador participa no jogo em curso.


            ########### LISTAR JOGADOR ############

                
        elif opcao[0] == "lj":                                                                            #listar jogadores              
            if len(lista_jogadores) == 0:                                                                   #verificação de número de jogadores, se estiver vazia é resultante uma saida com insucesso
                print("Não existem jogadores registados.")
            else:
                lista_lj = []                                                                               #serve para reiniciar os valores caso seja adicionado um nojogo jogador
                listar_jogadores(lista_jogadores, lista_partidas, lista_vitorias, lista_lj) 
                for jogadores, partidas, vitorias in lista_lj:                                              #ve a primeira lista dentro da lista_lj
                    print(f"Nome: {jogadores} / Partidas: {partidas} / Vitórias: {vitorias}")

            ########### DETALHES JOGO ############

        elif opcao[0] == "dj":
            pass

            ########### DESISTIR #############

        elif opcao[0] == "d":
            pass
            
            ########### COLOCAR PEÇA #############

        elif opcao[0] == "cp":
            pass

            ########### VISUALIZAR RESULTADO #############

        elif opcao[0] == "v":
            valor_lateral = 0
            desenhar_tabela(comprimento, tabela, valor_lateral)

            ########### GRAVAR #############
        
        elif opcao[0] == "g":
            pass
        
            ########## LER #############

        elif opcao[0] == "l":
            pass
            
            ########### SAIR DO MENU ############

        elif opcao[0] == "sm":
            break
        
        else:
            print("Opção inválida.")

main()