linhas = int(input('linhas-'))
colunas = int(input("colunas-"))

tabela = []
for i in range (linhas):
    tabela.append(["|__|"] * colunas)
    
    
for i in range(len(tabela)):
    for j in range(len(tabela[i])):
        print(tabela[i][j],end = '')
    print()

print(f"{tabela}\n")
while True:
    print("""Jogada jogador 1: """)
    linha = int(input("Entre com a linha: "))
    coluna = int(input("Entre com a coluna: "))

    tabela[linha][coluna] = 'X'
    for i in range(len(tabela)):
        for j in range(len(tabela[i])):
            print(tabela[i][j],end = '')
        print()

    print("Jogada jogador 2: ")
    linha = int(input("Entre com a linha: "))
    coluna = int(input("Entre com a coluna: "))

    tabela[linha][coluna] = 'O'
    for i in range(len(tabela)):
        for j in range(len(tabela[i])):
            print(tabela[i][j],end = '')
        print()

    if linha == 99:
        break