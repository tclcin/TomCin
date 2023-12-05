nome_missao = input()
grupo = []
nome_membro = 'string'

while nome_membro != 'Grupo formado':
    nome_membro = input()
    if nome_membro != 'Grupo formado':
        grupo.append(nome_membro)

print(f'O grupo formado por {len(grupo)} heróis para a missão {nome_missao} foi:')

for membro in grupo:
    print('- ' + membro)
