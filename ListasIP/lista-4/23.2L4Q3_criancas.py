    def soma_codigo(ascii_string : str) -> int:
        split_ascii_string = ascii_string.split(' ')
        while '' in split_ascii_string:
            split_ascii_string.remove('')
        ascii_code_list:list = list(map(int, split_ascii_string))
        
        somatorio_dos_codigos:int = 0
        for code in ascii_code_list:
            somatorio_dos_codigos += code

        return somatorio_dos_codigos

    def decodificador_ascii(ascii_string : str) -> str:
        split_ascii_string = ascii_string.split(' ')
        while '' in split_ascii_string:
            split_ascii_string.remove('')
        ascii_code_list:list = list(map(int, split_ascii_string))

        presente_decodificado:str = ''
        for code in ascii_code_list:
            presente_decodificado += chr(code)

        return presente_decodificado

    def presente_invalido(decodificado:str, lista_codificados:list, lista_decodificados:list) -> bool:
        invalido:bool = False
        endereco_presente:int = lista_decodificados.index(decodificado)

        soma_codigo_presente:int = soma_codigo(lista_codificados[endereco_presente])

        if soma_codigo_presente % 2 != 0:
            invalido = True
        
        return invalido
        

    def main():
        n_presentes_possiveis = int(input())

        presentes_codificados:list = []
        presentes_decodificados:list = []

        for i in range(n_presentes_possiveis):
            presentes_codificados.append(input())


        for presente in presentes_codificados:
            presente_decodificado = decodificador_ascii(presente)
            print(f"{presente_decodificado} foi adicionado a lista ultrassecreta de presentes da Anya!!")
            if presente_decodificado in presentes_decodificados:
                print(f"{presente_decodificado} já está na lista de presentes da Anya!!")
            presentes_decodificados.append(presente_decodificado)

        presentes_invalidos = []
        presentes_validos = []
        for presente in presentes_decodificados:
            if (presente_invalido(presente, presentes_codificados, presentes_decodificados)):
                presentes_invalidos.append(presente)
            else:
                presentes_validos.append(presente)
            
        if len(presentes_invalidos) != 0:
            print(f'Infelizmente o Twilight é mão de vaca e os seguintes itens precisaram ser excluídos da lista de presentes ultrassecretos da Anya: {", ".join(presentes_invalidos)}.')
        elif n_presentes_possiveis != 0:
            print("Parece que o Dia das Crianças desse ano será especial!!!! Anya ganhará todos os presentes planejados, mesmo que ela não seja tão exemplar como deveria…")

        if len(presentes_validos) != 0:
            print(f'Lista final dos melhores presentes da Anya: {", ".join(presentes_validos)}.')
        else:
            print("O quê? Nenhum presente? Isso é um absurdo! Vamos corrigir essa injustiça e garantir que Anya tenha um Dia das Crianças inesquecível!")

    main()