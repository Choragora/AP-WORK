lista_rj = [{'Nome': 'tomas', 'Pontos': 0, 'Jogos': 0}, {'Nome': 'tomas', 'Pontos': 0, 'Jogos': 0}]

for valor in lista_rj:
    contagem = lista_rj.count(valor["Nome"])
    if contagem == 0:
      print("nao existem")
      print(contagem)
      print(valor["Nome"])
    else:
      print(contagem)
      print(valor["Nome"])