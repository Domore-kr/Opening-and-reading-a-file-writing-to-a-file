def cook_book(rec):
    cook_book = {}
    with open(rec) as cook:
        for i in cook:
            cook_book[i.strip()] = []
            for a in range(int(cook.readline())):
                b = cook.readline().strip()
                cook_book[i.strip()].append(
                    {'ingredient_name': b[0:b.find('|')], 'quantity': int(b[b.find('|') + 2: b.rfind('|') - 1]),
                     'measure': b[b.rfind('|') + 2:]})
            cook.readline()
        return cook_book


def get_shop_list_by_dishes(dishes, person_count, rec):
    ingridients = {}
    cook = cook_book(rec)
    for i in dishes:
        for a in cook[i]:
            if ingridients.get(a['ingredient_name']) is None:
                ingridients[a['ingredient_name']] = {'measure': a['measure'],
                                                     'quantity': int(a['quantity'] * person_count)}
            else:
                double_ingridient = int(ingridients[a['ingredient_name']]['quantity'])
                ingridients[a['ingredient_name']] = {'measure': a['measure'],
                                                     'quantity': (
                                                             double_ingridient + int(a['quantity']) * person_count)}
    return print(ingridients)


get_shop_list_by_dishes(['Омлет', 'Фахитос', 'Омлет'], 2, 'recipes.txt')
