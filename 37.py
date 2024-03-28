
def find_nth_largest(lst, n):
    sorted_list = sorted(lst, reverse=True)
    return sorted_list[n - 1]
lst = []
n = int(input("Enter the number of elements in the list: "))
print("Enter the elements of the list:")
for i in range(n):
    element = int(input())
    lst.append(element)
N = int(input("Enter the value of N: "))
result = find_nth_largest(lst, N)
print(f"{N}th Largest number:", result)
