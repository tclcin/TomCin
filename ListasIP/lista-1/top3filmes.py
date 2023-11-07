nome_filme_1 = input()
pontuacao_global_filme_1 = int(input())
critica_filme_1 = input()

nome_filme_2 = input()
pontuacao_global_filme_2 = int(input())
critica_filme_2 = input()

nome_filme_3 = input()
pontuacao_global_filme_3 = int(input())
critica_filme_3 = input()


if pontuacao_filme 

filme_1 = ''
filme_2 = ''
filme_3 = ''
zerado = False

for (nome_filme, pontuacao_filme) in zip((nome_filme_1, nome_filme_2, nome_filme_3), (pontuacao_global_filme_1, pontuacao_global_filme_2, pontuacao_global_filme_3)):
    
    if pontuacao_filme == max(pontuacao_global_filme_1, pontuacao_global_filme_2, pontuacao_global_filme_3):
        filme_1 = nome_filme
    
    elif pontuacao_filme == min(pontuacao_global_filme_1, pontuacao_global_filme_2, pontuacao_global_filme_3):
        filme_3 = nome_filme
        
        if pontuacao_filme == 0:
            zerado = True
    
    else:
        filme_2 = nome_filme




print("**** TOP 3 FILMES ****")

print(f"{filme_1} está em 1° lugar")
print(f"{filme_2} está em 2° lugar")
print(f"{filme_3} está em 3° lugar")

if zerado:
    print(f"{filme_3} teve uma crítica péssima")