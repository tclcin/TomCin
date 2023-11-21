num_versos = int(input())
acertos = 0

for i in range(num_versos):
    
    plateia = input()
    plateia_analise = ''
    for letter in plateia:
        plateia_analise += letter.upper() 
    
    if i == 0:
        print("Cause, baby, now we've got")
        if plateia_analise == "BAD BLOOD":
            print(plateia_analise)
            acertos += 1
            
    
    elif i == 1:
        print("You know it used to be")
        if plateia_analise == "MAD LOVE":
            print(plateia_analise)
            acertos += 1
    
    elif i == 2:
        print("So take a look what")
        if plateia_analise == "YOU'VE DONE":
            print(plateia_analise)
            acertos += 1
    
    elif i == 3:
        print("Cause, baby, now we've got")
        if plateia_analise == "BAD BLOOD, HEY":
            print(plateia_analise)
            acertos += 1

if acertos == 4:
    print("A plateia deu um show! Acertou tudo!")

elif acertos >= 2:
    print("A plateia acertou a maior parte da música")

else:
    print("Foi um dia atípico e a plateia se esqueceu de grande da música")