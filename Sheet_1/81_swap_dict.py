d = {'a': 1, 'b': 2, 'c': 3}

max_key = max(d, key=d.get)
min_key = min(d, key=d.get)

d[max_key], d[min_key] = d[min_key], d[max_key]

print(d)