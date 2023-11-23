nome_pretendente = 'string'
palavra_pretendente = 'string'
palavra_taylor = 'string'

while nome_pretendente != 'vou dormir':
    nome_pretendente = input()
    if nome_pretendente != 'vou dormir':   
        
        palavra_pretendente = input()
        palavra_taylor = input()
        
 
        letras_iguais = ''
        
        for letra in palavra_taylor:

            if letra in palavra_pretendente:
                letras_iguais += letra
                palavra_pretendente = palavra_pretendente.replace(letra, '1', 1)

        
        
        if len(letras_iguais) >= len(palavra_taylor):
             print(f'você acertou, estreou na lista! {nome_pretendente}')
    
        else:
            print(f'perdeu, covarde!')


