x_jogador = int(input())
z_jogador = int(input())

x_hogsmead = 34
z_hogsmead = 220

x_kakariko = 0 
z_kakariko = 0

x_solitude = 140 
z_solitude = 456

distancia_hogsmead = ((x_hogsmead - x_jogador)**2 + (z_hogsmead - z_jogador)**2)**(1/2)
distancia_kakariko = ((x_kakariko - x_jogador)**2+(z_kakariko - z_jogador)**2)**(1/2)
distancia_solitude = ((x_solitude - x_jogador)**2 + (z_solitude - z_jogador)**2)**(1/2)

print(f"Distancia para Hogsmeade:{distancia_hogsmead: .2f}")
print(f"Distancia para Kakariko: {distancia_kakariko: .2f}")
print(f"Distancia para Solitude: {distancia_solitude: .2f}")
