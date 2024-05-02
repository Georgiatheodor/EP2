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

import random
def aloca_navios(mapa,lista):
    for bloco in lista:
        erro = False

        while not erro:
            linha = random.randint(0, len(mapa)-1)
            coluna = random.randint(0,len(mapa)-1)
            orientacao = random.choice(['h', 'v'])
            funcao = posicao_suporta(mapa, bloco, linha, coluna, orientacao)

            if funcao:
                if orientacao == 'v':
                    for i in range(bloco):
                        mapa[linha+i][coluna] = 'N'
                    erro = True
                else:
                    for a in range(bloco): 
                        mapa[linha][coluna + a] = 'N'
                    erro = True
    return mapa