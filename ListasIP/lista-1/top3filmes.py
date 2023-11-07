nome_filme_1 = input()
pontuacao_global_filme_1 = int(input())
critica_filme_1 = input()

nome_filme_2 = input()
pontuacao_global_filme_2 = int(input())
critica_filme_2 = input()

nome_filme_3 = input()
pontuacao_global_filme_3 = int(input())
critica_filme_3 = input()



if critica_filme_1 == "boa":
    pontuacao_global_filme_1 *= 1.25
elif critica_filme_1 == "media":
    pontuacao_global_filme_1 *= 1

elif critica_filme_1 == "ruim":
    pontuacao_global_filme_1 *= 0.75

elif critica_filme_1 == "pessima":
    pontuacao_global_filme_1 *= 0



if critica_filme_2 == "boa":
    pontuacao_global_filme_2 *= 1.25
elif critica_filme_2 == "media":
    pontuacao_global_filme_2 *= 1

elif critica_filme_2 == "ruim":
    pontuacao_global_filme_2 *= 0.75

elif critica_filme_2 == "pessima":
    pontuacao_global_filme_2 *= 0



if critica_filme_3 == "boa":
    pontuacao_global_filme_3 *= 1.25
elif critica_filme_3 == "media":
    pontuacao_global_filme_3 *= 1

elif critica_filme_3 == "ruim":
    pontuacao_global_filme_3 *= 0.75

elif critica_filme_3 == "pessima":
    pontuacao_global_filme_3 *= 0



filme_1 = ''
filme_2 = ''
filme_3 = ''
zerado = False


    
if pontuacao_global_filme_1 == max(pontuacao_global_filme_1, pontuacao_global_filme_2, pontuacao_global_filme_3):
    filme_1 = nome_filme_1
    
elif pontuacao_global_filme_1 == min(pontuacao_global_filme_1, pontuacao_global_filme_2, pontuacao_global_filme_3):
    filme_3 = nome_filme_1
        
else: 
    filme_2 = nome_filme_1



if pontuacao_global_filme_2 == max(pontuacao_global_filme_1, pontuacao_global_filme_2, pontuacao_global_filme_3):
    filme_1 = nome_filme_2
    
elif pontuacao_global_filme_2 == min(pontuacao_global_filme_1, pontuacao_global_filme_2, pontuacao_global_filme_3):
    filme_3 = nome_filme_2
        
else: 
    filme_2 = nome_filme_2



if pontuacao_global_filme_3 == max(pontuacao_global_filme_1, pontuacao_global_filme_2, pontuacao_global_filme_3):
    filme_1 = nome_filme_3
    
elif pontuacao_global_filme_3 == min(pontuacao_global_filme_1, pontuacao_global_filme_2, pontuacao_global_filme_3):
    filme_3 = nome_filme_3
        
else: 
    filme_2 = nome_filme_3





print("**** TOP 3 FILMES ****")

print(f"{filme_1} está em 1° lugar")
print(f"{filme_2} está em 2° lugar")
print(f"{filme_3} está em 3° lugar")

if pontuacao_global_filme_1 == 0 or pontuacao_global_filme_2 == 0 or pontuacao_global_filme_3 == 0:
    print(f"{filme_3} teve uma crítica péssima")