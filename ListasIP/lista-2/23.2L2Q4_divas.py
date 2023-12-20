total_number_of_shows = int(input())
remaining_shows = total_number_of_shows
rodadas_taylor = 0
rodadas_beyonce = 0


print("Vai começar! Vamos ver quem é a verdadeira diva!")
while remaining_shows > 0 and rodadas_beyonce < 3 and rodadas_taylor < 3:
    
    current_show = total_number_of_shows - remaining_shows + 1
    
    print(f"Vai começar a {current_show}º rodada!")
    
    remaining_shows -= 1
    pontuacao_final_taylor = 0

    pontuacao_final_beyonce = 0

    nota_coreografia_taylor = int(input())
    nota_figurino_taylor = int(input())
    nota_coreografia_beyonce = int(input())
    nota_figurino_beyonce = int(input())

    pontuacao_final_taylor += nota_coreografia_taylor * 4 + nota_figurino_taylor * 3

    pontuacao_final_beyonce += nota_coreografia_beyonce * 4 + nota_figurino_beyonce * 3
 


    tay_vencedora = pontuacao_final_taylor > pontuacao_final_beyonce
    bey_vencedora = pontuacao_final_beyonce > pontuacao_final_taylor
    vencedora = "Tay"*tay_vencedora + "Bey"*bey_vencedora

    maior_score = 0
    menor_score = 0
    if tay_vencedora:
        maior_score = pontuacao_final_taylor
        menor_score = pontuacao_final_beyonce
    else:
        maior_score = pontuacao_final_beyonce
        menor_score = pontuacao_final_taylor   

    print(f"Fim da apresentação! O placar da rodada {current_show} foi {maior_score}x{menor_score} para os representantes da {vencedora}.")

    if vencedora == "Tay":
        rodadas_taylor += 1
    else:
        rodadas_beyonce += 1
    
    diferenca = abs(pontuacao_final_beyonce - pontuacao_final_taylor)
    if diferenca > 20: 
        print(f"A diferença na pontuação foi de {diferenca} pontos.")
    else:
        print(f"A diferença de pontos foi de apenas {diferenca}.")

if rodadas_beyonce > rodadas_taylor:
    print(f"Minha nossa! A equipe da Beyoncé chocou o mundo e venceu a equipe da Taylor Swift por um placar de {rodadas_beyonce} a {rodadas_taylor}. A Bey é a verdadeira rainha do pop!")

else:
    print(f"Uuuh! Por um placar de {rodadas_taylor} a {rodadas_beyonce}, a equipe da Taylor Swift venceu a competição e mostrou que ela é a verdadeira diva do pop!")

    

