computadores_disponiveis = int(input())
dinheiro_disponivel = int(input())
tempo_limite = int(input())

computadores_ocupados = 0

nome_amigo = 'string'
while (nome_amigo != 'end' and computadores_ocupados < computadores_disponiveis):
    nome_amigo = input()

    if not ((nome_amigo == 'end') or (nome_amigo == 'laura') or (nome_amigo == 'carlos') or (nome_amigo == 'roberto')):
        computadores_ocupados += 1
    
if computadores_ocupados == 0:
    print("Ah não! João não conseguiu nenhum amigo que o ajudasse. Agora ele vai ter que contar com a sorte para pegar um bom lugar na fila, usando apenas seu computador.")

else:
    print(f"Bom começo! Consegui {computadores_ocupados} amigos que podem me ajudar a comprar o ingresso")


    posicao_mais_avancada = float('inf')
    computador_escolhido = -1
    opcoes = 0

    for i in range(computadores_ocupados):
        local_do_show = 'string'
        conseguiu_local = False
        while (local_do_show != 'end') and (not conseguiu_local):
            valor_do_ingresso = int(input()) 
            local_do_show = input() 
            
            
            conseguiu_local = False
            if (local_do_show == "rio de janeiro" or local_do_show == "são paulo" or local_do_show == "buenos aires"):
                conseguiu_local = True
                print("Consegui um ingresso em um local que João possa ir! Agora temos que ver o preço")
            
            conseguiu_preco = False
            if conseguiu_local:
                if (valor_do_ingresso < dinheiro_disponivel):
                    conseguiu_preco = True
                    print("Consegui o dinheiro! Agora só falta ver a minha colocação na fila dos ingressos...")
                else:
                    print("Caramba! Só tinha ingresso para a pista vip, que está bem acima do meu orçamento.")
                    
            if (conseguiu_preco and conseguiu_local):
                posicao_fila = int(input())
                if (10/16)*posicao_fila < tempo_limite * 60:
                    print("ISSOOO, conseguimos um ingresso!!!")
                    opcoes += 1
                    
                    if posicao_fila < posicao_mais_avancada:
                        posicao_mais_avancada = posicao_fila
                        computador_escolhido = i 
                        
                    
                else:
                    print(f"Caramba, essa foi quase! Mas infelizmente não consegui um bom lugar na fila dos ingressos no computador de número {i + 1}")

    
    if computador_escolhido == -1:
        if (computadores_ocupados/computadores_disponiveis) > 0.5:
            print("Não acredito que tive amigos para ocuparem mais da metade dos computadores, e ainda assim não consegui um ingresso...")
        else:
            print("Poxa, não acredito que não consegui o ingresso, acho que eu devia ter chamado mais amigos para ajudar.")
    
    else:
        print(f"Consegui o ingresso! Com {int((opcoes/computadores_ocupados)*100)}% de aproveitamento da ajuda dos meus amigos. E a fila escolhida para comprar o ingresso foi do computador número {computador_escolhido + 1}. Rumo ao show da Taylor!!!")


