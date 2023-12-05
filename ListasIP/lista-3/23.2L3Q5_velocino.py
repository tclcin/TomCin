informacoes_deuses = [
    ['Zeus', 'Poseidon', 'Atenas', 'Ares', 'Afrodite'],
    [100, 90, 80, 70, 60],
    ['Raio', 'Tridente', 'Égide', 'Lança', 'Cinto Mágico']
]

sequencia = input()
tamanho_sequencia = len(sequencia)
numero_do_digito_atual = 0
for digito in sequencia:
    numero_do_digito_atual += 1 
    query = int(digito)
    
    if (informacoes_deuses[0][query] == 'Atenas') or (informacoes_deuses[0][query] == 'Afrodite'): 
        print(f"Deusa:{informacoes_deuses[0][query]}")
    else:
        print(f'Deus:{informacoes_deuses[0][query]}') 
        
    print(f"Poder:{informacoes_deuses[1][query]}")
    print(f"Artefato:{informacoes_deuses[2][query]}")
    
    if numero_do_digito_atual != tamanho_sequencia:
        print('')