import json

def guardar_ficheiro_json(nome_ficheiro, d): #Guarda o ficheiro 
  json_string = json.dumps(d)
  json_file = open(nome_ficheiro, "w")
  json_file.write(json_string)
  json_file.close()

def ler_ficheiro_json(nome_ficheiro): #Lê o ficheiro
  with open(nome_ficheiro) as f:
    data = json.load(f)
    return data

def verificar_nomes(lista_rj, nome): #Verifica se os nomes estão presente na lista 
  nomes_rj = [valor['Nome'] for valor in lista_rj]
  if nome not in nomes_rj:
    return True
  else:
    return False
  
def bubble_sort(lista_rj): #Ordena por ordem alfabética os nomes da lista
  for i in range(len(lista_rj)):
    for j in range(0, len(lista_rj)-i-1):
      if lista_rj[j]["Nome"] > lista_rj[j+1]["Nome"]:
        temp = lista_rj[j+1]
        lista_rj[j+1] = lista_rj[j]
        lista_rj[j] = temp

def adicionar_pontos(lista_rj, nome): #Ao jogador vencedor adiciona 1 ponto correpondente à vitória
  for valor in lista_rj:
    if valor["Nome"] == nome:
        valor['Pontos'] += 1

def adicionar_jogos(lista_rj, nome): #Após um jogo jogado, as jogadores presentes irá ser adiciona 1 jogo
  for valor in lista_rj:
    if valor["Nome"] == nome:
        valor['Jogos'] += 1

def registar_jogador(nome_registar, lista_rj):  #Adiciona os jogadores à lista de jogadores
  nome_registar = {"Nome": nome_registar, "Pontos": 0, "Jogos": 0}
  lista_rj.append(nome_registar)
  return lista_rj

def remover_jogador(nome_remover, lista_rj):  #Remove os jogadores da lista de jogadores
  pontos = 0
  jogos = 0
  for valor in lista_rj:
    if valor["Nome"] == nome_remover:
      pontos = valor['Pontos']
      jogos = valor['Jogos']
  nome_remover = {"Nome": nome_remover, "Pontos": pontos, "Jogos": jogos}
  lista_rj.remove(nome_remover)
  return lista_rj

def listar_jogadores(lista_jogadores, lista_partidas, lista_vitorias, lista_lj):  #Dicionário com o nome de cada jogador, pontos e jogos do mesmo            
  for i in range(len(lista_jogadores)):                                                     
    jogadores = lista_jogadores[i]                                                          
    partidas = lista_partidas[i]                                                            
    vitorias = lista_vitorias[i]
    lista_lj.append([jogadores, partidas, vitorias])
  return lista_lj

def nome_jogadores_ij (jogador_1, jogador_2, lista_jogo): #Adiciona e ordena os jogadores pretendidos à lista de jogadores
  lista_jogo.append(jogador_1)
  lista_jogo.append(jogador_2)
  lista_jogo.sort()
  return lista_jogo

def pecas_especiais(peca, lista_pecas_especiais_j1, lista_pecas_especiais_j2):  #Adiciona as peças especiais à lista de peças especiais
  lista_pecas_especiais_j1.append(peca)
  lista_pecas_especiais_j2.append(peca)
  return lista_pecas_especiais_j1, lista_pecas_especiais_j2

   
                                 
