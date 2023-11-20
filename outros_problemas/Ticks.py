dias_real_life_jogados = int(input())
numero_de_casas = int(input())

dias_virtuais_jogados = dias_real_life_jogados * 9

ticks_totais = dias_virtuais_jogados * 12000

ticks_por_casa = int(ticks_totais/numero_de_casas)

print(ticks_por_casa)