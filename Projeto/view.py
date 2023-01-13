from controller import *
import os

def main():
    
    ########### VARIAVEIS TEMPORARIAS ############

    lista_tabela = []
    lista_rj = ler_ficheiro_json("jogadores_json")
    lista_pecas_especiais_j1 = []
    lista_pecas_especiais_j2 = []            
    lista_sentidos = ["e", "d"]
    nome = 0
    horizontal = 0
    vertical = 0

    os.system("cls")
    while True: 
        
        
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

                    if verificar_nomes(lista_rj, opcao[1]) == 1 and verificar_nomes(lista_rj, opcao[2]) == 2:
                        lista_jogo.append(opcao[1])
                        lista_jogo.append(opcao[2])

                        ########## DIMENSOES ##########

                        if (comprimento/2 <= altura <= comprimento):    #verifica as condições da dimensao da grelha
                            for i in range (altura):
                                lista_tabela.append(["|___|"] *comprimento)     #cria os slots da grelha
                                
                            ########## SEQUENCIA VENCEDORA ##########

                            if sequencia_vencedora != 1 and sequencia_vencedora != 2 and sequencia_vencedora < comprimento:     #verifica as condições da sequencia vencedora
                                
                               ########## PEÇAS ESPECIAIS ##########
                               
                                for peca in [int(i) for i in opcao[6:]]:    #serve para iterar a partir do 6 elemento da opcao     
                                    if peca < sequencia_vencedora and peca != 1:      #verifica se a peça é inferior a sequencia vencedora e é diferente de 1
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
            if verificar_nomes(lista_rj, opcao[1]) == False:    #loop que só é quebrado quando o jogador nao está na lista.
                registar_jogador(opcao[1], lista_rj)   #registar jogadores, adicionando a lista de rj
                escrever_ficheiro_json("jogadores_json", lista_rj)
                print("Jogador registado com sucesso.")
                print(lista_rj)
            else:
                print("Jogador existente.")



        ########### ELIMINAR JOGADOR ############
        
        elif opcao[0] == "ej":                                                                                   
            if len(lista_rj) != 0:    #verificação de número de jogadores
                if opcao[1] not in lista_jogo:    #verifica se o nome esta num jogo em curso
                    if opcao[1] in lista_rj:    #verifica se o nome esta registado                                                                
                        remover_jogador(opcao[1], lista_rj)                                                          
                        print("Jogador removido com sucesso.")
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
                print(f"Comprimento: {comprimento} | Altura: {altura}")
                print()

                ########## JOGADOR 1 ##########

                print(f"Nome: {lista_jogo[0]}")
                lista_dj_j1 = []
                for elemento in lista_pecas_especiais_j1:
                    if elemento not in lista_dj_j1:
                        contagem = lista_pecas_especiais_j1.count(elemento)
                        lista_dj_j1.append(elemento)
                        print(f"TamanhoPeça: {elemento} | Quantidade: {contagem}")
                print()

                ########## JOGADOR 2 ##########

                print(f"Nome: {lista_jogo[1]}")
                lista_dj_j2 = []
                for elemento in lista_pecas_especiais_j2:
                    if elemento not in lista_dj_j2:
                        contagem = lista_pecas_especiais_j2.count(elemento)
                        lista_dj_j2.append(elemento)
                        print(f"TamanhoPeça: {elemento} | Quantidade: {contagem}")
            else:
                print('Não existe jogo em curso.')



        ########### DESISTIR #############
            
        elif opcao[0] == "d":                                                                                           
            if len(lista_tabela) != 0:
                if opcao == 3:
                    if opcao[1] in lista_rj and opcao[2] in lista_rj:
                        if opcao[1] in lista_jogo and opcao[2] in lista_jogo:
                            #Adicionar o jogo jogado aos dois!!!!!
                            lista_jogo.clear()
                            lista_pecas_especiais_j1.clear()    #limpar o jogo em curso
                            lista_pecas_especiais_j2.clear()
                            lista_tabela.clear()
                            print('Desistência com sucesso. Jogo terminado.')

                        else:
                            print('Jogador não participa no jogo em curso.')
                    else:
                        print('Jogador não registado.')
                elif len(opcao) == 2:
                    if opcao[1] in lista_rj:
                        if opcao[1] in lista_jogo:
                            print('Desistência com sucesso. Jogo terminado.')
                            #Adicionar os pontos ao vencedor e o jogo jogado aos dois!!!!!por acabar
                            lista_jogo.clear()
                            lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                            lista_pecas_especiais_j2.clear()
                            lista_tabela.clear()
                        else:
                            print('Jogador não participa no jogo em curso.')
                    else:
                        print('Jogador não registado.')
            else:
                print('Não existe jogo em curso.')
                    
            

        ########### COLOCAR PEÇA #############

        elif opcao[0] == "cp":                      
            tamanho_peca = int(opcao[2])
            colunas = int(opcao[3])                                                                                          
            if len(lista_tabela) != 0:    #verifica se existe jogo em curso
                if opcao[1] in lista_jogo:    #verifica se nome esta na lista de jogadores em curso

                    ########## MUDANCA DE JOGADOR ##########

                    if opcao[1] != nome:    #variável nome que serve para alternar a vez dos jogadores                                                      
                        nome = opcao[1]                    

                        ########## PECA UNITARIA ##########

                        if tamanho_peca == 1:   

                            ########## JOGADOR 1 ##########

                            if nome == lista_jogo[0]:   
                                if lista_tabela[0][colunas] == "|___|":    #verifica se a coluna inserida está cheia
                                    ultimo_elemento_vazio = 1
                                    for i in range(len(lista_tabela)):      #loop para verificar os elementos vazios da coluna e no final inserir a jogada
                                        if lista_tabela[i][colunas] == "|___|":
                                            ultimo_elemento_vazio = i
                                        else:
                                            break
                                    lista_tabela[ultimo_elemento_vazio][colunas] = "| X |"
                                    print("Peça colocada.")

                                    ##########  HORIZONTAL ##########

                                    for i in range(len(lista_tabela)):
                                        for j in range(len(lista_tabela[i])):    #itera todos os valores da lista em base de linhas
                                            if horizontal != sequencia_vencedora:   #verifica se o variavel é igual a sequencia vencedora
                                                if lista_tabela[i][j] == "| X |":
                                                    horizontal += 1 
                                                    if horizontal == sequencia_vencedora:   #segunda verificação
                                                        print("Sequência conseguida. Jogo terminado.")
                                                        lista_jogo.clear()
                                                        lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                        lista_pecas_especiais_j2.clear()
                                                        lista_tabela.clear()
                                                        break
                                                else:
                                                    horizontal = 0
                                        
                                        if horizontal == sequencia_vencedora:   #serve para dar break da iteração das linhas
                                            break

                                    ########## VITORIA VERTICAL ##########

                                    for j in range(len(lista_tabela[0])):
                                        for i in range(len(lista_tabela)):  #itera todos os valores da lista em base de colunas
                                            if vertical != sequencia_vencedora:     #verifica se o variavel é igual a sequencia vencedora
                                                if lista_tabela[i][j] == "| X |":
                                                    vertical += 1 
                                                    if vertical == sequencia_vencedora:     #segunda verificação
                                                        print("Sequência conseguida. Jogo terminado.")
                                                        lista_jogo.clear()
                                                        lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                        lista_pecas_especiais_j2.clear()
                                                        lista_tabela.clear()
                                                        break
                                                        #Adicionar os pontos ao vencedor e o jogo jogado aos dois!
                                                else:
                                                    vertical = 0
                                        if vertical == sequencia_vencedora:   #serve para dar break da iteração das colunas
                                            break
                                    
                                    ########## VITORIA DIAGONAL ##########
                                    
                                    diagonal = [lista_tabela[i][len(lista_tabela) - 1 - i] for i in range(len(lista_tabela))]     
                                    if diagonal.count("| X |") == sequencia_vencedora:
                                        print("Sequência conseguida. Jogo terminado.")
                                        lista_jogo.clear()
                                        lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                        lista_pecas_especiais_j2.clear()
                                        lista_tabela.clear()
                                        #Adicionar os pontos ao vencedor e o jogo jogado aos dois!
                                        
                                    else:
                                        pass
                                else:
                                    print("Posição irregular.")
                                    nome = lista_jogo[1]    #mudar o valor do nome para o jogador adversário para que o jogador posso tentar denovo 

                            ########## JOGADOR 2 ##########

                            elif nome == lista_jogo[1]:
                                if lista_tabela[0][colunas] == "|___|":    #verifica se a coluna inserida está cheia 
                                    ultimo_elemento_vazio = 1
                                    for i in range(len(lista_tabela)):      #loop para verificar os elementos vazios da coluna e no final inserir a jogada
                                        if lista_tabela[i][colunas] == "|___|":
                                            ultimo_elemento_vazio = i
                                        else:
                                            break
                                    lista_tabela[ultimo_elemento_vazio][colunas] = "| O |"    
                                    print("Peça colocada.")
            

                                    ########## VITORIA HORIZONTAL ##########

                                    for i in range(len(lista_tabela)):      #itera todos os valores da lista em base das linhas
                                        for j in range(len(lista_tabela[i])):
                                            if horizontal != sequencia_vencedora:   #verifica se o variavel é igual a sequencia vencedora
                                                if lista_tabela[i][j] == "| O |":
                                                    horizontal += 1 
                                                    if horizontal == sequencia_vencedora:   #segunda verificação
                                                        print("Sequência conseguida. Jogo terminado.")
                                                        lista_jogo.clear()
                                                        lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                        lista_pecas_especiais_j2.clear()
                                                        lista_tabela.clear()
                                                        break
                                                else:
                                                    horizontal = 0
                                        
                                        if horizontal == sequencia_vencedora:   #serve para dar break da iteração das linhas
                                            break
                                    
                                    ########## VITORIA VERTICAL ##########

                                    for j in range(len(lista_tabela[0])):   #itera todos os valores da lista em base das colunas
                                        for i in range(len(lista_tabela)):
                                            if vertical != sequencia_vencedora:     #verifica se o variavel é igual a sequencia vencedora
                                                if lista_tabela[i][j] == "| X |":
                                                    vertical += 1 
                                                    if vertical == sequencia_vencedora:     #segunda verificação
                                                        print("Sequência conseguida. Jogo terminado.")
                                                        lista_jogo.clear()
                                                        lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                        lista_pecas_especiais_j2.clear()
                                                        lista_tabela.clear()
                                                        break
                                                        #Adicionar os pontos ao vencedor e o jogo jogado aos dois!
                                                else:
                                                    vertical = 0
                                        if vertical == sequencia_vencedora:    #serve para dar break da iteração das colunas
                                            break
                                    
                                    ########## VITORIA DIAGONAL ##########

                                    diagonal = [lista_tabela[i][len(lista_tabela) - 1 - i] for i in range(len(lista_tabela))]     
                                    if diagonal.count("| O |") == sequencia_vencedora:
                                        print("Sequência conseguida. Jogo terminado.")
                                        lista_jogo.clear()
                                        lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                        lista_pecas_especiais_j2.clear()
                                        lista_tabela.clear()                                                                                                                                                                                                                                                                                                                                                                                                                                
                                        #Adicionar os pontos ao vencedor e o jogo jogado aos dois!
                                    else:
                                        pass
                                else:
                                    print("Posição irregular.")
                                    nome = lista_jogo[0]    #mudar o valor do nome para o jogador adversário para que o jogador posso tentar denovo 


                        ########## PEÇA ESPECIAL ##########

                        elif (tamanho_peca != 1):

                            ########## JOGADOR 1 ########## 

                            if nome == lista_jogo[0]: 
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

                                                ########## VITORIA HORIZONTAL ##########

                                                for i in range(len(lista_tabela)):
                                                    for j in range(len(lista_tabela[i])):   #itera todos os valores da lista
                                                        if horizontal != sequencia_vencedora:   #verifica se o variavel é igual a sequencia vencedora
                                                            if lista_tabela[i][j] == "| X |":
                                                                horizontal += 1 
                                                                if horizontal == sequencia_vencedora:   #segunda verificação
                                                                    print("Sequência conseguida. Jogo terminado.")
                                                                    lista_jogo.clear()
                                                                    lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                                    lista_pecas_especiais_j2.clear()
                                                                    lista_tabela.clear()
                                                                    break
                                                            else:
                                                                horizontal = 0
                                        
                                                    if horizontal == sequencia_vencedora:   #serve para dar break da iteração das linhas
                                                        break

                                                ########## VITORIA VERTICAL ##########
                                                    
                                                for j in range(len(lista_tabela[0])):   #itera todos os valores da lista em base das colunas
                                                    for i in range(len(lista_tabela)):
                                                        if vertical != sequencia_vencedora:     #verifica se o variavel é igual a sequencia vencedora
                                                            if lista_tabela[i][j] == "| X |":
                                                                vertical += 1 
                                                                if vertical == sequencia_vencedora:    #segunda verificação
                                                                    print("Sequência conseguida. Jogo terminado.")
                                                                    lista_jogo.clear()
                                                                    lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                                    lista_pecas_especiais_j2.clear()
                                                                    lista_tabela.clear()
                                                                    break
                                                                    #Adicionar os pontos ao vencedor e o jogo jogado aos dois!
                                                            else:
                                                                vertical = 0
                                                    if vertical == sequencia_vencedora:    #serve para dar break da iteração das colunas
                                                        break
                                                
                                                ########## VITORIA DIAGONAL ##########

                                                diagonal = [lista_tabela[i][len(lista_tabela) - 1 - i] for i in range(len(lista_tabela))]     
                                                if diagonal.count("| X |") == sequencia_vencedora:
                                                    print("Sequência conseguida. Jogo terminado.")
                                                    lista_jogo.clear()
                                                    lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                    lista_pecas_especiais_j2.clear()
                                                    lista_tabela.clear()
                                                    #Adicionar os pontos ao vencedor e o jogo jogado aos dois!
                                                else:
                                                    pass 
                                                
                                                if len(lista_tabela) != 0 and (tamanho_peca in lista_pecas_especiais_j1): 
                                                    lista_pecas_especiais_j1.remove(tamanho_peca)    #limpar a peça especial usada
                                                else:
                                                    pass
                                            
                                            else:
                                                print("Posição irregular.")
                                                nome = lista_jogo[1]    #mudar o valor do nome para o jogador adversário para que o jogador posso tentar denovo   
                                                   
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

                                                ########## VITORIA HORIZONTAL ##########

                                                for i in range(len(lista_tabela)):     
                                                    for j in range(len(lista_tabela[i])):       #itera todos os valores da lista em base das linhas
                                                        if horizontal != sequencia_vencedora:   #verifica se o variavel é igual a sequencia vencedora
                                                            if lista_tabela[i][j] == "| X |":
                                                                horizontal += 1 
                                                                if horizontal == sequencia_vencedora:   #segunda verificação
                                                                    print("Sequência conseguida. Jogo terminado.")
                                                                    lista_jogo.clear()
                                                                    lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                                    lista_pecas_especiais_j2.clear()
                                                                    lista_tabela.clear()
                                                                    break
                                                            else:
                                                                horizontal = 0  
                                                    
                                                    if horizontal == sequencia_vencedora:   #serve para dar break da iteração das linhas
                                                        break
                                                
                                                ########## VITORIA VERTICAL ##########

                                                for j in range(len(lista_tabela[0])):   #itera todos os valores da lista em base das colunas
                                                    for i in range(len(lista_tabela)):
                                                        if vertical != sequencia_vencedora:     #verifica se o variavel é igual a sequencia vencedora
                                                            if lista_tabela[i][j] == "| X |":
                                                                vertical += 1 
                                                                if vertical == sequencia_vencedora:   #segunda verificação  
                                                                    print("Sequência conseguida. Jogo terminado.")  
                                                                    lista_jogo.clear()
                                                                    lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                                    lista_pecas_especiais_j2.clear()
                                                                    lista_tabela.clear()
                                                                    break
                                                                    #Adicionar os pontos ao vencedor e o jogo jogado aos dois!
                                                            else:
                                                                vertical = 0
                                                    if vertical == sequencia_vencedora:     #serve para dar break da iteração das colunas
                                                        break
                                                
                                                ########## VITORIA DIAGONAL ##########

                                                diagonal = [lista_tabela[i][len(lista_tabela) - 1 - i] for i in range(len(lista_tabela))]     
                                                if diagonal.count("| X |") == sequencia_vencedora:
                                                    print("Sequência conseguida. Jogo terminado.")
                                                    lista_jogo.clear()
                                                    lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                    lista_pecas_especiais_j2.clear()
                                                    lista_tabela.clear()
                                                    #Adicionar os pontos ao vencedor e o jogo jogado aos dois!
                                                else:
                                                    pass
                                                
                                                if len(lista_tabela) != 0 and (tamanho_peca in lista_pecas_especiais_j1): 
                                                    lista_pecas_especiais_j1.remove(tamanho_peca)    #limpar a peça especial usada
                                                else:
                                                    pass
                                            else:
                                                print("Posição irregular.")
                                                nome = lista_jogo[1]    #mudar o valor do nome para o jogador adversário para que o jogador posso tentar denovo    
                                    else:
                                        print("Tamanho de peça não disponivel.")
                                        nome = lista_jogo[1]    #mudar o valor do nome para o jogador adversário para que o jogador posso tentar denovo
                                else: 
                                    print("O jogador não apresenta peças especiais disponiveis.")
                                    nome = lista_jogo[1]    #mudar o valor do nome para o jogador adversário para que o jogador posso tentar denovo

                            ########## JOGADOR 2 ##########

                            elif nome == lista_jogo[1]: 
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

                                                ########## VITORIA HORIZONTAL ##########
                                                
                                                for i in range(len(lista_tabela)):
                                                    for j in range(len(lista_tabela[i])):   #itera todos os valores da lista em base das linhas
                                                        if horizontal != sequencia_vencedora:   #verifica se o variavel é igual a sequencia vencedora
                                                            if lista_tabela[i][j] == "| O |":
                                                                horizontal += 1 
                                                                if horizontal == sequencia_vencedora:  #segunda verificação
                                                                    print("Sequência conseguida. Jogo terminado.")
                                                                    lista_jogo.clear()
                                                                    lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                                    lista_pecas_especiais_j2.clear()
                                                                    lista_tabela.clear()
                                                                    break
                                                            else:
                                                                horizontal = 0
                                                    
                                                    if horizontal == sequencia_vencedora: #serve para dar break da iteração das linhas  
                                                        break
                                                
                                                ########## VITORIA VERTICAL ##########
                                                
                                                for j in range(len(lista_tabela[0])):
                                                    for i in range(len(lista_tabela)):     #itera todos os valores da lista em base das colunas
                                                        if vertical != sequencia_vencedora:     #verifica se o variavel é igual a sequencia vencedora
                                                            if lista_tabela[i][j] == "| X |":
                                                                vertical += 1 
                                                                if vertical == sequencia_vencedora:    #segunda verificação
                                                                    print("Sequência conseguida. Jogo terminado.")
                                                                    lista_jogo.clear()
                                                                    lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                                    lista_pecas_especiais_j2.clear()
                                                                    lista_tabela.clear()
                                                                    break
                                                                    #Adicionar os pontos ao vencedor e o jogo jogado aos dois!
                                                            else:
                                                                vertical = 0
                                                    if vertical == sequencia_vencedora:   #serve para dar break da iteração das linhas
                                                        break
                                                
                                                ########## VITORIA DIAGONAL ##########
                                            
                                                diagonal = [lista_tabela[i][len(lista_tabela) - 1 - i] for i in range(len(lista_tabela))]     
                                                if diagonal.count("| O |") == sequencia_vencedora:
                                                    print("Sequência conseguida. Jogo terminado.")
                                                    lista_jogo.clear()
                                                    lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                    lista_pecas_especiais_j2.clear()
                                                    lista_tabela.clear()
                                                    #Adicionar os pontos ao vencedor e o jogo jogado aos dois!
                                                else:
                                                    pass
                                
                                                if len(lista_tabela) != 0 and (tamanho_peca in lista_pecas_especiais_j2): 
                                                    lista_pecas_especiais_j2.remove(tamanho_peca)    #limpar a peça especial usada
                                                else:
                                                    pass
                                            else:
                                                print("Posição irregular.")
                                                nome = lista_jogo[0]    #mudar o valor do nome para o jogador adversário para que o jogador posso tentar denovo   

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

                                                ########## VITORIA HORIZONTAL ##########

                                                for i in range(len(lista_tabela)):
                                                    for j in range(len(lista_tabela[i])):   #itera todos os valores da lista em base das linhas
                                                        if horizontal != sequencia_vencedora:   #verifica se o variavel é igual a sequencia vencedora
                                                            if lista_tabela[i][j] == "| O |":
                                                                horizontal += 1 
                                                                if horizontal == sequencia_vencedora:   #segunda verificação
                                                                    print("Sequência conseguida. Jogo terminado.")
                                                                    lista_jogo.clear()
                                                                    lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                                    lista_pecas_especiais_j2.clear()
                                                                    lista_tabela.clear()
                                                                    break
                                                                    #Adicionar os pontos ao vencedor e o jogo jogado aos dois!
                                                            else:
                                                                horizontal = 0
                                                    
                                                    if horizontal == sequencia_vencedora:   #serve para dar break da iteração das linhas
                                                        break
                                                
                                                ########## VITORIA VERTICAL ##########

                                                for j in range(len(lista_tabela[0])):   #itera todos os valores da lista em base das colunas
                                                    for i in range(len(lista_tabela)):
                                                        if vertical != sequencia_vencedora:     #verifica se o variavel é igual a sequencia vencedora
                                                            if lista_tabela[i][j] == "| X |":
                                                                vertical += 1 
                                                                if vertical == sequencia_vencedora:     #segunda verificação
                                                                    print("Sequência conseguida. Jogo terminado.")
                                                                    lista_jogo.clear()
                                                                    lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                                    lista_pecas_especiais_j2.clear()
                                                                    lista_tabela.clear()
                                                                    break
                                                                    #Adicionar os pontos ao vencedor e o jogo jogado aos dois!
                                                            else:
                                                                vertical = 0
                                                    if vertical == sequencia_vencedora:     #serve para dar break da iteração das colunas
                                                        break
                                                
                                                ########## VITORIA DIAGONAL ##########

                                                diagonal = [lista_tabela[i][len(lista_tabela) - 1 - i] for i in range(len(lista_tabela))]     
                                                if diagonal.count("| O |") == sequencia_vencedora:
                                                    print("Sequência conseguida. Jogo terminado.")
                                                    lista_jogo.clear()
                                                    lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                    lista_pecas_especiais_j2.clear()
                                                    lista_tabela.clear()
                                                    #Adicionar os pontos ao vencedor e o jogo jogado aos dois!
                                                else:
                                                    pass

                                                if len(lista_tabela) != 0 and (tamanho_peca in lista_pecas_especiais_j2): 
                                                    lista_pecas_especiais_j2.remove(tamanho_peca)    #limpar a peça especial usada
                                                else:
                                                    pass
                                            else:
                                                print("Posição irregular.")
                                                nome = lista_jogo[0]    #mudar o valor do nome para o jogador adversário para que o jogador posso tentar denovo
                                    else:
                                        print("Tamanho de peça não disponivel.")
                                        nome = lista_jogo[0]    #mudar o valor do nome para o jogador adversário para que o jogador posso tentar denovo
                                else:
                                    print("O jogador não apresenta peças especiais disponiveis.")
                                    nome = lista_jogo[0]    #mudar o valor do nome para o jogador adversário para que o jogador posso tentar denovo
                    else:
                        print('Não é possível jogar 2 vezes de seguida')                       
                else:
                    print('Jogador não participa no jogo em curso.')
            else:
                print('Não existe jogo em curso.')




            ########### VISUALIZAR RESULTADO #############

        elif opcao[0] == "v":                                                                                           
            if len(lista_tabela) != 0:
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
