minutos = 0
parou = False
music_count = 0
opiniao = ''

while not parou and music_count < 21:

    opiniao = input()

    if opiniao == "amei":
        minutos += 4
    
    elif opiniao == "não parei de ouvir":
        minutos -= 4
        comentario = ''
        while comentario != "pulei":
            minutos += 4
            comentario = input()
    
    elif opiniao == "escutei só metade":
        minutos += 2
        
    
    elif opiniao == "parei":
        parou = True
    
    music_count += 1


print(f"Você ouviu {minutos} minutos hoje!!!")
