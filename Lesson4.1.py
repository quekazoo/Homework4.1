lst = [0, 1, 7, 2, 4, 8]
if len(lst) == 0:
    result = 0
else:
    pair_index = 0
    for i in range(0, len(lst), 2):
        pair_index += lst[i]
    result = pair_index * lst[-1]
print(result)