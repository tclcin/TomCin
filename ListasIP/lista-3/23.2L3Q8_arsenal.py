arsenal = "Foice de Hades, Talismã de Ícaro, Elmo da Invisibilidade, Cinto de Hermes, Espada Anaklusmos, Escudo Aegis, Adaga Katoptris".split(', ')

unwanted_equipment_individual = 'string'
individuals_names = []
chosen_equipment_all = []
while unwanted_equipment_individual != 'Parar':
    chosen_equipment_individual = []
    unwanted_equipment_individual = input()
   
    if unwanted_equipment_individual != 'Parar':
        unwanted_equipment_individual = unwanted_equipment_individual.split(('-'))
        individuals_names.append(unwanted_equipment_individual[0])
        
        for equipment in arsenal:
            if equipment not in unwanted_equipment_individual:
                chosen_equipment_individual.append(equipment)
        chosen_equipment_all.append(chosen_equipment_individual)

for i, name in enumerate(individuals_names):
    if len(chosen_equipment_all[i]) == 0:
        print(f'{name} irá batalhar na base do murro!')  
    elif len(chosen_equipment_all[i]) == 1:
        print(f'{name} irá rumo a batalha com o equipamento: {chosen_equipment_all[i][0]}!')
    else:
        print(f'{name} irá rumo a batalha com os seguintes equipamentos:',end=' ')
        print(', '.join(chosen_equipment_all[i][:-1]),end='')
        print(f' e {chosen_equipment_all[i][-1]}!')


