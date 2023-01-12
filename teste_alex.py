from controller import *
import os

def main():
            ########### MENU ############
    
    lista_tabela = []
    lista_rj = []
    lista_pecas_especiais_j1 = []
    lista_pecas_especiais_j2 = []            
    lista_sentidos = ["e", "d"]
    temp = 0
 
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

        if opcao[0] == "ij":   #se for iniciar jogo
            comprimento = int(opcao[3])                              
            altura = int(opcao[4]) 
            sequencia_vencedora = int(opcao[5])
                                                                                       
            if len(lista_rj) > 1:     #verifica se a lista tem pelo menos dois jogadores registados
                if len(lista_tabela) == 0:    #verifica se existe jogo em curso                                                                                                                                        
                    lista_jogo = []     #lista onde serao armazenados os jogadores                                                     
                    ########## NOMES ##########
                    if (opcao[1] in lista_rj) and (opcao[2] in lista_rj):    #verifica se os jogadores estao registados
                        nome_jogadores_ij(opcao[1], opcao[2], lista_jogo)
                        ########## DIMENSOES ##########
                        if (comprimento/2 <= altura <= comprimento):    #verifica as condições da dimensao da grelha
                            for i in range (altura):
                                lista_tabela.append(["|___|"] *comprimento)     #cria os slots da grelha
                            ########## SEQUENCIA VENCEDORA ##########
                            if sequencia_vencedora != 1 and sequencia_vencedora != 2 and sequencia_vencedora < comprimento:     #verifica as condições da sequencia vencedora
                               ########## PEÇAS ESPECIAIS ##########
                                for peca in [int(i) for i in opcao[6:]]:    #serve para iterar a partir do 6 elemento da opcao     
                                    if peca < sequencia_vencedora:      #verifica se a peça é inferior a sequencia vencedora
                                        pecas_especiais(peca, lista_pecas_especiais_j1, lista_pecas_especiais_j2)        
                                    else:
                                        print("Dimensões de peças especiais invalidas.")
                                        lista_pecas_especiais_j1.clear()
                                        lista_pecas_especiais_j2.clear()    #limpa todas as listas eliminando o jogo em curso
                                        lista_jogo.clear()
                                        lista_tabela.clear()
                                        break
                                ########## VERIFICAÇÃO FINAL ##########
                                if len(lista_pecas_especiais_j1) > 0 and len(lista_pecas_especiais_j2) > 0: #se tudo estiver bem inicia o jogo
                                    print(f"Jogo inicado entre {opcao[1]} e {opcao[2]}")
                            else:
                                print("Tamanho de sequência invalido.")
                                lista_pecas_especiais_j1.clear()
                                lista_pecas_especiais_j2.clear()    #limpa todas as listas eliminando o jogo em curso
                                lista_jogo.clear()
                                lista_tabela.clear()
                        else:  
                            print("Dimensões de grelha invalidas.")
                            lista_pecas_especiais_j1.clear()
                            lista_pecas_especiais_j2.clear()    #limpa todas as listas eliminando o jogo em curso
                            lista_jogo.clear()
                            lista_tabela.clear()
                    else:  
                        print("Jogador não registado.")
                        lista_pecas_especiais_j1.clear()
                        lista_pecas_especiais_j2.clear()    #limpa todas as listas eliminando o jogo em curso
                        lista_jogo.clear()
                        lista_tabela.clear()                                   
                    
                    print(lista_jogo)
                    print(lista_tabela)                     
                    print(lista_pecas_especiais_j1)     #limpa todas as listas eliminando o jogo em curso
                    print(lista_pecas_especiais_j2)

                else: 
                    print("Já existe um jogo em curso")
                
            else:
                print("É necessários estarem registados 2 jogadores.")
                
            
            ########### REGISTAR JOGADOR ############


        elif opcao[0] == "rj":    #registar jogador
            if opcao[1] not in lista_rj:    #loop que só é quebrado quando o jogador nao está na lista.
                registar_jogador(opcao[1], lista_rj)    #registar jogadores, adicionando a lista de rj
                print("Jogador registado com sucesso.")
                print(lista_rj) #retirar++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            else:
                print("Jogador existente.")

            ########### ELIMINAR JOGADOR ############
           
        elif opcao[0] == "ej":                                                                                   
            if len(lista_rj) != 0:    #verificação de número de jogadores
                if opcao[1] not in lista_jogo:    #verifica se o nome esta num jogo em curso
                    if opcao[1] in lista_rj:    #verifica se o nome esta registado                                                                
                        remover_jogador(opcao[1], lista_rj)                                                          
                        print("Jogador removido com sucesso.")
                        print(lista_rj) #retirar+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    else:
                        print("Jogador não existente.")
                else:
                    print("Jogador participa no jogo em curso.")
            else:
                print("Não existem jogadores registados")

            ########### LISTAR JOGADOR ############

                
        elif opcao[0] == "lj":                                                                                                        
            pass

            ########### DETALHES JOGO ############

        elif opcao[0] == "dj":                                                                                          
            if len(lista_tabela) != 0:    #verifica se existe jogo em curso
                print(f"{comprimento} {altura}")
                ########## JOGADOR 1 ##########
                print(lista_jogo[0])
                
                
            else:
                print('Não existe jogo em curso.')

            ########### DESISTIR #############

        elif opcao[0] == "d":                                                                                           
            if len(lista_tabela) != 0:
                if opcao == 3:
                    if opcao[1] in lista_rj and opcao[2] in lista_rj:
                        if opcao[1] in lista_jogo and opcao[2] in lista_jogo:
                            #Adicionar o jogo jogado aos dois!!!!!
                            #Limpar as listas
                            print('Desistência com sucesso. Jogo terminado.')

                        else:
                            print('Jogador não participa no jogo em curso.')
                    else:
                        print('Jogador não registado.')
                elif len(opcao) == 2:
                    if opcao[1] in lista_rj:
                        if opcao[1] in lista_jogo:
                            print('Desistência com sucesso. Jogo terminado.')
                            #Adicionar os pontos ao vencedor e o jogo jogado aos dois!!!!!
                            #limpar todas as listas
                        else:
                            print('Jogador não participa no jogo em curso.')
                    else:
                        print('Jogador não registado.')
                else:
                    False
            else:
                print('Não existe jogo em curso.')
                    
            
            ########### COLOCAR PEÇA #############

        elif opcao[0] == "cp":                      
            tamanho_peca = int(opcao[2])
            colunas = int(opcao[3])                                                                                          
            if len(lista_tabela) != 0:    #verifica se existe jogo em curso
                if opcao[1] in lista_jogo:    #verifica se nome esta na lista de jogadores em curso
                    ########## MUDANCA DE JOGADOR ##########
                    if opcao[1] != temp:    #variável temporária que serve para alternar a vez dos jogadores                                                      
                        temp = opcao[1]                            
                        ########## PECA UNITARIA ##########
                        if tamanho_peca == 1:   
                            ########## JOGADOR 1 ##########
                            if temp == lista_jogo[0]:   
                                if lista_tabela[0][colunas] == "|___|":    #verifica se a coluna inserida está cheia
                                    ultimo_elemento_vazio = 1
                                    for i in range(len(lista_tabela)):      #loop para verificar os elementos vazios da coluna e no final inserir a jogada
                                        if lista_tabela[i][colunas] == "|___|":
                                            ultimo_elemento_vazio = i
                                        else:
                                            break
                                    lista_tabela[ultimo_elemento_vazio][colunas] = "| X |"
                                    print("Peça colocada.")

                                    for i in range(len(lista_tabela)):                                                                                                                                                             #Isso pega a linha "i" da matriz usando o índice "i" e verifica se a expressão "val == x" é verdadeira 
                                        if all(val == "| X |" for val in lista_tabela[i]):                                                                                                                                              #para todos os valores na linha usando o método "all()", e imprime uma mensagem de acordo.
                                            print("VITORIA")
                                            
                                        else:
                                            pass


                                    for j in range(len(lista_tabela)):         
                                        if all(lista_tabela[i][j] == "| X |" for i in range(len(lista_tabela))):
                                            print(f"VITORIA")
                                            
                                        else:
                                            pass

                                    
                                    for i in range(len(lista_tabela)):
                                        if all(lista_tabela[i][i] == "| X |" for i in range(len(lista_tabela))):
                                            print("VITÓRIA")
                                            
                                        else:
                                            pass

                                else:
                                    print("Posição irregular.")
                                    temp = lista_jogo[1]    #mudar o valor do temp para o jogador adversário para que o jogador posso tentar denovo 
                            ########## JOGADOR 2 ##########
                            elif temp == lista_jogo[1]:
                                if lista_tabela[0][colunas] == "|___|":    #verifica se a coluna inserida está cheia 
                                    ultimo_elemento_vazio = 1
                                    for i in range(len(lista_tabela)):      #loop para verificar os elementos vazios da coluna e no final inserir a jogada
                                        if lista_tabela[i][colunas] == "|___|":
                                            ultimo_elemento_vazio = i
                                        else:
                                            break
                                    lista_tabela[ultimo_elemento_vazio][colunas] = "| O |"    
                                    print("Peça colocada.")

                                    for i in range(len(lista_tabela)):                                                                                                                                                             #Isso pega a linha "i" da matriz usando o índice "i" e verifica se a expressão "val == x" é verdadeira 
                                        if all(val == "| O |" for val in lista_tabela[i]):                                                                                                                                              #para todos os valores na linha usando o método "all()", e imprime uma mensagem de acordo.
                                            print("VITORIA")
                                            
                                        else:
                                            pass


                                    for j in range(len(lista_tabela)):         
                                        if all(lista_tabela[i][j] == "| O |" for i in range(len(lista_tabela))):
                                            print(f"VITORIA")
                                            
                                        else:
                                            pass

                                    for i in range(len(lista_tabela)):
                                        if all(lista_tabela[i][i] == "| O |" for i in range(len(lista_tabela))):
                                            print("VITÓRIA")
                                            
                                        else:
                                            pass
                                else:
                                    print("Posição irregular.")
                                    temp = lista_jogo[0]    #mudar o valor do temp para o jogador adversário para que o jogador posso tentar denovo 
                        ########## PEÇA ESPECIAL ##########
                        elif (tamanho_peca != 1):
                            ########## JOGADOR 1 ########## 
                            if temp == lista_jogo[0]: 
                                if len(lista_pecas_especiais_j1) != 0:    #verifica se o jogador tem peças especiais 
                                    if tamanho_peca in lista_pecas_especiais_j1:    #verifica se a peça requesitada existe dentro da lista de peças especiais
                                        ########## ESQUERDA ##########
                                        if opcao[4] == lista_sentidos[0]: 
                                            if colunas >= tamanho_peca - 1:    #equacao que limita o posicionamento para a esquerda
                                                ultimo_elemento_vazio = 1
                                                for j in range(tamanho_peca):   #loop para fazer a verificação e jogada igual o nume de vezes = tamanho da peça especial
                                                    if lista_tabela[0][colunas] == "|___|":
                                                        for i in range(len(lista_tabela)):     #loop para verificar os elementos vazios da coluna e no final inserir a jogada
                                                            if lista_tabela[i][colunas] == "|___|":
                                                                ultimo_elemento_vazio = i
                                                            else:
                                                                break
                                                        lista_tabela[ultimo_elemento_vazio][colunas] = "| X |"
                                                    colunas -= 1    #andar para a esquerda
                                                print("Peça colocada.")

                                                for i in range(len(lista_tabela)):                                                                                                                                                             #Isso pega a linha "i" da matriz usando o índice "i" e verifica se a expressão "val == x" é verdadeira 
                                                    if all(val == "| X |" for val in lista_tabela[i]):                                                                                                                                              #para todos os valores na linha usando o método "all()", e imprime uma mensagem de acordo.
                                                        print("VITORIA")
                                                    else:
                                                        pass


                                                for j in range(len(lista_tabela)):         
                                                    if all(lista_tabela[i][j] == "| X |" for i in range(len(lista_tabela))):
                                                        print(f"VITORIA")
                                                    else:
                                                        pass

                                                for i in range(len(lista_tabela)):
                                                    if all(lista_tabela[i][i] == "| X |" for i in range(len(lista_tabela))):
                                                        print("VITÓRIA")
                                                    else:
                                                        pass
                                                lista_pecas_especiais_j1.remove(tamanho_peca)    #limpar a peça especial usada
                                            else:
                                                print("Posição irregular.")
                                                temp = lista_jogo[1]    #mudar o valor do temp para o jogador adversário para que o jogador posso tentar denovo    
                                        ########## DIREITA ##########
                                        elif opcao[4] == lista_sentidos[1]: 
                                            if colunas < comprimento + 1 - tamanho_peca:    #equacao que limita o posicionamento para a direita
                                                ultimo_elemento_vazio = 1
                                                for j in range(tamanho_peca):   #loop para fazer a verificação e jogada igual o nume de vezes = tamanho da peça especial
                                                    if lista_tabela[0][colunas] == "|___|":
                                                        for i in range(len(lista_tabela)):    #loop para verificar os elementos vazios da coluna e no final inserir a jogada
                                                            if lista_tabela[i][colunas] == "|___|":
                                                                ultimo_elemento_vazio = i
                                                            else:
                                                                break
                                                        lista_tabela[ultimo_elemento_vazio][colunas] = "| X |"
                                                    colunas += 1    #andar para a direita
                                                print("Peça colocada.")

                                                for i in range(len(lista_tabela)):                                                                                                                                                             #Isso pega a linha "i" da matriz usando o índice "i" e verifica se a expressão "val == x" é verdadeira 
                                                    if all(val == "| X |" for val in lista_tabela[i]):                                                                                                                                              #para todos os valores na linha usando o método "all()", e imprime uma mensagem de acordo.
                                                        print("VITORIA")
                                                    else:
                                                        pass


                                                for j in range(len(lista_tabela)):         
                                                    if all(lista_tabela[i][j] == "| X |" for i in range(len(lista_tabela))):
                                                        print(f"VITORIA")
                                                    else:
                                                        pass

                                                for i in range(len(lista_tabela)):
                                                    if all(lista_tabela[i][i] == "| X |" for i in range(len(lista_tabela))):
                                                        print("VITÓRIA")
                                                    else:
                                                        pass
                                                lista_pecas_especiais_j1.remove(tamanho_peca)    #limpar a peça especial usada
                                            else:
                                                print("Posição irregular.")
                                                temp = lista_jogo[1]    #mudar o valor do temp para o jogador adversário para que o jogador posso tentar denovo    
                                    else:
                                        print("Tamanho de peça não disponivel.")
                                        temp = lista_jogo[1]    #mudar o valor do temp para o jogador adversário para que o jogador posso tentar denovo
                                else: 
                                    print("O jogador não apresenta peças especiais disponiveis.")
                                    temp = lista_jogo[1]    #mudar o valor do temp para o jogador adversário para que o jogador posso tentar denovo
                            ########## JOGADOR 2 ##########
                            elif temp == lista_jogo[1]: 
                                if len(lista_pecas_especiais_j2) != 0:     #verifica se o jogador tem peças especiais
                                    if tamanho_peca in lista_pecas_especiais_j2:    #verifica se a peça requesitada existe dentro da lista de peças especiais
                                        ########## ESQUERDA ##########
                                        if opcao[4] == lista_sentidos[0]: 
                                            if colunas >= tamanho_peca - 1:    #equacao que limita o posicionamento para a esquerda
                                                ultimo_elemento_vazio = 1
                                                for j in range(tamanho_peca):      #loop para fazer a verificação e jogada igual o nume de vezes = tamanho da peça especial
                                                    if lista_tabela[0][colunas] == "|___|":
                                                        for i in range(len(lista_tabela)):     #loop para verificar os elementos vazios da coluna e no final inserir a jogada
                                                            if lista_tabela[i][colunas] == "|___|":
                                                                ultimo_elemento_vazio = i
                                                            else:
                                                                break
                                                        lista_tabela[ultimo_elemento_vazio][colunas] = "| O |"
                                                    colunas -= 1    #andar para a esquerda
                                                print("Peça colocada.")

                                                for i in range(len(lista_tabela)):                                                                                                                                                             #Isso pega a linha "i" da matriz usando o índice "i" e verifica se a expressão "val == x" é verdadeira 
                                                    if all(val == "| O |" for val in lista_tabela[i]):                                                                                                                                              #para todos os valores na linha usando o método "all()", e imprime uma mensagem de acordo.
                                                        print("VITORIA")
                                                    else:
                                                        pass


                                                for j in range(len(lista_tabela)):         
                                                    if all(lista_tabela[i][j] == "| O |" for i in range(len(lista_tabela))):
                                                        print(f"VITORIA")
                                                    else:
                                                        pass

                                                for i in range(len(lista_tabela)):
                                                    if all(lista_tabela[i][i] == "| O |" for i in range(len(lista_tabela))):
                                                        print("VITÓRIA")
                                                    else:
                                                        pass
                                                lista_pecas_especiais_j2.remove(tamanho_peca)   #limpar a peça especial usada
                                            else:
                                                print("Posição irregular.")
                                                temp = lista_jogo[0]    #mudar o valor do temp para o jogador adversário para que o jogador posso tentar denovo    
                                        ########## DIREITA ##########
                                        elif opcao[4] == lista_sentidos[1]: 
                                            if colunas < comprimento + 1 - tamanho_peca:    #equacao que limita o posicionamento para a direita 
                                                ultimo_elemento_vazio = 1
                                                for j in range(tamanho_peca):    #loop para fazer a verificação e jogada igual o nume de vezes = tamanho da peça especial
                                                    if lista_tabela[0][colunas] == "|___|":     
                                                        for i in range(len(lista_tabela)):    #loop para verificar os elementos vazios da coluna e no final inserir a jogada
                                                            if lista_tabela[i][colunas] == "|___|":
                                                                ultimo_elemento_vazio = i
                                                            else:
                                                                break
                                                        lista_tabela[ultimo_elemento_vazio][colunas] = "| O |"
                                                    colunas += 1    #andar para a direita
                                                print("Peça colocada.")

                                                for i in range(len(lista_tabela)):                                                                                                                                                             #Isso pega a linha "i" da matriz usando o índice "i" e verifica se a expressão "val == x" é verdadeira 
                                                    if all(val == "| O |" for val in lista_tabela[i]):                                                                                                                                              #para todos os valores na linha usando o método "all()", e imprime uma mensagem de acordo.
                                                        print("VITORIA")
                                                    else:
                                                        pass


                                                for j in range(len(lista_tabela)):         
                                                    if all(lista_tabela[i][j] == "| O |" for i in range(len(lista_tabela))):
                                                        print(f"VITORIA")
                                                    else:
                                                        pass

                                                for i in range(len(lista_tabela)):
                                                    if all(lista_tabela[i][i] == "| O |" for i in range(len(lista_tabela))):
                                                        print("VITÓRIA")
                                                    else:
                                                        pass
                                                lista_pecas_especiais_j2.remove(tamanho_peca)    #limpar a peça especial usada
                                            else:
                                                print("Posição irregular.")
                                                temp = lista_jogo[0]    #mudar o valor do temp para o jogador adversário para que o jogador posso tentar denovo
                                    else:
                                        print("Tamanho de peça não disponivel.")
                                        temp = lista_jogo[0]    #mudar o valor do temp para o jogador adversário para que o jogador posso tentar denovo
                                else:
                                    print("O jogador não apresenta peças especiais disponiveis.")
                                    temp = lista_jogo[0]    #mudar o valor do temp para o jogador adversário para que o jogador posso tentar denovo
                    else:
                        print('Não é possível jogar 2 vezes de seguida')                       
                else:
                    print('Jogador não participa no jogo em curso.')
            else:
                print('Não existe jogo em curso.')

            ########### VISUALIZAR RESULTADO #############
        elif opcao[0] == "v":                                                                                           
            if lista_tabela != 0:
                for i in range(len(lista_tabela)):      #represetação gráfica da tabela atualizada
                    for j in range(len(lista_tabela[i])):
                        print(lista_tabela[i][j],end = '')                        
                    print()
            else:
                print("Não existe jogo em curso")

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
