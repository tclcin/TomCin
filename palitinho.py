import itertools
solved_states = []
state_tree = {}
to_solve_states = [[1,1,1,1]]


while len(to_solve_states) != 0:
	iteration(to_solve_states[0])

    
def iteration(game_state):
	# ler um estado da stack
    
    # gerar filhos
    
    # adicionar filhos que não estão em to_solve em to_solve
    # remover game_state do to_solve
    
    # state_tree[game_state] = filhos
    # adicionar filhos ao state_tree para tree[game_state]
  	
	# adicionar game_state ao solved_states
    
    
    
    
    
    
    
def child_generator(game_state):
	children = []
  	if (game_state[0] + gamestate[1] % 2 == 0) and game_state[0] != game_state[1]:
		avg = (game_state[0] + game_state[1])/2
        child = [i for i in game_state]
		child[0], child[1] = avg, avg
        child = invert_sort(child)
        children.append(child)
   	for i in range(2):
      	for j in range(2, 4):
          	child = [n for n in game_state]
            child = soma(i, j, child)
            if child not in children:
                child = invert_sort(child)
                children.append(child)
    return children


                    
def soma([i, j, game_state]):
    game_state[i] = (game_state[j] + game_state[i])
    if game_state[i] >= 5:
    	game_state[i] = 0
    return game_state


def invert_sort(game_state):
  	pair1 = [game_state[0], game_state[1]]
    pair2 = [game_state[2], game_state[3]]
    sort(pair1)
    sort(pair2)
  	inverted = [pair2[0], pair2[1], pair1[0], pair2[1]]

