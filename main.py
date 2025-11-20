items = {
    'r': {'size': 3, 'points': 25},
    'p': {'size': 2, 'points': 15},
    'a': {'size': 2, 'points': 15},
    'm': {'size': 2, 'points': 20},
    'i': {'size': 1, 'points': 5},
    'k': {'size': 1, 'points': 15},
    'x': {'size': 3, 'points': 20},
    't': {'size': 1, 'points': 25},
    'f': {'size': 1, 'points': 15},
    'd': {'size': 1, 'points': 10},
    's': {'size': 2, 'points': 20},
    'c': {'size': 2, 'points': 20}
}

must_have = items['d']
items.pop('d')
max_size = 9 - must_have['size']
def gen_table(items, max_size = max_size):
    table = [[0 for _ in range(max_size)] for _ in range (len(items))]
    for i, item in enumerate(items.values()):
        size = item['size']
        points = item['points']

        for limit_size in range(1, max_size + 1):
            idx = limit_size - 1
            if i == 0:
                if size > limit_size:
                    table[i][idx] = 0  
                else:
                    table[i][idx] = points
            else: 
                prev_points = table[i-1][idx]
                if size > limit_size:
                    table[i][idx] = prev_points
                else:
                    if idx < size:
                        rest = 0
                    else:
                        table[i-1][idx - size]
                    result = max(rest + points, prev_points)
                    table[i][idx] = result
    for i in table: print(i)


def get_size_and_points(items):
    size = [items[item]['size'] for item in items]
    points = [items[item]['points'] for item in items]
    return size, points
size, points = get_size_and_points(items)
print(size)
print(points)

