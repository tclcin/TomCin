parte_do_labirinto = 'string'

labirinto = []

while parte_do_labirinto != 'Fim do labirinto':
    parte_do_labirinto = input()
    if parte_do_labirinto != 'Fim do labirinto': 
        labirinto.append(parte_do_labirinto.replace(' ', ''))

coordenadas_reliquias = []
for linha in range(len(labirinto)):
    if '1' in labirinto[linha]:
        for coluna in range(len(labirinto[linha])):
            if labirinto[linha][coluna] == '1':
                coordenadas_reliquias.append([linha,coluna])

if coordenadas_reliquias != []:
    print('Relíquias encontradas nos seguintes locais:')
    for linha_coluna in coordenadas_reliquias:
        print(f'linha: {linha_coluna[0]}, coluna: {linha_coluna[1]}')
else:
    print('Nenhuma relíquia encontrada no labirinto.')