message_ascii = input()
message_translation = '' 

can_translate = True
for char in message_ascii:
    char_translation_sum = ord(char) + len(message_ascii)   
    char_translation = 'char'

    if char == ' ':
        char_translation = ' '
    elif (48 <= char_translation_sum <= 57) or (char_translation_sum >= 256):
        can_translate = False
    else:
        char_translation = chr(char_translation_sum)

    message_translation += char_translation

if message_translation == ' ':
    print("Ué não tem nada para me decifrar aqui")
elif can_translate:
    print(f"Descobri o que a mensagem significa: {message_translation}")
else:
    print("Algo de errado não está certo. Será que estou ficando doido?")