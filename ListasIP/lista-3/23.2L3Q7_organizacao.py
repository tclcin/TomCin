number_of_dorms = int(input())
number_of_floors = int(input())

campers_in_dorms = []



for i in range(number_of_dorms):
    campers_in_floors = []
    for j in range(number_of_floors):
        number_of_campers = int(input())
        campers_in_floors.append(number_of_campers)
    campers_in_dorms.append(campers_in_floors)

most_campers_sum = -1
most_campers_dorm = -1
for i in range(len(campers_in_dorms)):
    if sum(campers_in_dorms[i]) > most_campers_sum:
        most_campers_dorm = i
        most_campers_sum = sum(campers_in_dorms[i]) 

for dorm in campers_in_dorms:
    for i in range(len(dorm)):
        if i < (len(dorm)) - 1:
            print(dorm[i],end=' ')
        else:
            print(dorm[i],end='')
    print('')

print('')    
print(f"O chalé {most_campers_dorm + 1} foi o que mais recebeu semi-deuses, tendo um acréscimo de {most_campers_sum} novos campistas!")