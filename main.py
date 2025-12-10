import random

items_dict = {
    'r': {'slots': 3, 'points': 25},
    'p': {'slots': 2, 'points': 15},
    'a': {'slots': 2, 'points': 15},
    'm': {'slots': 2, 'points': 20},
    'i': {'slots': 1, 'points': 5},
    'k': {'slots': 1, 'points': 15},
    'x': {'slots': 3, 'points': 20},
    't': {'slots': 1, 'points': 25},
    'f': {'slots': 1, 'points': 15},
    'd': {'slots': 1, 'points': 10},
    's': {'slots': 2, 'points': 20},
    'c': {'slots': 2, 'points': 20}
}

inv_slots_x = 3
inv_slots_y = 3
inv_slots = inv_slots_x * inv_slots_y
# заражение - антидот обязателен
# убираем антидот из списка чтобы не положить в рюкзак дубликат
must_have = items_dict.pop('d')
max_slots = inv_slots - must_have['slots']
start_points = 15
chr_points = start_points # + must_have['points']


def get_slots_and_points(items_dict):
    '''
    Создаём списки значений площади и ценности
    '''
    slots = [items_dict[item]['slots'] for item in items_dict]
    points = [items_dict[item]['points'] for item in items_dict]
    return slots, points


def get_table(items_dict, max_slots):
    n = len(items_dict) 
    slots, points = get_slots_and_points(items_dict)

    # zeroes table max slots + 1 colums and items_dict count rows rows
    table = [[0 for _ in range(max_slots+1)] for _ in range(n+1)]

    
    for row in range(n+1):
        for col in range (max_slots+1):
            prev_points = table[row-1][col]
            # can just remove this zeroes colums and row? seems to just add confusion with indexes
            if row == 0 or col==0:
                table[row][col] = 0
            # если площадь предмета меньше площади столбца, 
            # максимизируем значение суммарной ценности
            elif slots[row-1] <= col: # -1 row is item. - 1 cause 1 row i zeroes
                current_points = points[row-1] + table[row-1][col-slots[row-1]]
                table[row][col] = max(current_points, prev_points)
            # если площадь предмета больше площади столбца,
            # забираем значение ячейки из предыдущей строки
            else: # оазмео больше макс размера            
                table[row][col] = prev_points
    return table, slots, points


def get_selected_items(items_dict, max_slots):
    table, slots, points = get_table(items_dict, max_slots)
    n = len(items_dict)
    res = table[n][max_slots] # last element [8][11]
    print(res)
    a = max_slots
    items_list = []

    for i in range(n, 0, -1):
        if res <= 0: 
            break
        if res == table[i-1][a]:
            continue
        else:
            items_list.append({'slots': slots[i-1], 'points':points[i-1]})
            res -= points[i-1]
            a -= slots[i-1]
    # print(items_list)

    selected_items = []
    for search in items_list:
        selected_item = []
        for key, value in items_dict.items():
            if value == search:
                selected_item.append(key)
        selected_items.append(selected_item)

    #[['k', 'f'], ['t'], ['k', 'f'], ['m', 's', 'c'], ['r']]
    items_variant = []
    for item in selected_items:
        if len(item) > 1:
            n = 0
            while n == 0:
                random_item = random.choice(item)
                if random_item not in items_variant:
                    items_variant.append(random_item)
                    n += 1
        else:
            items_variant.append(item[0])
    return items_variant

    # inv_inventory_variants = []
    # inv_inv = [] 
    # for variant in selected_items:  
    #     inv_slot = '' 
    #     #for j in range(len(i)):
    #         #if j not in inv_inv:
    #             #inv_inv += i[j]
    #     inv_inv += inv_slot]
    # print(inv_inv)


items_variant = get_selected_items(items_dict, max_slots)
print(items_variant)

inv_variant = ['d','k', 't', 'f', 'm', 'r']

def calc_chr_points(items_dict, chr_points):
    for item in items_dict:
        if item in inv_variant:
            chr_points += items_dict[item]['points']
        else:
            chr_points -= items_dict[item]['points']
    return chr_points

'''
print(calc_chr_points(items_dict, chr_points))
# 'k': {'slots': 1, 'points': 15}
# 't': {'slots': 1, 'points': 25}
# 'f': {'slots': 1, 'points': 15}
# 'm': {'slots': 2, 'points': 20}
# 'r': {'slots': 3, 'points': 25}
# 'd': {'slots': 1, 'points': 10}

slots = []
items_dict.update({'d': must_have})
print(items_dict)
for i in inv_variant:
    slots += i * items_dict[i]['slots']
print(slots)

rows = [slots[i:i + inv_slots_x] for i in range(0, len(slots), inv_slots_x)]
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# n = 3  
# res = [] 
# for i in range(0, len(a), n):  # Slice list in steps of n
#     res.append(a[i:i + n])
for r in rows: print(' '.join(f'[{x}]' for x in r))


'''