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

# убираем антидот из списка чтобы не положить в рюкзак дубликат
must_have_key = 'd'
must_have = items_dict.pop(must_have_key)

inv_slots_x = 3
inv_slots_y = 3
inv_slots = inv_slots_x * inv_slots_y
max_slots = inv_slots - must_have['slots']

start_points = 15
chr_points = start_points + must_have['points']


def get_table(items_dict, max_slots):
    n = len(items_dict) 
    slots = [items_dict[item]['slots'] for item in items_dict]
    points = [items_dict[item]['points'] for item in items_dict]
    table = [[0 for _ in range(max_slots+1)] for _ in range(n+1)]
    
    for row in range(n+1):
        for col in range (max_slots+1):
            prev_points = table[row-1][col]
            if row == 0 or col==0:
                table[row][col] = 0
            # если площадь предмета меньше площади столбца, 
            # максимизируем значение суммарной ценности
            elif slots[row-1] <= col: #-1 cause 1 row is zeroes
                current_points = points[row-1] + table[row-1][col-slots[row-1]]
                table[row][col] = max(current_points, prev_points)
            # если площадь предмета больше площади столбца,
            # забираем значение ячейки из предыдущей строки
            else:         
                table[row][col] = prev_points
    return table, slots, points


def get_selected_items(items_dict, max_slots):
    table, slots, points = get_table(items_dict, max_slots)
    n = len(items_dict)
    res = table[n][max_slots]
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
    
    # find keys, some items have same points and value:
    # [['k', 'f'], ['t'], ['k', 'f'], ['m', 's', 'c'], ['r']]
    selected_items = []
    for search in items_list:
        selected_item = []
        for key, value in items_dict.items():
            if value == search:
                selected_item.append(key)
        selected_items.append(selected_item)
   
    # return a random fitting inventory variant 
    inventory = []
    for item in selected_items:
        # exclude already selected items to not add duplicates
        r = random.choice([i for i in item if i not in inventory])
        inventory.append(r)
    return inventory


def calc_chr_points(items_dict, chr_points, inventory):
    for item in items_dict:
        points = items_dict[item]['points']
        if item in inventory:
            chr_points += points
        else:
            chr_points -= points
    return chr_points


if __name__ == '__main__':
    inventory = get_selected_items(items_dict, max_slots)
    chr_points = calc_chr_points(items_dict, chr_points, inventory)
    
    slots = []
    slots += must_have_key * must_have['slots']
    
    for i in inventory:
        slots += i * items_dict[i]['slots']
    rows = [slots[i:i + inv_slots_x] for i in range(0, len(slots), inv_slots_x)] 

    for r in rows: print(' '.join(f'[{k}]' for k in r))
    print('Total survival points: ', chr_points)

