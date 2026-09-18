# 1. Binary Search
# Binary Search is a searching algorithm used to find an element in a sorted list.
# It checks the middle element and eliminates half of the search area in each step.

numbers = [10, 20, 30, 40, 50, 60, 70]
target = 50

left = 0
right = len(numbers) - 1

while left <= right:
    mid = (left + right) // 2

    if numbers[mid] == target:
        print("Element found at index:", mid)
        break

    elif target > numbers[mid]:
        left = mid + 1

    else:
        right = mid - 1

# 2. Iterative Binary Search
# Iterative Binary Search uses a loop to repeatedly divide the search area into half.

def binary_search(numbers, target):

    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid

        elif target > numbers[mid]:
            left = mid + 1

        else:
            right = mid - 1

    return -1

numbers = [10, 20, 30, 40, 50]
print("Index:", binary_search(numbers, 40))

# 3. Recursive Binary Search
# Recursive Binary Search uses a function that calls itself
# with a smaller search area.

def recursive_binary_search(numbers, target, left, right):

    if left > right:
        return -1

    mid = (left + right) // 2

    if numbers[mid] == target:
        return mid

    elif target > numbers[mid]:
        return recursive_binary_search(
            numbers, target, mid + 1, right
        )

    else:
        return recursive_binary_search(
            numbers, target, left, mid - 1
        )

numbers = [10, 20, 30, 40, 50]

result = recursive_binary_search(
    numbers, 40, 0, len(numbers) - 1
)

print("Index:", result)

# 4. First Occurrence
# First Occurrence finds the first position of a target when duplicate values exist.

def first_occurrence(numbers, target):

    left = 0
    right = len(numbers) - 1
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            answer = mid
            right = mid - 1

        elif target > numbers[mid]:
            left = mid + 1

        else:
            right = mid - 1

    return answer

numbers = [10, 20, 20, 20, 30]

print("First occurrence:", first_occurrence(numbers, 20))

# 5. Last Occurrence
# Last Occurrence finds the last position of a target when duplicate values exist.

def last_occurrence(numbers, target):

    left = 0
    right = len(numbers) - 1
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            answer = mid
            left = mid + 1

        elif target > numbers[mid]:
            left = mid + 1

        else:
            right = mid - 1

    return answer
numbers = [10, 20, 20, 20, 30]
print("Last occurrence:", last_occurrence(numbers, 20))

# 6. Count Occurrences
# Count Occurrences finds how many times a target appears in a sorted list.
# It can be calculated using the first and last occurrence.

def count_occurrences(numbers, target):

    first = first_occurrence(numbers, target)
    last = last_occurrence(numbers, target)

    if first == -1:
        return 0

    return last - first + 1
numbers = [10, 20, 20, 20, 30]
print("Count:", count_occurrences(numbers, 20))

# 7. Search Insert Position
# Search Insert Position finds the index where a target should be inserted while keeping the list sorted.

def search_insert(numbers, target):

    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid

        elif target > numbers[mid]:
            left = mid + 1

        else:
            right = mid - 1

    return left
numbers = [10, 20, 30, 40]
print("Insert position:", search_insert(numbers, 25))

# 8. Lower Bound
# Lower Bound finds the first position where an element is greater than or equal to the target.

def lower_bound(numbers, target):

    left = 0
    right = len(numbers)

    while left < right:
        mid = (left + right) // 2

        if numbers[mid] < target:
            left = mid + 1

        else:
            right = mid

    return left
numbers = [10, 20, 30, 40, 50]
print("Lower bound:", lower_bound(numbers, 25))

# 9. Upper Bound
# Upper Bound finds the first position where an element is greater than the target.

def upper_bound(numbers, target):

    left = 0
    right = len(numbers)

    while left < right:
        mid = (left + right) // 2

        if numbers[mid] <= target:
            left = mid + 1

        else:
            right = mid

    return left
numbers = [10, 20, 20, 30, 40]
print("Upper bound:", upper_bound(numbers, 20))

# 10. Binary Search on Descending List
# Binary Search can also work on a list sorted in descending order.
# The comparison conditions are reversed.

def binary_search_descending(numbers, target):

    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid

        elif target < numbers[mid]:
            left = mid + 1

        else:
            right = mid - 1

    return -1
numbers = [70, 60, 50, 40, 30, 20, 10]
print("Index:", binary_search_descending(numbers, 40))

# 11. Binary Search on Rotated Sorted Array
# A rotated sorted array is a sorted array that has been shifted from a particular position.
# Binary Search identifies the sorted half and searches in the appropriate half.

def search_rotated(numbers, target):

    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid

        if numbers[left] <= numbers[mid]:

            if numbers[left] <= target < numbers[mid]:
                right = mid - 1

            else:
                left = mid + 1

        else:

            if numbers[mid] < target <= numbers[right]:
                left = mid + 1

            else:
                right = mid - 1

    return -1
numbers = [30, 40, 50, 10, 20]
print("Index:", search_rotated(numbers, 10))
