numeros_validos = False


n1 = int(input())

if n1 > 0: 
   
    n2 = int(input())
     
    if n2 > 0:

        n3 = int(input())

        if n3 > 0:
            numeros_validos = True


if n1 <= 0:
    print(f"{n1} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.")

elif n2 <= 0:
    print(f"{n2} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.")

elif n3 <= 0:
    print(f"{n3} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir")



if numeros_validos:
    palavra_valida = False

    palavra = input()
    if palavra.islower():
        palavra_valida = True
    else:
        print(f"{palavra} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.")
    

n5 = 0
if numeros_validos and palavra_valida:
    n5 = int(input())
    

if n5 > 0:
    if n1 % 2 == 0:
        n1 *= 2
    else: 
        n1 *= 0.5
    
    if n2 % 2 == 0:
        n2 *= 2
    else: 
        n2 *= 0.5

    if n3 % 2 == 0:
        n3 *= 2
    else: 
        n3 *= 0.5

    numero_final = (n5 * n1 * n2 * n3)**(1/2)

    if numero_final >= 10:
        print(f"O número {numero_final:.2f} e a palavra {palavra} eram as respostas. A caixa foi aberta.")
    else:
        print(f"A combinação era muito pequena, a caixa só vai poder ser aberta daqui a {10-numero_final:.2f} anos.")



elif numeros_validos and palavra_valida:
    print(f"{n5} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.")







    
