points = 0
song_count = 0
finished_fine = False
# possíveis eventos

event = '' 



while points >= 0:

    event = input()

    ciranda = (event == "os fãs estão formando uma ciranda") 
    flashes = (event == "os fãs estão ligando os flashes e atrapalhando a visão") 
    dancando = (event == "os fãs estão dançando na frente da tela") 
    gritando = (event == "os fãs estão gritando o nome da Taylor e atrapalhando a música") 
    cantando = (event == "os fãs estão cantando as músicas em coro") 
    casamento = (event == "houve um pedido de casamento na sessão")

    musica = (not ciranda and not flashes and not dancando and not gritando and not cantando and not casamento)
    
    negative_points = (-3 * ciranda) + (-2 * flashes) + (-2 * dancando) + (-2 * gritando)
    positive_points = (2 * cantando) + (2 * casamento) + (1 * musica)

    points += negative_points + positive_points

    if musica:
        song_count += 1
        if event == "long live":
            finished_fine = True
            break

if finished_fine:
    print(f"A Taylor conseguiu concluir o show sem muitas interrupções e cantou {song_count} músicas.")
else:
    print(f"A Taylor só conseguiu cantar {song_count} músicas e a sessão foi interrompida.")

