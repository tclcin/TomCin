## Saúde jogador
vida_jogador = int(input())
vivo = True

## Informações de batalha jogadoer
poder_arma_jogador = int(input())
habilidade_luta_jogador = int(input())
poder_surpresa_jogador = int(input())

## Informações oponente 
poder_arma_mascarado = int(input())
habilidade_luta_mascarado = int(input())
poder_surpresa_mascarado = int(input())
defesa_mascarado = int(input())


# Primeira luta
if (poder_arma_jogador > poder_arma_mascarado) and (habilidade_luta_jogador > habilidade_luta_mascarado) and (poder_surpresa_jogador > poder_surpresa_mascarado):
    
    print("Ainda bem que deu tudo certo, está quase em casa")
    pass

elif (vida_jogador - defesa_mascarado > 0):
    
    print("Rápido, corra antes que ele vá atrás de você!")
    
    poder_arma_jogador *= 0.95
    habilidade_luta_jogador *= 0.95
    poder_surpresa_jogador *= 1.05

else: 
    
    print("Oh, no! Acabou pra mim")
    
    vivo = False


# Segunda Luta
if vivo:
    poder_arma_novo_mascarado = int(input())
    habilidade_luta_novo_mascarado = int(input())
    poder_surpresa_novo_mascarado = int(input())

    if (poder_arma_jogador >= poder_arma_novo_mascarado) or (habilidade_luta_jogador >= habilidade_luta_novo_mascarado) or (poder_surpresa_jogador >= poder_surpresa_novo_mascarado):
    
        print("Casa, aqui vou eu")
    
    else:
        print("Oh, no! Acabou pra mim")