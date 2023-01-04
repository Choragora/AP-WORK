linhas = int(input('linhas-'))
colunas = int(input("colunas-"))
valor_lateral = 1
tabela = [[]]


for i in range (linhas):
    tabela.append(["|___|"] * colunas)


for i in range(colunas):
    if i < 10:
        print(f"     {i+1}", end="")
    else:
        print(f"    {i+1}", end="")
print()  
    
for i in range(len(tabela)):
    print(valor_lateral,end = ' ')
    valor_lateral += 1
    for j in range(len(tabela[i])): 
        print(tabela[i][j],end = '')                        #mexe em cada linha e cada coluna em separado
    print()                                                 #adicionar um espaço em branco e a garantir que damos espaços
print(tabela)
