computadores_disponiveis = int(input())
dinheiro_disponivel = int(input())
tempo_limite = int(input())

computadores_ocupados = 0

nome = 'string'
while nome != 'end' and computadores_ocupados < computadores_disponiveis:
    nome = input()

    if not (nome == 'end' or nome == 'laura' or nome == 'carlos' or nome == 'roberto'):
        computadores_ocupados += 1
    
if computadores_ocupados == 0:
    print("Ah não! João não conseguiu nenhum amigo que o ajudasse. Agora ele vai ter que contar com a sorte para pegar um bom lugar na fila, usando apenas seu computador.")

else:
    print(f"Bom começo! Consegui {computadores_ocupados} amigos que podem me ajudar a comprar o ingresso")


    posicao_mais_avancada = 7*10**9
    computador_escolhido = -1
    opcoes = 0
    for i in range(computadores_ocupados):
        valor_do_ingresso = 'string'
        local_do_show = 'string'
        tentando = False
        
        valor_do_ingresso = input()
        if valor_do_ingresso != 'end':
            valor_do_ingresso = int(valor_do_ingresso)
            local_do_show = input()
            tentando = True
        
        consegiu_local = False
        if tentando and (local_do_show == "rio de janeiro" or local_do_show == "são paulo" or local_do_show == "buenos aires"):
            consegiu_local = True
            print("Consegui um ingresso em um local que João possa ir! Agora temos que ver o preço")
        
        consegiu_preco = False
        if consegiu_local:
            if valor_do_ingresso < dinheiro_disponivel:
                consegiu_preco = True
                print("Consegui o dinheiro! Agora só falta ver a minha colocação na fila dos ingressos...")
            else:
                print("Caramba! Só tinha ingresso para a pista vip, que está bem acima do meu orçamento.")
                
        if tentando and consegiu_preco and consegiu_local:
            posicao_fila = int(input())
            if (10/16)*posicao_fila < tempo_limite * 60:
                print("ISSOOO, conseguimos um ingresso!!!")
                opcoes += 1
                if posicao_fila < posicao_mais_avancada:
                    computador_escolhido = i 
                
            else:
                print(f"Caramba, essa foi quase! Mas infelizmente não consegui um bom lugar na fila dos ingressos no computador de número {i}")

    
    if computador_escolhido == -1:
        if computadores_ocupados/computadores_disponiveis > 0.5:
            print("Não acredito que tive amigos para ocuparem mais da metade dos computadores, e ainda assim não consegui um ingresso...")
        else:
            print("Poxa, não acredito que não consegui o ingresso, acho que eu devia ter chamado mais amigos para ajudar.")
    
    else:
        print(f"Consegui o ingresso! Com {int((opcoes/computadores_ocupados)*100)}% de aproveitamento da ajuda dos meus amigos. E a fila escolhida para comprar o ingresso foi do computador número {computador_escolhido}. Rumo ao show da Taylor!!!")


