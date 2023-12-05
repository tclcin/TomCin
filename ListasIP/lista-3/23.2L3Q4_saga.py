livros_sergio = input().split(', ')
total_edicoes = int(input())
percy_sergio = []
outra_saga_sergio = []
saga_percy = ['O Ladrão de Raios', 'O Mar de Monstros', 'A Maldição do Titã', 'A Batalha do Labirinto', 'O Último Olimpiano']
livros_faltando = ['O Ladrão de Raios', 'O Mar de Monstros', 'A Maldição do Titã', 'A Batalha do Labirinto', 'O Último Olimpiano']


for livro in livros_sergio:
    if livro in saga_percy:
        percy_sergio.append(livro)
        livros_faltando.remove(livro)
    elif livro != '':
        outra_saga_sergio.append(livro)


string_livros_faltando = ''
for i in range(len(livros_faltando)):
    if i == 0:
        string_livros_faltando = livros_faltando[i]
    else:
        string_livros_faltando += ', ' + livros_faltando[i]  

string_livros_outra_saga = ''
for i in range(len(outra_saga_sergio)):
    if i == 0:
        string_livros_outra_saga = outra_saga_sergio[i]
    else:
        string_livros_outra_saga += ', ' + outra_saga_sergio[i]


if len(percy_sergio) == len(saga_percy):
    print('Sua coleção está completa! Você pode ler à vontade.')
elif len(percy_sergio) != 0:
    print(f"Infelizmente, sua coleção está incompleta. Falta(m) esse(s) livro(s): {string_livros_faltando}.")
else:
    print(f'Caramba, você não tem nenhum livro. Compre todos imediatamente.')
if len(outra_saga_sergio) != 0:
    print(f'Cuidado, Sérgio! Você está organizando seus livros de uma forma errada, o(s) livro(s): {string_livros_outra_saga}, não faz(em) parte da saga "Percy Jackson e os Olimpianos".')

