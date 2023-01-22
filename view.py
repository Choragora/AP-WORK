from controller import *
import os

def main():
    
    ########### VARIAVEIS TEMPORARIAS ############
    
    lista_rj = ler_ficheiro_json("jogadores.json")
    lista_tabela = []
    lista_jogo = []
    lista_pecas_especiais_j1 = []
    lista_pecas_especiais_j2 = []            
    lista_sentidos = ["e", "d"]
    nome = 0
    horizontal = 0
    vertical = 0
    diagonal = 0
    diagonal_invertida = 0
    nome_vencedor = 0
    nome_vencedor_desistencia = 0
    nome_desistente = 0
    

    os.system("cls")
    while True: 
        
        
        opcao = input("Introduza a sua opção: ").lower().split(' ')

        
        ########### INICIAR JOGO ############

        if opcao[0] == "ij": 
            horizontal = 0
            vertical = 0
            diagonal = 0
            diagonal_invertida = 0
            comprimento = int(opcao[3])                              
            altura = int(opcao[4]) 
            sequencia_vencedora = int(opcao[5])
                                                                                       
            if len(lista_rj) > 1:                   #Verifica se a lista tem pelo menos dois jogadores registados
                if len(lista_tabela) == 0:          #Verifica se existe um jogo em curso                                                                                                                                       
                    lista_jogo = []                 #Lista onde serão armazenados os jogadores   

                    ########## NOMES ##########

                    if verificar_nomes(lista_rj, opcao[1]) == False and verificar_nomes(lista_rj, opcao[2]) == False:
                        lista_jogo.append(opcao[1])  #Se o jogador 1 e 2 estiverem na lista de jogadores, os mesmo 
                        lista_jogo.append(opcao[2])  #são adicionados à lista do jogo

                        ########## DIMENSOES ##########

                        if (comprimento/2 <= altura <= comprimento):        #Verifica as condições da dimensao da grelha
                            for i in range (altura):
                                lista_tabela.append(["|___|"] *comprimento) #Cria os slots da grelha
                                
                            ########## SEQUENCIA VENCEDORA ##########

                            if sequencia_vencedora != 1 and sequencia_vencedora != 2 and sequencia_vencedora < comprimento: #Verifica as condições da sequencia vencedora
                                
                               ########## PEÇAS ESPECIAIS ##########
                               
                                for peca in [int(i) for i in opcao[6:]]:    #Conta o numero de peças especiais introduzidas pelo utilizador 
                                    if peca < sequencia_vencedora and peca != 1:      #Verifica se a peça é inferior a sequencia vencedora e é diferente de 1
                                        pecas_especiais(peca, lista_pecas_especiais_j1, lista_pecas_especiais_j2)   #Peça especial adiciona à lista de peças especiais de cada jogador        
                                    else:
                                        print("Dimensões de peças especiais invalidas.")
                                        lista_pecas_especiais_j1.clear()
                                        lista_pecas_especiais_j2.clear()    
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

                else: 
                    print("Já existe um jogo em curso")
                
            else:
                print("É necessários estarem registados 2 jogadores.")
                
            

        ########### REGISTAR JOGADOR ############

        elif opcao[0] == "rj":    
            if verificar_nomes(lista_rj, opcao[1]) == True:    
                registar_jogador(opcao[1], lista_rj)
                bubble_sort(lista_rj) 
                guardar_ficheiro_json("jogadores.json", lista_rj)
                print("Jogador registado com sucesso.")
            else:
                print("Jogador existente.")



        ########### ELIMINAR JOGADOR ############
        
        elif opcao[0] == "ej":                                                                                   
            if len(lista_rj) != 0:                  #Verificação de número de jogadores
                if opcao[1] not in lista_jogo:      #Verifica se o nome está num jogo em curso
                    if verificar_nomes(lista_rj, opcao[1]) == False:       #verifica se o nome está registado                                                                
                        remover_jogador(opcao[1], lista_rj)
                        guardar_ficheiro_json("jogadores.json", lista_rj)                                                          
                        print("Jogador removido com sucesso.")
                    else:
                        print("Jogador não existente.")
                else:
                    print("Jogador participa no jogo em curso.")
            else:
                print("Não existem jogadores registados")



        ########### LISTAR JOGADOR ############

        elif opcao[0] == "lj":                                                                                                       
            if len(lista_rj) != 0:  #Verifica se existem jogadores registados
                for listagem in lista_rj:
                    print(listagem)
            else:
                print("Não existem jogadores registados.")


        ########### DETALHES JOGO ############

        elif opcao[0] == "dj":                                                                                          
            if len(lista_tabela) != 0:    #Verifica se existe jogo em curso
                print(f"Comprimento: {comprimento} | Altura: {altura}")
                print()

                ########## JOGADOR 1 ##########

                print(f"Nome: {lista_jogo[0]}") #Print do primeiro jogador da lista do jogo
                lista_dj_j1 = []
                for elemento in lista_pecas_especiais_j1:
                    if elemento not in lista_dj_j1: #Percorre a lista e verifica se cada elemento não está presente na lista_dj_j1 
                        contagem = lista_pecas_especiais_j1.count(elemento) #Conta o numero de ocorrencias desse elemento na lista_pecas_especiais_j1
                        lista_dj_j1.append(elemento)    #Adiciona-o na lista_dj_j1
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
            if len(lista_tabela) != 0:  #Verifica se existe um jogo em curso
                if len(opcao) == 3: #Ambos os jogadores desistem
                    if verificar_nomes(lista_rj, opcao[1]) == False and verificar_nomes(lista_rj, opcao[2]) == False:   #Verifica se ambos os jogadores estam presentes na lista
                        if opcao[1] in lista_jogo and opcao[2] in lista_jogo:
                            adicionar_jogos(lista_rj, opcao[1])
                            adicionar_jogos(lista_rj, opcao[2]) 
                            guardar_ficheiro_json("jogadores.json", lista_rj)
                            lista_jogo.clear()
                            lista_pecas_especiais_j1.clear()    #limpar o jogo em curso
                            lista_pecas_especiais_j2.clear()
                            lista_tabela.clear()
                            print('Desistência com sucesso. Jogo terminado.')

                        else:
                            print('Jogador não participa no jogo em curso.')
                    else:
                        print('Jogador não registado.')
                
                elif len(opcao) == 2:   #Apenas 1 jogador desiste
                    if verificar_nomes(lista_rj, opcao[1]) == False:
                        if opcao[1] in lista_jogo:
                            nome_desistente = opcao[1]    #O nome vencedor ganha o valor do ultimo a jogar
                            lista_jogo.remove(nome_desistente)    #Remove o jogador que ganhou
                            nome_vencedor_desistencia = lista_jogo[0]   #Para que possamos pegar o valor do jogador que perdeu
                            adicionar_pontos(lista_rj, nome_vencedor_desistencia)
                            adicionar_jogos(lista_rj, nome_desistente)
                            adicionar_jogos(lista_rj, nome_vencedor_desistencia) 
                            guardar_ficheiro_json("jogadores.json", lista_rj)
                            print('Desistência com sucesso. Jogo terminado.')
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
            tamanho_peca = int(opcao[2])    #Tamanho da peça que vai ser colocada
            colunas = int(opcao[3])         #A coluna onde a peça irá ser colocada                                                                                       
            if len(lista_tabela) != 0:      #verifica se existe jogo em curso
                if opcao[1] in lista_jogo:  #verifica se nome esta na lista de jogadores em curso

                    ########## MUDANCA DE JOGADOR ##########

                    if opcao[1] != nome:    #Variável nome que serve para alternar a vez dos jogadores                                                      
                        nome = opcao[1]                    

                        ########## PECA UNITARIA ##########

                        if tamanho_peca == 1:   

                            ########## JOGADOR 1 ##########

                            if nome == lista_jogo[0]:   
                                if lista_tabela[0][colunas] == "|___|":    #Verifica se a coluna inserida está cheia
                                    ultimo_elemento_vazio = 1
                                    for i in range(len(lista_tabela)):     #Loop para verificar os elementos vazios da coluna e no final inserir a jogada
                                        if lista_tabela[i][colunas] == "|___|":
                                            ultimo_elemento_vazio = i
                                        else:
                                            break
                                    lista_tabela[ultimo_elemento_vazio][colunas] = "| X |"
                                    print("Peça colocada.")

                                    ##########  HORIZONTAL ##########

                                    for i in range(len(lista_tabela)):
                                        for j in range(len(lista_tabela[i])):       #Itera todos os valores da lista em base de linhas
                                            if horizontal != sequencia_vencedora:   #Verifica se a variavel é diferente da sequencia vencedora
                                                if lista_tabela[i][j] == "| X |":
                                                    horizontal += 1                         #Controlar o número de elementos = X que se encontram de seguida
                                                    if horizontal == sequencia_vencedora:   #Segunda verificação 
                                                        nome_vencedor = nome                #O nome vencedor ganha o valor do ultimo a jogar
                                                        lista_jogo.remove(nome_vencedor)    #Remove o jogador que ganhou
                                                        nome_perdedor = lista_jogo[0]       #Para que possamos pegar o valor do jogador que perdeu
                                                        adicionar_pontos(lista_rj, nome_vencedor)
                                                        adicionar_jogos(lista_rj, nome_vencedor)
                                                        adicionar_jogos(lista_rj, nome_perdedor) 
                                                        guardar_ficheiro_json("jogadores.json", lista_rj)
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

                                    if horizontal != sequencia_vencedora:
                                        for j in range(len(lista_tabela[0])):
                                            for i in range(len(lista_tabela)):          #Itera todos os valores da lista em base de colunas
                                                if vertical != sequencia_vencedora:     #Verifica se o variavel é igual a sequencia vencedora
                                                    if lista_tabela[i][j] == "| X |":
                                                        vertical += 1                           #Controlar o número de elementos = X que se encontram de seguida
                                                        if horizontal == sequencia_vencedora:   #Segunda verificação
                                                            nome_vencedor = nome                #O nome vencedor ganha o valor do ultimo a jogar
                                                            lista_jogo.remove(nome_vencedor)    #Remove o jogador que ganhou
                                                            nome_perdedor = lista_jogo[0]       #Para que possamos pegar o valor do jogador que perdeu
                                                            adicionar_pontos(lista_rj, nome_vencedor)
                                                            adicionar_jogos(lista_rj, nome_vencedor)
                                                            adicionar_jogos(lista_rj, nome_perdedor) 
                                                            guardar_ficheiro_json("jogadores.json", lista_rj)
                                                            print("Sequência conseguida. Jogo terminado.")
                                                            lista_jogo.clear()
                                                            lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                            lista_pecas_especiais_j2.clear()
                                                            lista_tabela.clear()
                                                            break
                                                    else:
                                                        vertical = 0
                                            if vertical == sequencia_vencedora:   #serve para dar break da iteração das colunas
                                                break
                                    
                                    ########## VITORIA DIAGONAL ##########

                                    if horizontal != sequencia_vencedora and vertical != sequencia_vencedora:
                                        for i in range(len(lista_tabela)):
                                            for j in range(len(lista_tabela[i])):   #verifica todos os elementos da tabela
                                                if lista_tabela[i][j] == "| X |":   #caso encontre um X na verificação vai passar à verificação de qunatos se encontram de seguida
                                                    for k in range(1,sequencia_vencedora):
                                                        if i+k < len(lista_tabela) and j+k < len(lista_tabela[i]) and lista_tabela[i+k][j+k] == "| X |":
                                                            diagonal +=1                ##Controlar o número de elementos = X que se encontram de seguida
                                                            if diagonal == sequencia_vencedora-1:
                                                                nome_perdedor = lista_jogo[0] 
                                                                nome_vencedor = nome    #o nome vencedor ganha o valor do ultimo a jogar
                                                                lista_jogo.remove(nome_vencedor)    #remove o jogador que ganhou
                                                                nome_perdedor = lista_jogo[0]   #para que possamos pegar o valor do jogador que perdeu
                                                                adicionar_pontos(lista_rj, nome_vencedor)
                                                                adicionar_jogos(lista_rj, nome_vencedor)
                                                                adicionar_jogos(lista_rj, nome_perdedor) 
                                                                guardar_ficheiro_json("jogadores.json", lista_rj)
                                                                print("Sequência conseguida. Jogo terminado.")
                                                                lista_jogo.clear()
                                                                lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                                lista_pecas_especiais_j2.clear()
                                                                lista_tabela.clear()
                                                                break #break k
                                                        else:
                                                            diagonal = 0 
                                                            break
                                                    
                                                    if diagonal == sequencia_vencedora: #break j
                                                        break

                                            if diagonal == sequencia_vencedora: #breaj i
                                                break

                                        if horizontal != sequencia_vencedora and vertical != sequencia_vencedora and diagonal != sequencia_vencedora:
                                            for i in range(len(lista_tabela)-1, -1, -1):
                                                for j in range(len(lista_tabela[i])-1, -1, -1):      #verifica todos os elementos da tabela
                                                    if lista_tabela[i][j] == "| X |":                #caso encontre um X na verificação vai passar à verificação de qunatos se encontram de seguida
                                                        diagonal_invertida = 0
                                                        for k in range(1, sequencia_vencedora):
                                                            if i-k >= 0 and j+k < len(lista_tabela[i]) and lista_tabela[i-k][j+k] == "| X |":
                                                                diagonal_invertida += 1    #Controlar o número de elementos = X que se encontram de seguida
                                                                if diagonal_invertida == sequencia_vencedora-1:
                                                                    nome_perdedor = lista_jogo[0]
                                                                    nome_vencedor = nome    #o nome vencedor ganha o valor do ultimo a jogar
                                                                    lista_jogo.remove(nome_vencedor)    #remove o jogador que ganhou
                                                                    nome_perdedor = lista_jogo[0]   #para que possamos pegar o valor do jogador que perdeu
                                                                    adicionar_pontos(lista_rj, nome_vencedor)
                                                                    adicionar_jogos(lista_rj, nome_vencedor)
                                                                    adicionar_jogos(lista_rj, nome_perdedor) 
                                                                    guardar_ficheiro_json("jogadores.json", lista_rj)
                                                                    print("Sequência conseguida. Jogo terminado.")
                                                                    lista_jogo.clear()
                                                                    lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                                    lista_pecas_especiais_j2.clear()
                                                                    lista_tabela.clear()
                                                                    break #break k
                                                            else:
                                                                diagonal_invertida = 0
                                                                break

                                                        if diagonal_invertida == sequencia_vencedora: #break j
                                                            break
                                                        
                                                if diagonal_invertida == sequencia_vencedora: #break i
                                                    break
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
                                                        nome_vencedor = nome    #o nome vencedor ganha o valor do ultimo a jogar
                                                        lista_jogo.remove(nome_vencedor)    #remove o jogador que ganhou
                                                        nome_perdedor = lista_jogo[0]   #para que possamos pegar o valor do jogador que perdeu
                                                        adicionar_pontos(lista_rj, nome_vencedor)
                                                        adicionar_jogos(lista_rj, nome_vencedor)
                                                        adicionar_jogos(lista_rj, nome_perdedor) 
                                                        guardar_ficheiro_json("jogadores.json", lista_rj)
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
                                    
                                    if horizontal != sequencia_vencedora:
                                        for j in range(len(lista_tabela[0])):   #itera todos os valores da lista em base das colunas
                                            for i in range(len(lista_tabela)):
                                                if vertical != sequencia_vencedora:     #verifica se o variavel é igual a sequencia vencedora
                                                    if lista_tabela[i][j] == "| O |":
                                                        vertical += 1 
                                                        if vertical == sequencia_vencedora:     #segunda verificação
                                                            nome_vencedor = nome    #o nome vencedor ganha o valor do ultimo a jogar
                                                            lista_jogo.remove(nome_vencedor)    #remove o jogador que ganhou
                                                            nome_perdedor = lista_jogo[0]   #para que possamos pegar o valor do jogador que perdeu
                                                            adicionar_pontos(lista_rj, nome_vencedor)
                                                            adicionar_jogos(lista_rj, nome_vencedor)
                                                            adicionar_jogos(lista_rj, nome_perdedor) 
                                                            guardar_ficheiro_json("jogadores.json", lista_rj)
                                                            print("Sequência conseguida. Jogo terminado.")
                                                            lista_jogo.clear()
                                                            lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                            lista_pecas_especiais_j2.clear()
                                                            lista_tabela.clear()
                                                            break
                                                            
                                                    else:
                                                        vertical = 0
                                            if vertical == sequencia_vencedora:    #serve para dar break da iteração das colunas
                                                break
                                    
                                    ########## VITORIA DIAGONAL ##########
                                    
                                    if horizontal != sequencia_vencedora and vertical != sequencia_vencedora:
                                        for i in range(len(lista_tabela)):
                                            for j in range(len(lista_tabela[i])):
                                                if lista_tabela[i][j] == "| O |":
                                                    for k in range(1,sequencia_vencedora):
                                                        if i+k < len(lista_tabela) and j+k < len(lista_tabela[i]) and lista_tabela[i+k][j+k] == "| O |":
                                                            diagonal +=1
                                                            if diagonal == sequencia_vencedora-1:
                                                                nome_perdedor = lista_jogo[0] 
                                                                nome_vencedor = nome    #o nome vencedor ganha o valor do ultimo a jogar
                                                                lista_jogo.remove(nome_vencedor)    #remove o jogador que ganhou
                                                                nome_perdedor = lista_jogo[0]   #para que possamos pegar o valor do jogador que perdeu
                                                                adicionar_pontos(lista_rj, nome_vencedor)
                                                                adicionar_jogos(lista_rj, nome_vencedor)
                                                                adicionar_jogos(lista_rj, nome_perdedor) 
                                                                guardar_ficheiro_json("jogadores.json", lista_rj)
                                                                print("Sequência conseguida. Jogo terminado.")
                                                                lista_jogo.clear()
                                                                lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                                lista_pecas_especiais_j2.clear()
                                                                lista_tabela.clear()
                                                                break #break k
                                                        else:
                                                            diagonal = 0
                                                            break
                                                    
                                                    if diagonal == sequencia_vencedora: #break j
                                                        break

                                            if diagonal == sequencia_vencedora: #breaj i
                                                break

                                    if horizontal != sequencia_vencedora and vertical != sequencia_vencedora and diagonal != sequencia_vencedora:
                                            for i in range(len(lista_tabela)-1, -1, -1):
                                                for j in range(len(lista_tabela[i])-1, -1, -1):
                                                    if lista_tabela[i][j] == "| O |":
                                                        diagonal_invertida = 0
                                                        for k in range(1, sequencia_vencedora):
                                                            if i-k >= 0 and j+k < len(lista_tabela[i]) and lista_tabela[i-k][j+k] == "| O |":
                                                                diagonal_invertida += 1
                                                                if diagonal_invertida == sequencia_vencedora-1:
                                                                    nome_perdedor = lista_jogo[0]
                                                                    nome_vencedor = nome    #o nome vencedor ganha o valor do ultimo a jogar
                                                                    lista_jogo.remove(nome_vencedor)    #remove o jogador que ganhou
                                                                    nome_perdedor = lista_jogo[0]   #para que possamos pegar o valor do jogador que perdeu
                                                                    adicionar_pontos(lista_rj, nome_vencedor)
                                                                    adicionar_jogos(lista_rj, nome_vencedor)
                                                                    adicionar_jogos(lista_rj, nome_perdedor) 
                                                                    guardar_ficheiro_json("jogadores.json", lista_rj)
                                                                    print("Sequência conseguida. Jogo terminado.")
                                                                    lista_jogo.clear()
                                                                    lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                                    lista_pecas_especiais_j2.clear()
                                                                    lista_tabela.clear()
                                                                    break #break k
                                                            else:
                                                                diagonal_invertida = 0
                                                                break

                                                        if diagonal_invertida == sequencia_vencedora: #break j
                                                            break
                                                        
                                                if diagonal_invertida == sequencia_vencedora: #break i
                                                    break

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
                                                                    nome_vencedor = nome    #o nome vencedor ganha o valor do ultimo a jogar
                                                                    lista_jogo.remove(nome_vencedor)    #remove o jogador que ganhou
                                                                    nome_perdedor = lista_jogo[0]   #para que possamos pegar o valor do jogador que perdeu
                                                                    adicionar_pontos(lista_rj, nome_vencedor)
                                                                    adicionar_jogos(lista_rj, nome_vencedor)
                                                                    adicionar_jogos(lista_rj, nome_perdedor) 
                                                                    guardar_ficheiro_json("jogadores.json", lista_rj)
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
                                                
                                                if horizontal != sequencia_vencedora:
                                                    for j in range(len(lista_tabela[0])):   #itera todos os valores da lista em base das colunas
                                                        for i in range(len(lista_tabela)):
                                                            if vertical != sequencia_vencedora:     #verifica se o variavel é igual a sequencia vencedora
                                                                if lista_tabela[i][j] == "| X |":
                                                                    vertical += 1 
                                                                    if vertical == sequencia_vencedora:    #segunda verificação
                                                                        nome_vencedor = nome    #o nome vencedor ganha o valor do ultimo a jogar
                                                                        lista_jogo.remove(nome_vencedor)    #remove o jogador que ganhou
                                                                        nome_perdedor = lista_jogo[0]   #para que possamos pegar o valor do jogador que perdeu
                                                                        adicionar_pontos(lista_rj, nome_vencedor)
                                                                        adicionar_jogos(lista_rj, nome_vencedor)
                                                                        adicionar_jogos(lista_rj, nome_perdedor) 
                                                                        guardar_ficheiro_json("jogadores.json", lista_rj)
                                                                        print("Sequência conseguida. Jogo terminado.")
                                                                        lista_jogo.clear()
                                                                        lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                                        lista_pecas_especiais_j2.clear()
                                                                        lista_tabela.clear()
                                                                        break
                                                                        
                                                                else:
                                                                    vertical = 0
                                                        if vertical == sequencia_vencedora:    #serve para dar break da iteração das colunas
                                                            break
                                                
                                                ########## VITORIA DIAGONAL ##########                                                
                                                
                                                if horizontal != sequencia_vencedora and vertical != sequencia_vencedora:
                                                    for i in range(len(lista_tabela)):
                                                        for j in range(len(lista_tabela[i])):
                                                            if lista_tabela[i][j] == "| X |":
                                                                for k in range(1,sequencia_vencedora):
                                                                    if i+k < len(lista_tabela) and j+k < len(lista_tabela[i]) and lista_tabela[i+k][j+k] == "| O |":
                                                                        diagonal +=1
                                                                        if diagonal == sequencia_vencedora-1:
                                                                            nome_perdedor = lista_jogo[0] 
                                                                            nome_vencedor = nome    #o nome vencedor ganha o valor do ultimo a jogar
                                                                            lista_jogo.remove(nome_vencedor)    #remove o jogador que ganhou
                                                                            nome_perdedor = lista_jogo[0]   #para que possamos pegar o valor do jogador que perdeu
                                                                            adicionar_pontos(lista_rj, nome_vencedor)
                                                                            adicionar_jogos(lista_rj, nome_vencedor)
                                                                            adicionar_jogos(lista_rj, nome_perdedor) 
                                                                            guardar_ficheiro_json("jogadores.json", lista_rj)
                                                                            print("Sequência conseguida. Jogo terminado.")
                                                                            lista_jogo.clear()
                                                                            lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                                            lista_pecas_especiais_j2.clear()
                                                                            lista_tabela.clear()
                                                                            break #break k
                                                                    else:
                                                                        diagonal = 0
                                                                        break
                                                                
                                                                if diagonal == sequencia_vencedora: #break j
                                                                    break

                                                        if diagonal == sequencia_vencedora: #breaj i
                                                            break

                                                    if horizontal != sequencia_vencedora and vertical != sequencia_vencedora and diagonal != sequencia_vencedora:
                                                        for i in range(len(lista_tabela)-1, -1, -1):
                                                            for j in range(len(lista_tabela[i])-1, -1, -1):
                                                                if lista_tabela[i][j] == "| X |":
                                                                    diagonal_invertida = 0
                                                                    for k in range(1, sequencia_vencedora):
                                                                        if i-k >= 0 and j+k < len(lista_tabela[i]) and lista_tabela[i-k][j+k] == "| X |":
                                                                            diagonal_invertida += 1
                                                                            if diagonal_invertida == sequencia_vencedora-1:
                                                                                nome_perdedor = lista_jogo[0]
                                                                                nome_vencedor = nome    #o nome vencedor ganha o valor do ultimo a jogar
                                                                                lista_jogo.remove(nome_vencedor)    #remove o jogador que ganhou
                                                                                nome_perdedor = lista_jogo[0]   #para que possamos pegar o valor do jogador que perdeu
                                                                                adicionar_pontos(lista_rj, nome_vencedor)
                                                                                adicionar_jogos(lista_rj, nome_vencedor)
                                                                                adicionar_jogos(lista_rj, nome_perdedor) 
                                                                                guardar_ficheiro_json("jogadores.json", lista_rj)
                                                                                print("Sequência conseguida. Jogo terminado.")
                                                                                lista_jogo.clear()
                                                                                lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                                                lista_pecas_especiais_j2.clear()
                                                                                lista_tabela.clear()
                                                                                break #break k
                                                                        else:
                                                                            diagonal_invertida = 0
                                                                            break

                                                                    if diagonal_invertida == sequencia_vencedora: #break j
                                                                        break
                                                                    
                                                            if diagonal_invertida == sequencia_vencedora: #break i
                                                                break                                   
                                                
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
                                                                    nome_vencedor = nome    #o nome vencedor ganha o valor do ultimo a jogar
                                                                    lista_jogo.remove(nome_vencedor)    #remove o jogador que ganhou
                                                                    nome_perdedor = lista_jogo[0]   #para que possamos pegar o valor do jogador que perdeu
                                                                    adicionar_pontos(lista_rj, nome_vencedor)
                                                                    adicionar_jogos(lista_rj, nome_vencedor)
                                                                    adicionar_jogos(lista_rj, nome_perdedor) 
                                                                    guardar_ficheiro_json("jogadores.json", lista_rj)
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
                                                
                                                if horizontal != sequencia_vencedora:
                                                    for j in range(len(lista_tabela[0])):   #itera todos os valores da lista em base das colunas
                                                        for i in range(len(lista_tabela)):
                                                            if vertical != sequencia_vencedora:     #verifica se o variavel é igual a sequencia vencedora
                                                                if lista_tabela[i][j] == "| X |":
                                                                    vertical += 1 
                                                                    if vertical == sequencia_vencedora:   #segunda verificação
                                                                        nome_vencedor = nome    #o nome vencedor ganha o valor do ultimo a jogar
                                                                        lista_jogo.remove(nome_vencedor)    #remove o jogador que ganhou
                                                                        nome_perdedor = lista_jogo[0]   #para que possamos pegar o valor do jogador que perdeu
                                                                        adicionar_pontos(lista_rj, nome_vencedor)
                                                                        adicionar_jogos(lista_rj, nome_vencedor)
                                                                        adicionar_jogos(lista_rj, nome_perdedor) 
                                                                        guardar_ficheiro_json("jogadores.json", lista_rj)  
                                                                        print("Sequência conseguida. Jogo terminado.")  
                                                                        lista_jogo.clear()
                                                                        lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                                        lista_pecas_especiais_j2.clear()
                                                                        lista_tabela.clear()
                                                                        break
                                                                        
                                                                else:
                                                                    vertical = 0
                                                        if vertical == sequencia_vencedora:     #serve para dar break da iteração das colunas
                                                            break
                                                
                                                ########## VITORIA DIAGONAL ##########

                                                if horizontal != sequencia_vencedora and vertical != sequencia_vencedora:
                                                    for i in range(len(lista_tabela)):
                                                        for j in range(len(lista_tabela[i])):
                                                            if lista_tabela[i][j] == "| X |":
                                                                for k in range(1,sequencia_vencedora):
                                                                    if i+k < len(lista_tabela) and j+k < len(lista_tabela[i]) and lista_tabela[i+k][j+k] == "| O |":
                                                                        diagonal +=1
                                                                        if diagonal == sequencia_vencedora-1:
                                                                            nome_perdedor = lista_jogo[0] 
                                                                            nome_vencedor = nome    #o nome vencedor ganha o valor do ultimo a jogar
                                                                            lista_jogo.remove(nome_vencedor)    #remove o jogador que ganhou
                                                                            nome_perdedor = lista_jogo[0]   #para que possamos pegar o valor do jogador que perdeu
                                                                            adicionar_pontos(lista_rj, nome_vencedor)
                                                                            adicionar_jogos(lista_rj, nome_vencedor)
                                                                            adicionar_jogos(lista_rj, nome_perdedor) 
                                                                            guardar_ficheiro_json("jogadores.json", lista_rj)
                                                                            print("Sequência conseguida. Jogo terminado.")
                                                                            lista_jogo.clear()
                                                                            lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                                            lista_pecas_especiais_j2.clear()
                                                                            lista_tabela.clear()
                                                                            break #break k
                                                                    else:
                                                                        diagonal = 0
                                                                        break
                                                                
                                                                if diagonal == sequencia_vencedora: #break j
                                                                    break

                                                        if diagonal == sequencia_vencedora: #breaj i
                                                            break

                                                    if horizontal != sequencia_vencedora and vertical != sequencia_vencedora and diagonal != sequencia_vencedora:
                                                        for i in range(len(lista_tabela)-1, -1, -1):
                                                            for j in range(len(lista_tabela[i])-1, -1, -1):
                                                                if lista_tabela[i][j] == "| X |":
                                                                    diagonal_invertida = 0
                                                                    for k in range(1, sequencia_vencedora):
                                                                        if i-k >= 0 and j+k < len(lista_tabela[i]) and lista_tabela[i-k][j+k] == "| X |":
                                                                            diagonal_invertida += 1
                                                                            if diagonal_invertida == sequencia_vencedora-1:
                                                                                nome_perdedor = lista_jogo[0]
                                                                                nome_vencedor = nome    #o nome vencedor ganha o valor do ultimo a jogar
                                                                                lista_jogo.remove(nome_vencedor)    #remove o jogador que ganhou
                                                                                nome_perdedor = lista_jogo[0]   #para que possamos pegar o valor do jogador que perdeu
                                                                                adicionar_pontos(lista_rj, nome_vencedor)
                                                                                adicionar_jogos(lista_rj, nome_vencedor)
                                                                                adicionar_jogos(lista_rj, nome_perdedor) 
                                                                                guardar_ficheiro_json("jogadores.json", lista_rj)
                                                                                print("Sequência conseguida. Jogo terminado.")
                                                                                lista_jogo.clear()
                                                                                lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                                                lista_pecas_especiais_j2.clear()
                                                                                lista_tabela.clear()
                                                                                break #break k
                                                                        else:
                                                                            diagonal_invertida = 0
                                                                            break

                                                                    if diagonal_invertida == sequencia_vencedora: #break j
                                                                        break
                                                                    
                                                            if diagonal_invertida == sequencia_vencedora: #break i
                                                                break                    
                                                    
                                                
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
                                                                    nome_vencedor = nome    #o nome vencedor ganha o valor do ultimo a jogar
                                                                    lista_jogo.remove(nome_vencedor)    #remove o jogador que ganhou
                                                                    nome_perdedor = lista_jogo[0]   #para que possamos pegar o valor do jogador que perdeu
                                                                    adicionar_pontos(lista_rj, nome_vencedor)
                                                                    adicionar_jogos(lista_rj, nome_vencedor)
                                                                    adicionar_jogos(lista_rj, nome_perdedor) 
                                                                    guardar_ficheiro_json("jogadores.json", lista_rj)
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
                                                
                                                if horizontal != sequencia_vencedora:
                                                    for j in range(len(lista_tabela[0])):
                                                        for i in range(len(lista_tabela)):     #itera todos os valores da lista em base das colunas
                                                            if vertical != sequencia_vencedora:     #verifica se o variavel é igual a sequencia vencedora
                                                                if lista_tabela[i][j] == "| O |":
                                                                    vertical += 1 
                                                                    if vertical == sequencia_vencedora:    #segunda verificação
                                                                        nome_vencedor = nome    #o nome vencedor ganha o valor do ultimo a jogar
                                                                        lista_jogo.remove(nome_vencedor)    #remove o jogador que ganhou
                                                                        nome_perdedor = lista_jogo[0]   #para que possamos pegar o valor do jogador que perdeu
                                                                        adicionar_pontos(lista_rj, nome_vencedor)
                                                                        adicionar_jogos(lista_rj, nome_vencedor)
                                                                        adicionar_jogos(lista_rj, nome_perdedor) 
                                                                        guardar_ficheiro_json("jogadores.json", lista_rj)
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

                                                if horizontal != sequencia_vencedora and vertical != sequencia_vencedora:
                                                    for i in range(len(lista_tabela)):
                                                        for j in range(len(lista_tabela[i])):
                                                            if lista_tabela[i][j] == "| O |":
                                                                for k in range(1,sequencia_vencedora):
                                                                    if i+k < len(lista_tabela) and j+k < len(lista_tabela[i]) and lista_tabela[i+k][j+k] == "| O |":
                                                                        diagonal +=1
                                                                        if diagonal == sequencia_vencedora-1:
                                                                            nome_perdedor = lista_jogo[0] 
                                                                            nome_vencedor = nome    #o nome vencedor ganha o valor do ultimo a jogar
                                                                            lista_jogo.remove(nome_vencedor)    #remove o jogador que ganhou
                                                                            nome_perdedor = lista_jogo[0]   #para que possamos pegar o valor do jogador que perdeu
                                                                            adicionar_pontos(lista_rj, nome_vencedor)
                                                                            adicionar_jogos(lista_rj, nome_vencedor)
                                                                            adicionar_jogos(lista_rj, nome_perdedor) 
                                                                            guardar_ficheiro_json("jogadores.json", lista_rj)
                                                                            print("Sequência conseguida. Jogo terminado.")
                                                                            lista_jogo.clear()
                                                                            lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                                            lista_pecas_especiais_j2.clear()
                                                                            lista_tabela.clear()
                                                                            break #break k
                                                                    else:
                                                                        diagonal = 0
                                                                        break
                                                                
                                                                if diagonal == sequencia_vencedora: #break j
                                                                    break

                                                        if diagonal == sequencia_vencedora: #breaj i
                                                            break

                                                    if horizontal != sequencia_vencedora and vertical != sequencia_vencedora and diagonal != sequencia_vencedora:
                                                        for i in range(len(lista_tabela)-1, -1, -1):
                                                            for j in range(len(lista_tabela[i])-1, -1, -1):
                                                                if lista_tabela[i][j] == "| O |":
                                                                    diagonal_invertida = 0
                                                                    for k in range(1, sequencia_vencedora):
                                                                        if i-k >= 0 and j+k < len(lista_tabela[i]) and lista_tabela[i-k][j+k] == "| O |":
                                                                            diagonal_invertida += 1
                                                                            if diagonal_invertida == sequencia_vencedora-1:
                                                                                nome_perdedor = lista_jogo[0]
                                                                                nome_vencedor = nome    #o nome vencedor ganha o valor do ultimo a jogar
                                                                                lista_jogo.remove(nome_vencedor)    #remove o jogador que ganhou
                                                                                nome_perdedor = lista_jogo[0]   #para que possamos pegar o valor do jogador que perdeu
                                                                                adicionar_pontos(lista_rj, nome_vencedor)
                                                                                adicionar_jogos(lista_rj, nome_vencedor)
                                                                                adicionar_jogos(lista_rj, nome_perdedor) 
                                                                                guardar_ficheiro_json("jogadores.json", lista_rj)
                                                                                print("Sequência conseguida. Jogo terminado.")
                                                                                lista_jogo.clear()
                                                                                lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                                                lista_pecas_especiais_j2.clear()
                                                                                lista_tabela.clear()
                                                                                break #break k
                                                                        else:
                                                                            diagonal_invertida = 0
                                                                            break

                                                                    if diagonal_invertida == sequencia_vencedora: #break j
                                                                        break
                                                                    
                                                            if diagonal_invertida == sequencia_vencedora: #break i
                                                                break
                                             
                                
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
                                                                    nome_vencedor = nome    #o nome vencedor ganha o valor do ultimo a jogar
                                                                    lista_jogo.remove(nome_vencedor)    #remove o jogador que ganhou
                                                                    nome_perdedor = lista_jogo[0]   #para que possamos pegar o valor do jogador que perdeu
                                                                    adicionar_pontos(lista_rj, nome_vencedor)
                                                                    adicionar_jogos(lista_rj, nome_vencedor)
                                                                    adicionar_jogos(lista_rj, nome_perdedor) 
                                                                    guardar_ficheiro_json("jogadores.json", lista_rj)
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
                                                
                                                if horizontal != sequencia_vencedora:
                                                    for j in range(len(lista_tabela[0])):   #itera todos os valores da lista em base das colunas
                                                        for i in range(len(lista_tabela)):
                                                            if vertical != sequencia_vencedora:     #verifica se o variavel é igual a sequencia vencedora
                                                                if lista_tabela[i][j] == "| O |":
                                                                    vertical += 1 
                                                                    if vertical == sequencia_vencedora:     #segunda verificação
                                                                        nome_vencedor = nome    #o nome vencedor ganha o valor do ultimo a jogar
                                                                        lista_jogo.remove(nome_vencedor)    #remove o jogador que ganhou
                                                                        nome_perdedor = lista_jogo[0]   #para que possamos pegar o valor do jogador que perdeu
                                                                        adicionar_pontos(lista_rj, nome_vencedor)
                                                                        adicionar_jogos(lista_rj, nome_vencedor)
                                                                        adicionar_jogos(lista_rj, nome_perdedor) 
                                                                        guardar_ficheiro_json("jogadores.json", lista_rj)
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
                                                
                                                if horizontal != sequencia_vencedora and vertical != sequencia_vencedora:
                                                    for i in range(len(lista_tabela)):
                                                        for j in range(len(lista_tabela[i])):
                                                            if lista_tabela[i][j] == "| X |":
                                                                for k in range(1,sequencia_vencedora):
                                                                    if i+k < len(lista_tabela) and j+k < len(lista_tabela[i]) and lista_tabela[i+k][j+k] == "| O |":
                                                                        diagonal +=1
                                                                        if diagonal == sequencia_vencedora-1:
                                                                            nome_perdedor = lista_jogo[0] 
                                                                            nome_vencedor = nome    #o nome vencedor ganha o valor do ultimo a jogar
                                                                            lista_jogo.remove(nome_vencedor)    #remove o jogador que ganhou
                                                                            nome_perdedor = lista_jogo[0]   #para que possamos pegar o valor do jogador que perdeu
                                                                            adicionar_pontos(lista_rj, nome_vencedor)
                                                                            adicionar_jogos(lista_rj, nome_vencedor)
                                                                            adicionar_jogos(lista_rj, nome_perdedor) 
                                                                            guardar_ficheiro_json("jogadores.json", lista_rj)
                                                                            print("Sequência conseguida. Jogo terminado.")
                                                                            lista_jogo.clear()
                                                                            lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                                            lista_pecas_especiais_j2.clear()
                                                                            lista_tabela.clear()
                                                                            break #break k
                                                                    else:
                                                                        diagonal = 0
                                                                        break
                                                                
                                                                if diagonal == sequencia_vencedora: #break j
                                                                    break

                                                        if diagonal == sequencia_vencedora: #breaj i
                                                            break

                                                    if horizontal != sequencia_vencedora and vertical != sequencia_vencedora and diagonal != sequencia_vencedora:
                                                        for i in range(len(lista_tabela)-1, -1, -1):
                                                            for j in range(len(lista_tabela[i])-1, -1, -1):
                                                                if lista_tabela[i][j] == "| O |":
                                                                    diagonal_invertida = 0
                                                                    for k in range(1, sequencia_vencedora):
                                                                        if i-k >= 0 and j+k < len(lista_tabela[i]) and lista_tabela[i-k][j+k] == "| O |":
                                                                            diagonal_invertida += 1
                                                                            if diagonal_invertida == sequencia_vencedora-1:
                                                                                nome_perdedor = lista_jogo[0]
                                                                                nome_vencedor = nome    #o nome vencedor ganha o valor do ultimo a jogar
                                                                                lista_jogo.remove(nome_vencedor)    #remove o jogador que ganhou
                                                                                nome_perdedor = lista_jogo[0]   #para que possamos pegar o valor do jogador que perdeu
                                                                                adicionar_pontos(lista_rj, nome_vencedor)
                                                                                adicionar_jogos(lista_rj, nome_vencedor)
                                                                                adicionar_jogos(lista_rj, nome_perdedor) 
                                                                                guardar_ficheiro_json("jogadores.json", lista_rj)
                                                                                print("Sequência conseguida. Jogo terminado.")
                                                                                lista_jogo.clear()
                                                                                lista_pecas_especiais_j1.clear()    #Limpar o jogo em curso
                                                                                lista_pecas_especiais_j2.clear()
                                                                                lista_tabela.clear()
                                                                                break #break k
                                                                        else:
                                                                            diagonal_invertida = 0
                                                                            break

                                                                    if diagonal_invertida == sequencia_vencedora: #break j
                                                                        break
                                                                    
                                                            if diagonal_invertida == sequencia_vencedora: #break i
                                                                break
                                           
                                                   
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
            if len(lista_tabela) != 0:  #Verifica se existe um jogo em curso
                for i in range(len(lista_tabela)):      #Representação gráfica da tabela atualizada
                    for j in range(len(lista_tabela[i])):
                        print(lista_tabela[i][j],end = '')  #Print ao elemento [i][j] e dá um espaço entre eles                       
                    print()
            else:
                print("Não existe jogo em curso")




            ########### GRAVAR #############
    
        elif opcao[0] == "g":
            if opcao[1] == "jogo_guardado":                                                                                           
                jogo_atual = [lista_tabela, lista_jogo, lista_pecas_especiais_j1, lista_pecas_especiais_j2, lista_rj]   #grava o jogo
                guardar_ficheiro_json("jogo_guardado.json", jogo_atual)
                print("Jogo gravado.")
            else:
                print("Ocorreu um erro na gravação.")
        


            ########## LER #############

        elif opcao[0] == "l": 
            if opcao[1] == "jogo_guardado":                                                                                           
                ler_ficheiro_json("jogo_guardado.json")
                lista_tabela = jogo_atual[0]
                lista_jogo = jogo_atual[1]
                lista_pecas_especiais_j1 = jogo_atual[2]
                lista_pecas_especiais_j2 = jogo_atual[3]
                print("Jogo carregado.")
            else:
                print("Ocorreu um erro no carregamento.")
            
            ########### SAIR DO MENU ############
 
        elif opcao[0] == "sm":                                                                                           
            break
        
        else:
            print("Opção inválida.")