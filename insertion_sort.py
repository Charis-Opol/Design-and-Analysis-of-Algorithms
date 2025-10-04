array = [38, 27, 43, 3, 9, 82, 10]

n = len(array)

for i in range(1, n):
    insert_index = i
    poped_element = array.pop(i)
    for j in range(i - 1, -1, -1):
        if poped_element < array[j]:
            insert_index = j
    array.insert(insert_index, poped_element)

print(array)