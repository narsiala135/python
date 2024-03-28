def remove_duplicates(array):
    if not array:
        return []

    unique_array = [array[0]]

    for num in array[1:]:
        if num != unique_array[-1]:
            unique_array.append(num)

    return unique_array

array = [15, 14, 25, 14, 32, 14, 31]

array.sort()

sorted_array = remove_duplicates(array)

print("Sorted Array =", sorted_array)
