def itera_listas(lista_partidas, lista_nomes, lista_vitorias, resultado):
  for i in range(len(lista_partidas)):
    partida = lista_partidas[i]
    nome = lista_nomes[i]
    vitoria = lista_vitorias[i]
    resultado.append([partida, nome, vitoria])
  return resultado

resultado = []

lista_nomes = ['Jogador 1', 'Jogador 2', 'Jogador 3', 'Jogador 4']
lista_partidas = [1, 2, 3, 4]
lista_vitorias = [1, 2, 3, 4]

resultado = itera_listas(lista_partidas, lista_nomes, lista_vitorias, resultado)
print(resultado)
for partida, nome, vitoria in resultado:
  print(f"Partida: {partida} Nome: {nome} Vitória: {vitoria}")




    
