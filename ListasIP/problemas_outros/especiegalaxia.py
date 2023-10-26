nome_especie = input()
num_bebes_especie = 0

while True:
    especie_1 = input()
    if especie_1 == "fim":
        break
    especie_2 = input()
    caracteristica_1 = input()
    caracteristica_2 = input()
    probababilidade1 = int(input())
    probabilidade_2 = int(input())
    potencial_1 = int(input())
    potencial_2 = int(input())

    squared_difference_1 = (probababilidade1 - potencial_1) ** 2
    squared_difference_2 = (probabilidade_2 - potencial_2) ** 2

    if squared_difference_1 > squared_difference_2:
        especie_bebe = especie_1
        caracteristica_bebe = caracteristica_1
    else:
        especie_bebe = especie_2
        caracteristica_bebe = caracteristica_2

    if especie_bebe == nome_especie:
        num_bebes_especie += 1

    print("O bebê ET gerado é da espécie " + especie_bebe + " e tem como característica " + caracteristica_bebe)


print("nasceram " + str(num_bebes_especie) + " bebês ETs da espécie " + nome_especie)


