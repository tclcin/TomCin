numero_definidor = int(input())

string_1 = input()
string_2 = input()
string_3 = input()

num_letras_string_1 = len(string_1)
num_letras_string_2 = len(string_2)
num_letras_string_3 = len(string_3)


maior_string = ''
menor_string = ''


meia_string = ''

# Definindo a maior string
if num_letras_string_2 <= num_letras_string_1 >= num_letras_string_3:
    maior_string = string_1

elif num_letras_string_1 <= num_letras_string_2 >= num_letras_string_3:
    maior_string = string_2

else:
    maior_string = string_3

# Definindo a menor string
if num_letras_string_2 >= num_letras_string_1 <= num_letras_string_3:
    menor_string = string_1

elif num_letras_string_1 >= num_letras_string_2 <= num_letras_string_3:
    menor_string = string_2
else:
    menor_string = string_3

# Definindo a string intermediária
if (num_letras_string_2 >= num_letras_string_1 >= num_letras_string_3) or (num_letras_string_3 >= num_letras_string_1 >= num_letras_string_3):
    meia_string = string_1

elif (num_letras_string_1 >= num_letras_string_2 >= num_letras_string_2) or (num_letras_string_3 >= num_letras_string_2 >= num_letras_string_1):
    meia_string = string_2

else:
    meia_string = string_3

# Caso limite 
if num_letras_string_1 == num_letras_string_2 == num_letras_string_3:
    maior_string = string_1
    menor_string = string_2
    meia_string = string_3


if numero_definidor == 1:
    if len(maior_string) == len(meia_string) or len(maior_string) == len(menor_string):
        print("(Droga! Ainda não consegui descobrir o local que possui mais sinais desconhecidos! Vou ter que ficar mais um tempo nessa Mansão Mal-Assombrada...)")
        print("AAAAAA! Um fantasma me assustou!")
        print('''(Uma mensagem apareceu no monitor que você estava usando. "Agente, um erro inesperado aconteceu. A EPF contactará você novamente quando tudo estiver funcionando da forma correta. Nosso sistema foi invadido por alguém que se identifica como Hubert P.Enguin")''')

        if (maior_string * (menor_string < maior_string > meia_string)) + (meia_string * (menor_string < meia_string > maior_string)) + (menor_string * (meia_string < menor_string > maior_string)) != "":
            print(f"{maior_string * (menor_string < maior_string > meia_string) + (meia_string * (menor_string < meia_string > maior_string)) + (menor_string * (meia_string < menor_string > maior_string))}")
            print('''(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")''')
    
    else:
        print(maior_string)
        print('''(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")''')

else:
    if len(menor_string) == len(meia_string) or len(menor_string) == len(maior_string):
        print("(Droga! Ainda não consegui descobrir o local que possui mais sinais desconhecidos! Vou ter que ficar mais um tempo nessa Mansão Mal-Assombrada...)")
        print("AAAAAA! Um fantasma me assustou!")
        print('''(Uma mensagem apareceu no monitor que você estava usando. "Agente, um erro inesperado aconteceu. A EPF contactará você novamente quando tudo estiver funcionando da forma correta. Nosso sistema foi invadido por alguém que se identifica como Hubert P.Enguin")''')
        if (maior_string * (menor_string < maior_string > meia_string)) + (meia_string * (menor_string < meia_string > maior_string)) + (menor_string * (meia_string < menor_string > maior_string)) != '':
            print(f"{(maior_string * (menor_string < maior_string > meia_string)) + (meia_string * (menor_string < meia_string > maior_string)) + (menor_string * (meia_string < menor_string > maior_string))}")
            print('''(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")''')
    
    else:
        print(menor_string)
        print('''(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")''')


print("(Depois de ler a mensagem, você dormiu. Ao acordar, você não estava mais no CIn de outubro de 2012, mas no CIn de 2023, sem acreditar na situação que vivenciou)")