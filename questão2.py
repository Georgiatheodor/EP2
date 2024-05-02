def posicao_suporta (mapa, blocos, linha,coluna, orientação):
    if orientação=='v':
        if linha+blocos > len(mapa):
            return False
        
        for i in range(blocos):
            if mapa[linha+i][coluna]!= ' ':
                return False
        
    
    else:
        if coluna + blocos > (len(mapa[linha])):
            return False
        
        for i in range(blocos):
            if mapa[linha][coluna+i]!=' ':
                return False
    return True
