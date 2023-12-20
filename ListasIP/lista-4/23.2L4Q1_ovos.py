horoscopos = [
    "Os astros estão radiantes hoje! Eles farão o possível para abençoar a todos com boa sorte.", # melhor previsão 
    "Os astros estão de bom humor hoje. Acho que você terá um pouco de sorte extra.", # ótima previsão 
    "As estrelas estão neutras hoje. O dia está em suas mãos.", # boa previsão 
    "Isso é raro. As estrelas estão absolutamente neutras hoje.", # previsão neutra
    "Hoje, Kiq não pôde consultar as estrelas. Sem a orientação astrológica, a busca por ovos fica à mercê do destino." # pior previsão 
]

frases_finais = [
    "Incrível! Seu signo está em alta. Você encontrou todos os ovos!",
    "Ótimo trabalho! Os astros estão ao seu lado. Você encontrou a maioria dos ovos!",
    "Bom esforço! Os astros sorriem para você. Muitos ovos foram encontrados.", 
    "Continue procurando! Seu horóscopo sugere que há mais ovos a serem encontrados.",
    "Ainda não encontrou nenhum ovo. O horóscopo aconselha persistência. Continue tentando!"
]

def max(value_1, value_2):
    if value_1 > value_2:
        return value_1
    else:
        return value_2

def itens_encontrados(numero_dia, itens_escondidos, previsão):
    itens_encontrados = 0
    if previsão == horoscopos[0]:
        itens_encontrados = itens_escondidos
    elif previsão == horoscopos[1]:
        itens_encontrados = itens_escondidos * 0.7
    elif previsão == horoscopos[2]:
        itens_encontrados = max(itens_escondidos * 0.7, itens_escondidos/((itens_escondidos % numero_dia) + 1))
    elif previsão == horoscopos[3]:
        itens_encontrados = (itens_escondidos % numero_dia) + 1
    elif previsão == horoscopos[4]:
        itens_encontrados = 0
    
    itens_encontrados = int(itens_encontrados)
    return itens_encontrados

def aproveitamento(taxa_de_sucesso):
    aproveitamento = 'string'

    if taxa_de_sucesso == 1:
        aproveitamento = frases_finais[0]
    elif 0.66 < taxa_de_sucesso < 1:
        aproveitamento = frases_finais[1]
    elif 0.33 < taxa_de_sucesso <= 0.66:
        aproveitamento = frases_finais[2]
    elif 0 < taxa_de_sucesso <= 0.33:
        aproveitamento = frases_finais[3]
    else:
        aproveitamento = frases_finais[4]
    
    return aproveitamento



qtd_dias = int(input())
ovos_encontrados_cada_dia = [] # lista do numero de ovos encontrados a cada dia 
total_ovos_encontados = 0
total_ovos_escondidos = 0

for i in range(qtd_dias):
    ovos_escondidos_dia = int(input())
    total_ovos_escondidos += ovos_escondidos_dia
    horoscopo_dia = input()
    dia = i + 1
    ovos_encontrados_dia = itens_encontrados(dia, ovos_escondidos_dia, horoscopo_dia)
    total_ovos_encontados += ovos_encontrados_dia
   
    ovos_encontrados_cada_dia.append(ovos_encontrados_dia)

for j in range(len(ovos_encontrados_cada_dia)):
    dia =  j + 1
    ovos_encontrados = ovos_encontrados_cada_dia[j]

    print(f"Dia {dia}")
    print(f"Hoje Carlos encontrou {ovos_encontrados} ovos!!")

print(f"Kiq encontrou {total_ovos_encontados} de um total de {total_ovos_escondidos}")

taxa_de_encontro = total_ovos_encontados / total_ovos_escondidos
print(aproveitamento(taxa_de_encontro))