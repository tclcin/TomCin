nomes = ['Zeus', 'Afrodite', 'Poseidon', 'Hércules', 'Aquiles', 'Orfeu']
especialidades = ['trovão', 'amor', 'oceanos', 'força', 'resistência', 'música']
naturezas = ['deus', 'deusa', 'deus', 'semideus', 'semideus', 'semideus']

quantidade_questoes = int(input())
acertos = 0


for i in range(quantidade_questoes):
    resposta_percy = input().split(', ')
    nome_resposta = 'string'
    parte_resposta = 'string' 
    natureza_resposta = 'string'
    especialidade_resposta = 'string'
    chutou = False 
    acertou = False  

    for parte in resposta_percy:
        if parte in nomes:
            nome_resposta = parte
        elif parte in especialidades:
            especialidade_resposta = parte
        elif parte in naturezas:
            natureza_resposta = parte
        else:
            chutou = True 

    if not chutou:
        deus_em_questao = nomes.index(nome_resposta)
        
        if (especialidade_resposta == especialidades[deus_em_questao]) and (natureza_resposta == naturezas[deus_em_questao]):
            acertou = True
            acertos += 1
        
    if acertou:
        print(f'A resposta da {i+1}ª questão está... CORRETA!')
    else:
        print(f'A resposta da {i + 1}ª questão está... ERRADA!')

if quantidade_questoes == 0:
    print('Infelizmente, Percy Jackson, chegou atrasado para a exame...')

else:
    taxa_de_acerto = int(acertos/quantidade_questoes*100)

    print(f'Percy Jackson, sua taxa de acerto no EDEM é de aproximadamente... {taxa_de_acerto}%') 

    if taxa_de_acerto == 100:
        print('UAU, você gabaritou! Você é praticamente um deus do Olimpo!')
    elif taxa_de_acerto >= 60:
        print('Muito bem, você quase pode começar a desfilar entre os semideuses!')
    elif 60 > taxa_de_acerto >= 20:
        print('Você pode melhorar um pouco mais!')
    else: 
        print('Bem... te vejo ano que vem')