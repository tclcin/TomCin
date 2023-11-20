number_of_shows = int(input())

rodadas_taylor = 0
rodadas_beyonce = 0



for i in range(number_of_shows):

    pontuacao_final_taylor = 0

    pontuacao_final_beyonce = 0

    nota_coreografia_taylor = int(input())
    nota_figurino_taylor = int(input())
    nota_coreografia_beyonce = int(input())
    nota_figurino_beyonce = int(input())

    pontuacao_final_taylor += nota_coreografia_taylor * 4 + nota_figurino_taylor * 3

    pontuacao_final_beyonce += nota_coreografia_beyonce * 4 + nota_figurino_beyonce * 3

    if pontuacao_final_beyonce > pontuacao_final_taylor:
        rodadas_beyonce += 1
    else:
        rodadas_taylor += 1


    

