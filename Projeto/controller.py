import json

def escrever_ficheiro_json(nome_ficheiro, d):
  json_string = json.dumps(d)
  json_file = open(nome_ficheiro, "w")
  json_file.write(json_string)
  json_file.close()

def ler_ficheiro_json(nome_ficheiro):
  with open(nome_ficheiro) as f:
    data = json.load(f)
    return data

def registar_jogador(nome_registar, lista_rj):                                       #função de adicionar jogadores dento da lista de jogadores
  nome_registar = {"Nome": nome_registar, "Pontos": 0, "Jogos": 0}
  lista_rj.append(nome_registar)
  return lista_rj

def verificar_nomes(lista_rj, nome):
  contagem = 0
  for valor in lista_rj:
    if valor["Nome"] == nome:
      contagem += 1
      if contagem ==
    else:
      return False
   

def remover_jogador(nome_remover, lista_jogadores):                                         #função de remover jogadores da lista de jogadores
  lista_jogadores.remove(nome_remover)
  return lista_jogadores

def listar_jogadores(lista_jogadores, lista_partidas, lista_vitorias, lista_lj):            #função que faz a iteração de cada uma das três listas, passando em cada posição igual entre ambas as listas,
  for i in range(len(lista_jogadores)):                                                     #depois o valor de i de ambas as listas na posição n (primeiro loop n=0, loops seguintes n+1) são armazenadas em  
    jogadores = lista_jogadores[i]                                                          #uma lista, e essa lista é armazenada em outra lista teno uma lista base para outras listas.
    partidas = lista_partidas[i]                                                            #este processo repete-se ate a ultima posição de cada lista, atençao qeu cada lista tem que apresentar o mesmo numero de indices
    vitorias = lista_vitorias[i]
    lista_lj.append([jogadores, partidas, vitorias])
  return lista_lj

def nome_jogadores_ij (jogador_1, jogador_2, lista_jogo):                               #funcao que adiciona os nomes dos 2 jogadores dentro de uma lista e ordena os mesmos alfabeticamente
  lista_jogo.append(jogador_1)
  lista_jogo.append(jogador_2)
  lista_jogo.sort()
  return lista_jogo

def pecas_especiais(peca, lista_pecas_especiais_j1, lista_pecas_especiais_j2):
  lista_pecas_especiais_j1.append(peca)
  lista_pecas_especiais_j2.append(peca)
  return lista_pecas_especiais_j1, lista_pecas_especiais_j2   

def colocar_peca_j1(colunas, lista_tabela):
  ultimo_elemento_vazio = 1
  for i in range(len(lista_tabela)):
    if lista_tabela[i][colunas] == "|___|":
        ultimo_elemento_vazio = i
    else:
        break
  lista_tabela[ultimo_elemento_vazio][colunas] = "| X |"

def colocar_peca_j2(colunas, lista_tabela):
  ultimo_elemento_vazio = 1
  for i in range(len(lista_tabela)):
      if lista_tabela[i][colunas] == "|___|":
          ultimo_elemento_vazio = i
      else:
          break
  lista_tabela[ultimo_elemento_vazio][colunas] = "| O |"     
                                 
