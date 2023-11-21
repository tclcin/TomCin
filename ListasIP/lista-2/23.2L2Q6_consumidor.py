num_total_compradores = int(input())
num_cambistas = 0

for i in range(num_total_compradores):
    strikes = 0

    nome_dado = input()
    cpf_dado = input()
    nome_real = input()
    cpf_real = input()

    num_ingr = int(input())
    preco_total = float(input())
    cdg_compra = input()

    if nome_dado != nome_real:
        strikes += 1

    if cpf_dado != cpf_real:
        strikes += 1
    
    if num_ingr > 12:
        strikes += 1
    
    if preco_total > 1500:
        strikes += 1

    digitos_impares = 0
    for digito in cdg_compra:
        if int(digito) % 2 != 0:
            digitos_impares += 1
    if digitos_impares > 7:
        strikes += 1

    if strikes >= 3:
        num_cambistas += 1

    
print(f"Total de compradores analisados: {num_total_compradores}")
print(f"Total de suspeitas de cambistas: {num_cambistas}")
