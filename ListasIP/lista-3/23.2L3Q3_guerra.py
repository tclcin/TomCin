itens_desejados = input().split(', ')

itens_acampamento = input().split(', ')

itens_conseguidos = []

for desejado in itens_desejados:
    conseguiu = False
    for encontrado in itens_acampamento:
        if encontrado == desejado:
            conseguiu = True
            itens_conseguidos.append(encontrado)

if len(itens_conseguidos) != 0:
    print("Estes são os itens que já tenho no Acampamento Meio-Sangue:")

for i in range(len(itens_conseguidos)):
    print(f'{i + 1}º item: {itens_conseguidos[i]}')

if len(itens_conseguidos) == 0:
    print(f"Hmm, preciso visitar um vendedor ambulante! Não encontrei nenhum dos {len(itens_desejados)} itens aqui no Acampamento Meio-Sangue.")
elif len(itens_desejados) > len(itens_conseguidos):
    print(f"Vou precisar adquirir {len(itens_desejados) - len(itens_conseguidos)} itens antes da batalha!")
else:
    print(f"Perfeito, encontrei todos os {len(itens_desejados)} itens aqui no Acampamento Meio-Sangue!")

print("Estou pronto para a batalha! Que comece a guerra contra os Titãs!")