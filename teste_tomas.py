import os



# def criacao_tabela (linhas, colunas):




os.system("cls")

linhas = int(input('linhas-'))
colunas = int(input("colunas-"))
valor_lateral = 1
tabela = []

########## TABELA VAZIA #################

for i in range (linhas):
    tabela.append(["|___|"] * colunas)

for i in range(colunas):
    print(f"    {i+1}", end="")
print()  
   
for i in range(len(tabela)):
    print(valor_lateral,end = ' ')
    valor_lateral += 1
    for j in range(len(tabela[i + 1])): 
        print(tabela[i][j],end = '')                        #mexe em cada linha e cada coluna em separado
    print()                                                 #adicionar um espaço em branco e a garantir que damos espaços
print(tabela)

############# PRIMEIRA JOGADA ##############
while True:
    valor_lateral = 0
    print("""Jogada jogador 1: """)
    linha = int(input("Entre com a linha: "))
    coluna = int(input("Entre com a coluna: "))


    for i in range(colunas):
        print(f"   {i} ", end="")
    print()   
    
    tabela[linha][coluna] = '| X |'
    for i in range(len(tabela)):
        print(valor_lateral,end = '')
        valor_lateral += 1
        for j in range(len(tabela[i])):
            print(tabela[i][j],end = '')
        print()   
    
    valor_lateral = 0
    print("Jogada jogador 2: ")
    linha = int(input("Entre com a linha: "))
    coluna = int(input("Entre com a coluna: "))

    for i in range(colunas):
        print(f"   {i} ", end="")
    print()  
        
    tabela[linha][coluna] = '| O |'
    for i in range(len(tabela)):
        print(valor_lateral,end = '')
        valor_lateral += 1
        for j in range(len(tabela[i])):
            print(tabela[i][j],end = '')
        print()
    
    if linha == 99:
        break