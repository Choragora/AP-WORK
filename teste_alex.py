linhas = int(input('linhas-'))
colunas = int(input("colunas-"))
valor_lateral = 0
tabela = []

########## TABELA VAZIA #################

for i in range (linhas):
    tabela.append(["|___|"] * colunas)

for i in range(colunas):
    print(f"    {i}", end="")
print()  
   
for i in range(len(tabela)):
    print(valor_lateral,end = ' ')
    valor_lateral += 1
    for j in range(len(tabela[i])):
        print(tabela[i][j],end = '')                        
    print()                                                 #adicionar um espaço em branco e a garantir que damos espaçosz

while True:
    valor_lateral = 0
    print("Jogada jogador 1: ")
    colunas = int(input("Em que coluna deseja jogar? "))

    last_empty_column = 1

    for i in range(len(tabela)):
        if tabela[i][colunas] == "|___|":
            last_empty_column = i
        else:
            break
    tabela[last_empty_column][colunas] = "1"
    
    for i in range(colunas):
        print(f"    {i}", end="")
    print()

    for i in range(len(tabela)):
        print(valor_lateral,end = ' ')
        valor_lateral += 1
        for j in range(len(tabela[i])):
            print(tabela[i][j],end = '')                        
        print()  
