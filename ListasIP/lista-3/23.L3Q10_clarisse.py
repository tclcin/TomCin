arsenal = input().split(' - ')

objetos_analisados = int(input())
objetos_escolhidos = []

objeto_mostrado = int(len(arsenal)/2)


for i in range(objetos_analisados):
    rotacao = input()
    quantidade_rotacao = int(rotacao[:-1])
    sentido_rotacao = rotacao[-1:]

    if sentido_rotacao == '>':
        objeto_mostrado = (objeto_mostrado + quantidade_rotacao) % len(arsenal)
    else:
        objeto_mostrado = (objeto_mostrado - quantidade_rotacao) % len(arsenal)
    
    escolha = input()
    if escolha == 'Adicionar':
        if  arsenal[objeto_mostrado] in objetos_escolhidos:
            print(f"{arsenal[objeto_mostrado]} já está na mochila. Não seja gananciosa, ou acabará como Midas!")
        else:
            print(f"{arsenal[objeto_mostrado]} adicionado a mochila")    
            objetos_escolhidos.append(arsenal[objeto_mostrado])
    else:
        print(f"{arsenal[objeto_mostrado]} não vai ser tão útil assim!")
        
if objetos_escolhidos != []:
    print(f'Com {", ".join(objetos_escolhidos)}, seremos imbatíveis na caça à bandeira!')
        

   
    


