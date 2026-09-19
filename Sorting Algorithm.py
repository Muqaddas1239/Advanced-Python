# Sorting Algorithms
# Sorting means arranging data in a particular order.
# Real-world example: Arranging students according to their marks.

# Bubble Sort
# Bubble Sort compares adjacent elements and swaps them if they are in the wrong order.
# Real-world example: Arranging people from shortest to tallest.

numbers = [5, 3, 8, 4, 2]

for i in range(len(numbers)):
    for j in range(len(numbers) - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)


# Selection Sort
# Selection Sort finds the smallest element and places it at its correct position.
# Real-world example: Arranging products from cheapest to most expensive.

numbers = [5, 3, 8, 4, 2]

for i in range(len(numbers)):
    minimum = i

    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[minimum]:
            minimum = j

    numbers[i], numbers[minimum] = numbers[minimum], numbers[i]

print(numbers)


# Insertion Sort
# Insertion Sort takes one element at a time and places it in its correct position.
# Real-world example: Arranging playing cards in your hand.

numbers = [5, 3, 8, 4, 2]

for i in range(1, len(numbers)):
    current = numbers[i]
    j = i - 1

    while j >= 0 and numbers[j] > current:
        numbers[j + 1] = numbers[j]
        j -= 1

    numbers[j + 1] = current

print(numbers)


# Merge Sort
# Merge Sort divides data into smaller parts, sorts them, and then combines them.
# Real-world example: Dividing a large class into groups, sorting each group, and combining them.

def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    middle = len(numbers) // 2

    left = merge_sort(numbers[:middle])
    right = merge_sort(numbers[middle:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


numbers = [5, 3, 8, 4, 2]

print(merge_sort(numbers))


# Quick Sort
# Quick Sort chooses a pivot and divides the data into smaller and larger elements.
# Real-world example: Choosing one person as a reference and separating shorter and taller people.

def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[0]

    smaller = [x for x in numbers[1:] if x <= pivot]
    larger = [x for x in numbers[1:] if x > pivot]

    return quick_sort(smaller) + [pivot] + quick_sort(larger)


numbers = [5, 3, 8, 4, 2]

print(quick_sort(numbers))