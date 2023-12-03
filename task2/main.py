def get_shop_list_by_dishes(dishes, person_count):
    ingridient_dict = {}
    for dish in dishes:
        for i in range(len(cook_book[dish])):
            temporary_dict = {}
            if cook_book[dish][i]['ingredient_name'] in ingridient_dict:
                temporary_dict['quantity'] = ingridient_dict[cook_book[dish][i]['ingredient_name']]['quantity'] + int(cook_book[dish][i]['quantity']) * person_count
            else:
                temporary_dict['quantity'] = int(cook_book[dish][i]['quantity']) * person_count
            temporary_dict['measure'] = cook_book[dish][i]['measure']
            ingridient_dict[cook_book[dish][i]['ingredient_name']] = temporary_dict
    print(f'\nСписок ингридиентов:\n{ingridient_dict}')


cook_book = {}
dish_dict = {}

with open('recipes.txt', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if idx == 0:
            cook_book[line.strip()] = []
            current_dish_key = line.strip()
            current_dish_idx = idx

        elif idx == current_dish_idx + 1:
            counter = int(line.strip())
            dish_pos = idx

        elif idx - dish_pos <= counter:
            ingridient = line.split("|")
            dish_dict['ingredient_name'] = ingridient[0].strip()
            dish_dict['quantity'] = ingridient[1].strip()
            dish_dict['measure'] = ingridient[2].strip()
            cook_book[current_dish_key].append(dish_dict)
            dish_dict = {}

        elif idx == dish_pos + counter + 2:
            cook_book[line.strip()] = []
            current_dish_key = line.strip()
            current_dish_idx = idx


print(f'Кулинарная книга:\n{cook_book}')

get_shop_list_by_dishes(['Фахитос', 'Омлет', 'Помидоры с сыром'], 2)

