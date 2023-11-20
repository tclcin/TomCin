qtd_songs = int(input())
total_score = 1

for i in range(qtd_songs):
    song = input().lower()
    
    song_score = 0
    for letter in song:
        
        if letter in ["a", "e", "i", "o", "u"]:
            song_score += 1
        
        else:
            song_score += 2
    
    total_score *= song_score

print(f"Parabéns por adquirir o ingresso! Seu assento é o {total_score}, estamos ansiosos para vê-lo, vai ser incrível!")