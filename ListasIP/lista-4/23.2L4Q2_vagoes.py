def organizar_malas(lista_de_pesos : list):
    pesos_inteiros = list(map(int, lista_de_pesos))
    pesos_inteiros.sort()

    i = 0 
    j = len(pesos_inteiros) - 1
    while i <= 1:
        pesos_inteiros[i], pesos_inteiros[j] = pesos_inteiros[j], pesos_inteiros[i] 
        i += 1
        j -= 1
    
    pesos_str = list(map(str, pesos_inteiros))

    malas_organizadas = ', '.join(pesos_str)
    return malas_organizadas

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
    
    lista_convocados = ", ".join(convocados)
    return lista_convocados

def protocolo_de_inicio(pesos_malas: list, qtd_carvao: int, peso: int, num_passageiros: int, lista_funcionarios: list, horario: str, roteiro: str):
    print(f"A nova organização das malas é a seguinte: {organizar_malas(lista_de_pesos=pesos_malas)}")
    
    velocidade_carga_totalpessoas = parametros(carvao=qtd_carvao, peso=peso, passageiros=num_passageiros)
    velocidade = velocidade_carga_totalpessoas[0]
    carga = velocidade_carga_totalpessoas[1]
    total_pessoas = velocidade_carga_totalpessoas[2]
    print(f"A velocidade que o trem partirá é de: {velocidade}Km/H")
    print(f"A carga do Trem em Toneladas é: {carga} Ton.")
    print(f"A quantidade de passageiros é de {total_pessoas}")

    funcionarios_convocados = turno(horario=horario, roteiro=roteiro, funcionarios=lista_funcionarios)
    if funcionarios_convocados != '':
        print(f"Os funcionários convocados são: {funcionarios_convocados}")
    else:
        print("Os funcionários convocados são: Nenhum! O turno da Madrugada vai ser tranquilo para todos")



lista_pesos_malas = input().split(', ')

carvao_peso_passageiros = input().split(', ')
qtd_carvao = int(carvao_peso_passageiros[0])
peso = int(carvao_peso_passageiros[1])
num_passageiros = int(carvao_peso_passageiros[2])

lista_funcionarios = input().split(', ')
horario = input()
roteiro = input()

protocolo_de_inicio(lista_pesos_malas, qtd_carvao, peso, num_passageiros, lista_funcionarios, horario, roteiro)