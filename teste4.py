


linhas = int(input('linhas-'))
colunas = int(input("colunas- "))
tabela = linhas * colunas
a = []
for i in range (linhas):
    a.append(["|__|"])

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end = '')
    print()

print (a)