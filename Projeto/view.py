from controller import *
import os

def main():
            ########### MENU ############
    
    lista_tabela = []
    lista_rj = []
    lista_lj = []
    lista_partidas = [1, 3, 4]
    lista_vitorias = [1, 2, 3]
    lista_pecas_especiais_j1 = []
    lista_pecas_especiais_j2 = []            
    temp = 0
    valor_lateral=0 
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


        if opcao[0] == "ij":                                                                                                          #iniciar jogo
            comprimento = int(opcao[3])                                 
            altura = int(opcao[4])
            sequencia_vencedora = int(opcao[5])
                                                                                       
            if len(lista_rj) > 1:
                if len(lista_tabela) == 0:                                                                                            #se a lista tiver pelo menos dois jogadores registados                                  
                    lista_jogo = []                                                     
                    ## Nomes ##
                    if (opcao[1] in lista_rj) and (opcao[2] in lista_rj):                                                             #verifica se os jogadores estao registados
                        nome_jogadores_ij(opcao[1], opcao[2], lista_jogo)
                        ## Dimensoes ##
                        if (comprimento/2 <= altura <= comprimento):                                                                  #verifica as condições da dimensao da grelha
                            criar_tabela(comprimento, altura, lista_tabela)                                                           #cria os slots com os inseridos
                            ## Sequencia vencedora ##
                            if sequencia_vencedora != 1 and sequencia_vencedora != 2 and sequencia_vencedora < comprimento:           #verifica as condições da sequencia vencedora
                               ## Peças especais ##
                               for peca in [int(i) for i in opcao[6:]]:       
                                if peca < sequencia_vencedora:  
                                    pecas_especiais(peca, lista_pecas_especiais_j1, lista_pecas_especiais_j2)
                                    print(f"Jogo iniciado entre {opcao[1]} e {opcao[2]}") 
                                else:
                                    print("Dimensões de peças especiais invalidas.")
                                    lista_pecas_especiais_j1.clear()
                                    lista_pecas_especiais_j2.clear()
                                    lista_jogo.clear()
                                    lista_tabela.clear()
                                    break
                            else:
                                print("Tamanho de sequência invalido.")
                                lista_pecas_especiais_j1.clear()
                                lista_pecas_especiais_j2.clear()
                                lista_jogo.clear()
                                lista_tabela.clear()
                        else:  
                            print("Dimensões de grelha invalidas.")
                            lista_pecas_especiais_j1.clear()
                            lista_pecas_especiais_j2.clear()
                            lista_jogo.clear()
                            lista_tabela.clear()
                    else:  
                        print("Jogador não registado.")
                        lista_pecas_especiais_j1.clear()
                        lista_pecas_especiais_j2.clear()
                        lista_jogo.clear()
                        lista_tabela.clear()                                   
                    
                    print(lista_jogo)
                    print(lista_tabela)                     
                    print(lista_pecas_especiais_j1)
                    print(lista_pecas_especiais_j2)

                else: 
                    print("Já existe um jogo em curso")
                
            else:
                print("É necessários estarem registados 2 jogadores.")
                
            
            ########### REGISTAR JOGADOR ############


        elif opcao[0] == "rj":                                                                                   #registar jogador
            if opcao[1] not in lista_rj:                                                                         #loop que só é quebrado quando o jogador nao está na lista.
                registar_jogador(opcao[1], lista_rj)                                                             #registar jogadores, adicionando a lista de jogadores
                print("Jogador registado com sucesso.")
                print(lista_rj) #retirar
            else:
                print("Jogador existente.")

            ########### ELIMINAR JOGADOR ############
           
            
        elif opcao[0] == "ej":                                                                                   #eliminar jogador
            if len(lista_rj) != 0:                                                                               #verificação de número de jogadores, se estiver vazia é resultante uma saida com insucesso
                if opcao[1] not in lista_jogo:
                    if opcao[1] in lista_rj:                                                                     #loop que só é quebrado quando o jogador está na lista.
                        remover_jogador(opcao[1], lista_rj)                                                          #remover jogadores, removendo da lista de jogadores
                        print("Jogador removido com sucesso.")
                        print(lista_rj)
                    else:
                        print("Jogador não existente.")
                else:
                    print("Jogador participa no jogo em curso.")
            else:
                print("Não existem jogadores registados")

            ########### LISTAR JOGADOR ############

                
        elif opcao[0] == "lj":                                                                                          #listar jogadores              
            if len(lista_rj) == 0:                                                                               #verificação de número de jogadores, se estiver vazia é resultante uma saida com insucesso
                print("Não existem jogadores registados.")
            else:
                lista_lj = []                                                                                           #serve para reiniciar os valores caso seja adicionado um nojogo jogador
                listar_jogadores(lista_rj, lista_partidas, lista_vitorias, lista_lj) 
                for jogadores, partidas, vitorias in lista_lj:                                                          #ve a primeira lista dentro da lista_lj
                    print(f"Nome: {jogadores} / Partidas: {partidas} / Vitórias: {vitorias}")

            ########### DETALHES JOGO ############

        elif opcao[0] == "dj":                                                                                          #detalhes do jogo
            if len(lista_tabela) != 0:
                print(f"{comprimento} {altura}")
                print("")


            ########### DESISTIR #############

        elif opcao[0] == "d":                                                                                           #desistir
            pass    
            
            ########### COLOCAR PEÇA #############

        elif opcao[0] == "cp":
            colunas = int(opcao[3])                                                                                          #colocar peça
            if len(lista_tabela) != 0: 
                if opcao[1] in lista_jogo:
                    if opcao[1] != temp:                                                      
                        temp = opcao[1]
                        if temp == lista_jogo[0]:
                            ultimo_elemento_vazio = 1
                            for i in range(len(lista_tabela)):
                                if lista_tabela[i][colunas] == "|___|":
                                    ultimo_elemento_vazio = i
                                else:
                                    break
                            lista_tabela[ultimo_elemento_vazio][colunas] = "| X |"
                            print("Peça colocada.")

                        elif temp == lista_jogo[1]:
                            ultimo_elemento_vazio = 1
                            for i in range(len(lista_tabela)):
                                if lista_tabela[i][colunas] == "|___|":
                                    ultimo_elemento_vazio = i
                                else:
                                    break
                            lista_tabela[ultimo_elemento_vazio][colunas] = "| O |"
                            print("Peça colocada.")
                    else:
                        print('Não é possível jogar 2 vezes de seguida')                       
                else:
                    print('Jogador não participa no jogo em curso.')
            else:
                print('Não existe jogo em curso.')

            ########### VISUALIZAR RESULTADO #############

        elif opcao[0] == "v":                                                                                           #ver lista_tabela
            if lista_tabela != 0:
                for i in range(colunas):
                    print(f"    {i}", end="")
                print()

                for i in range(len(lista_tabela)):
                    print(valor_lateral,end = ' ')
                    valor_lateral += 1
                    for j in range(len(lista_tabela[i])):
                        print(lista_tabela[i][j],end = '')                        
                    print()
            else:
                print("Não existe jogo em curso")

            ########### GRAVAR #############
        
        elif opcao[0] == "g":                                                                                           #gravar
            pass
        
            ########## LER #############

        elif opcao[0] == "l":                                                                                           #ler
            pass
            
            ########### SAIR DO MENU ############
 
        elif opcao[0] == "sm":                                                                                          #sair menu 
            break
        
        else:
            print("Opção inválida.")

main()
