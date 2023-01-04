def tem_sequencia_vencedora(tabuleiro):
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] == linha[3] or linha[1] == linha[2] == linha[3] == linha[4]
            return True
    return False