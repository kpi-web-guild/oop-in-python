from classes import *
from main import *

def sort_by_weight(some_list):
	return some_list.weight

# Метод для создания списка юнитов
def create_units(type_units, count_units, weight_one_unit = 0):
	units_list = []
	if(weight_one_unit != 0):
		for unit in range(count_units):
			unit = type_units(weight_one_unit)
			units_list.append(unit)
		return units_list
	else:
		for unit in range(count_units):
			unit = type_units()
			units_list.append(unit)
		return units_list

# Метод для вывода результата, и отладки. 
def out_put(predator_list, sneils_list):
	print("-----FISH_PREDATORS-----")
	predator_list.sort(key = sort_by_weight)
	predator_list.reverse()
	for pred in range(len(predator_list)):
		print("Weight:", predator_list[pred].weight, "Count:", predator_list[pred].count_unit_eaten)
	
	print("-----Sneils-----")
	sneils_list.sort(key = sort_by_weight)
	sneils_list.reverse()
	for sneil in range(len(sneils_list)):
		print("Weight:", sneils_list[sneil].weight, "Count:", sneils_list[sneil].count_unit_eaten)
	
	print()
	print("*******Who`s stay?*******")
	print("Count sneils:", len(sneils_list))

# Один метод запускает все жизненные процессы существ в аквариуме
# Остаются в живых только охотники и улитки, поэтому передаём их количество
# подозреваю что можно проверить наличие объектов определенного класса в списке, но 
# условие (Fish in aquarium or Seaweed in aquarium) in while loop не даёт true
def start_fauna(aquarium, immortal_units):
	while len(aquarium) > immortal_units:				
		i = random.randint(0, len(aquarium)-1)
		some_unit = aquarium[i]
		if type(some_unit) == Seaweed:
			continue
		else:
			some_unit.hunt(aquarium)
