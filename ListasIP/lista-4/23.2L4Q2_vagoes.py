def organizar_malas(lista_de_pesos : list):
    pesos_inteiros = list(map(int, lista_de_pesos))
    pesos_inteiros.sort()

    i = 0 
    j = len(pesos_inteiros) - 1
    while i <= 1:
        pesos_inteiros[i], pesos_inteiros[j] = pesos_inteiros[j], pesos_inteiros[i] 
        i += 1
        j -= 1
    
    return pesos_inteiros

def parametros(carvao: int, peso: int, passageiros: int):
    velocidade = round((carvao + 200) / 2)
    carga = round((peso + 4000) / 1000)
    total_pessoas = passageiros + 40

    return [velocidade, carga, total_pessoas]

def turno(horario: str, roteiro: str, funcionarios: list):
    convocados = []
    if 7 <= int(horario[0:2]) < 21:
        if roteiro == "Roteiro 1":
            convocados = [funcionarios[0], funcionarios[1]]
        else:
            convocados = [funcionarios[0], funcionarios[-1]]
    else:
        if roteiro == "Roteiro 1":
            convocados = [funcionarios[2]]
        else:
            convocados = []
    
    return[convocados]


lista_pesos_malas = input().split(', ')

carvao_peso_passageiros = input().split(', ')
qtd_carvao = carvao_peso_passageiros[0]
peso = carvao_peso_passageiros[1]
num_passageiros = carvao_peso_passageiros[2]

lista_funcionarios = input().split(', ')
horario = input()
roteiro = input()
