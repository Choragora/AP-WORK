tabela = [1, 2, None, 4, '']
elementos_vazios = [i for i, x in enumerate(tabela) if x == '']

print("Elementos Vazios : ", elementos_vazios)

for i in range(len(tabela)):
    if i == elementos_vazios[0]:
        tabela[i] = 'x'
        break

print("tabela : ", tabela)