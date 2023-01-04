def registar_jogador(nome_registar, lista_jogadores): # função de adicionar jogadores dento da lista de jogadores
  lista_jogadores.append(nome_registar)
  return lista_jogadores


def remover_jogador(nome_remover, lista_jogadores): # função de remover jogadores da lista de jogadores
  lista_jogadores.remove(nome_remover)
  return lista_jogadores


def listar_jogadores(lista_jogadores, lista_partidas, lista_vitorias, lista_lj): # função que faz a iteração de cada uma das três listas, passando em cada posição igual entre ambas as listas,
  for i in range(len(lista_jogadores)):                                          # depois o valor de i de ambas as listas na posição n (primeiro loop n=0, loops seguintes n+1) são armazenadas em  
    jogadores = lista_jogadores[i]                                               # uma lista, e essa lista é armazenada em outra lista teno uma lista base para outras listas.
    partidas = lista_partidas[i]                                                 # este processo repete-se ate a ultima posição de cada lista, atençao qeu cada lista tem que apresentar o mesmo numero de indices
    vitorias = lista_vitorias[i]
    lista_lj.append([jogadores, partidas, vitorias])
  return lista_lj


def nome_jogadores_ij (jogador_1, jogador_2, jogadores_jogo):
  jogadores_jogo.append(jogador_1)
  jogadores_jogo.append(jogador_2)
  jogadores_jogo.sort()
  return jogadores_jogo