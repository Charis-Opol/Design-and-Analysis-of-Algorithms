def mergesort(array):
    if len(array) <= 1:
        return array
    mid = len (array)//2
    left = mergesort(array[:mid])
    right = mergesort(array[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

array1 = [38, 27, 43, 3, 9, 82, 10]
sorted_array = mergesort(array1)
print(sorted_array)