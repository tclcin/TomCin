total_celebridades = int(input())
kanye = False 
gerard = False 
Chris = False 

for i in range(total_celebridades):
    nome_celeb = input()
 
    if nome_celeb == "Kanye West": 
        kanye = True 
    elif nome_celeb == "Gerard Piqué":
        gerard = True 
    elif nome_celeb == "Chris Martin":
        chris = True

    print(f"Apresentador: Contamos com a ilustre presença de {nome_celeb}, uma salva de palmas!")

candidato = "string"
taylor = False
katy = False
ariana = False 
beyonce = False 
shakira = False 
while candidato != "Início da Premiação":
    candidato = input()
    if candidato == "Taylor Swift":
        taylor = True 
    elif candidato == "Katy Perry":
        katy = True
    elif candidato == "Ariana Grande":
        ariana = True
    elif candidato == "Beyoncé":
        beyonce = True 
    elif candidato == "Shakira":
        shakira = True

vencedor = 'string'

if taylor:
    vencedor = "TAYLOR SWIFT"

elif katy:
    vencedor = "KATY PERRY"

elif ariana:
    vencdor = "ARIANA GRANDE"

elif beyonce:
    vencedor = "BEYONCÉ"

else:
    vencedor = "SHAKIRA"


print("Apresentador: E a artista do ano do MTV Video Music Awards 2023 é...")
print(vencedor)

if vencedor == "TAYLOR SWIFT" and kanye: 
    print("Kanye West: Eu vou te deixar terminar. Estou feliz por você, mas Beyoncé fez um dos melhores vídeos de todos os tempos.")

elif vencedor == "SHAKIRA" and gerard:
    print("Gerard Piqué: Meu amor me perdoa, volta pra mim...")

elif vencedor == "BEYONCE" and chris:
    print("Chris Martin: Minha heroína, minha irmã, meu tudo. Você merece!")
