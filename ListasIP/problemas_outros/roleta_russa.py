import random
import os



while True:
    guess = random.randint(0, 6)

    user = int(input("Escolha um número de 1 a 6"))

    if user != guess:
        print("parabéns, você sobreviveu!!!!")
    else:
        if os.name == 'posix':
            os.system('sudo shutdown now')

