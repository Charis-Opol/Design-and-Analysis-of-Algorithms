list = [2, 4, 3, 1, 5]

inversion_count = 0
for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if list[i] > list[j]:
            inversion_count += 1

print("Number of inversion counts: ", inversion_count)


