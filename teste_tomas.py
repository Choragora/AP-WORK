def criar_tabela(comprimento, altura, tabela):
  for i in range (altura):
    tabela.append(["|___|"] * comprimento)

def desenhar_tabela(altura, tabela, valor_lateral):
  for i in range(altura):
      print(f"    {i}", end="")
  print()  
    
  for i in range(len(tabela)):
      print(valor_lateral,end = ' ')
      valor_lateral += 1
      for j in range(len(tabela[i])):
          print(tabela[i][j],end = '')                        
      print()                                            

comprimento = 5
altura = 7
tabela = []
valor_lateral = 0
criar_tabela(comprimento, altura, tabela)
print(tabela)

desenhar_tabela(altura, tabela, valor_lateral)

